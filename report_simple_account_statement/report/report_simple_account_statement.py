 #-*- coding: utf 8 -*-
import pooler
from report import report_sxw
import calendar

from datetime import datetime, date, time, timedelta
import math, pdb

class ReportStatus(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(ReportStatus, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_result': self.get_result,
            'get_company_info': self.get_company_info,
            
        })
              
    def get_result(self, form):
        invoice_obj = form['form']['period_id'][0]
        filtro = [('type', '=', 'in_invoice'),('state', '=', 'open'),('period_id','=', form['form']['period_id'][0])]
        invoice_ids= self.pool.get('account.invoice').search(self.cr, self.uid,filtro,order="date_invoice")
        invoice_obj= self.pool.get('account.invoice').browse(self.cr, self.uid, invoice_ids )
        return invoice_obj
        
    def get_company_info(self,form):
        company = self.pool.get('res.company').search(self.cr, self.uid,[('id','=',1)])
        company_obj= self.pool.get('res.company').browse(self.cr,self.uid,company)
        return company_obj


     # def get_total_debit_credit(self, line_ids):
     #    sum_tot_debit = 0.00
     #    sum_tot_credit = 0.00
     #    for line in line_ids:
     #        sum_tot_debit += (line.debit)
     #        sum_tot_credit += (line.credit)
     #    return {'sum_tot_debit': sum_tot_debit, 'sum_tot_credit': sum_tot_credit}

report_sxw.report_sxw('report.simple.account.statement' ,'report.simple.account.statement.wizard', 'report_simple_account_statement/report/report_simple_account_statement.mako', parser = ReportStatus)

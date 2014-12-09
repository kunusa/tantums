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
            'get_invoices': self.get_invoices,
            'get_company_info': self.get_company_info,
            'get_total_payments': self.get_total_payments,
            'get_accumulate_balance': self.get_accumulate_balance,
            'get_current_period':self.get_current_period,
        })
              
       
    def get_invoices(self,form):
        domain = [('state', '=', 'open'),('period_id','=', form['form']['period_id'][0]),('partner_id','=',form['form']['partner_id'][0])]
        if form['form']['mov_type']:
            domain.append(('type','=',form['form']['mov_type']))
        invoice_ids= self.pool.get('account.invoice').search(self.cr, self.uid,domain,order="date_invoice")
        invoice_obj= self.pool.get('account.invoice').browse(self.cr, self.uid, invoice_ids)
        if (len(invoice_obj) <= 0):
            domain_no_current_invoices=[('state', '=', 'open'),('period_id','!=',form['form']['period_id'][0]),('partner_id','=',form['form']['partner_id'][0])]
            if form['form']['mov_type']:
                domain_no_current_invoices.append(('type','=',form['form']['mov_type']))
            invoice_ids=self.pool.get('account.invoice').search(self.cr, self.uid,domain_no_current_invoices,order="date_invoice")
            invoice_obj= self.pool.get('account.invoice').browse(self.cr, self.uid, invoice_ids)
        return invoice_obj

    def get_current_period(self,form):
        current_period=form['form']['period_id'][0]
        return current_period

        
    def get_company_info(self,form):
        company = self.pool.get('res.company').search(self.cr, self.uid,[('id','=',1)])
        company_obj= self.pool.get('res.company').browse(self.cr,self.uid,company)
        return company_obj


    def get_total_payments(self,payment_ids,period):
        sum_tot_payment = 0.00
        for invoice  in range(0,len(payment_ids)):
            if payment_ids[int(invoice)].period_id.id == period :
                sum_tot_payment += payment_ids[int(invoice)].debit
        return sum_tot_payment

    def get_accumulate_balance(self,partner,period):
        acummulate_balance = 0.00
        credit_sum_tot = 0.00
        debit_sum_tot  = 0.00
        invoice_ids = self.pool.get('account.invoice').search(self.cr,self.uid,[('partner_id','=',partner),('state', '=', 'open'),('residual','>',0),('period_id','<',period)],order="date_invoice")
        invoice_obj = self.pool.get('account.invoice').browse(self.cr,self.uid,invoice_ids)
        for invoice in invoice_obj:
            credit_sum_tot += (invoice_obj[0].amount_total)
        if (len(invoice_obj) > 0):
            for invoice  in range(0,len(invoice_obj[0].payment_ids)):
                if invoice_obj[0].payment_ids[int(invoice)].period_id.id != period:
                    debit_sum_tot += invoice_obj[0].payment_ids[int(invoice)].debit
        acummulate_balance = credit_sum_tot - debit_sum_tot
        return acummulate_balance


report_sxw.report_sxw('report.simple.account.statement' ,'report.simple.account.statement.wizard', 'report_simple_account_statement/report/report_simple_account_statement.mako', parser = ReportStatus)
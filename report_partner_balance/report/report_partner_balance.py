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
            'get_move_lines': self.get_move_lines,
            'get_tc': self.get_tc,
            'get_partners': self.get_partners, 
        })
       
    def get_move_lines(self,form,partner):
        common_domain =[('date','>=',form['form']['date_start']),('date','<=',form['form']['date_finish']),('partner_id','=',partner)]
        journals_supplier = [('type','in',['bank','cash','purchase','general','purchase_refund'])]
        journals_customer = [('type','in',['bank','cash','sale','general','sale_refund'])]
        if (form['form']['mov_type'] == 'customer'):
            journals_ids=self.pool.get('account.journal').search(self.cr,self.uid,journals_customer)
            partner_account=self.get_partner_account('customer',partner)
            common_domain.append(('account_id','=',partner_account.id))
        else:
            journals_ids=self.pool.get('account.journal').search(self.cr,self.uid,journals_supplier)
            partner_account=self.get_partner_account('supplier',partner)
            common_domain.append(('account_id','=',partner_account.id))
        common_domain.append(('journal_id','in',journals_ids))
        if form['form']['centro_costo_id']:
            common_domain.append(('centro_costo_id','=',form['form']['centro_costo_id'][0]))  
        account_movements_ids=self.pool.get('account.move.line').search(self.cr,self.uid,common_domain,order="date")
        account_movements_obj=self.pool.get('account.move.line').browse(self.cr,self.uid,account_movements_ids)
        sum_tot_debit = 0.00
        sum_tot_credit = 0.00
        for line in account_movements_obj:
            # if no base currency
            if line.journal_id.currency:
                if line.debit: 
                    sum_tot_debit  += line.debit/self.get_tc(line.currency_id.id,line.date)
                if line.credit:
                    sum_tot_credit += line.credit/self.get_tc(line.currency_id.id,line.date)
            else:
                if line.debit: 
                    sum_tot_debit  += line.debit
                if line.credit:
                    sum_tot_credit += line.credit
        if (form['form']['mov_type'] == 'customer'):
           return sum_tot_debit - sum_tot_credit
        else:
            return sum_tot_credit - sum_tot_debit

    def get_tc(self,currency_id,date):
        rate =  self.pool.get('res.currency.rate').search(self.cr,self.uid,[('currency_id','=',currency_id),('name','=',date)])    
        if rate:
            return self.pool.get('res.currency.rate').browse(self.cr,self.uid,rate)[0].rate
        else:
            return "No TC"
    
    def get_partner_account(self,partner_type,partner):
        if partner_type == 'supplier':
            return self.pool.get('res.partner').browse(self.cr,self.uid,partner).property_account_payable
        else:
            return self.pool.get('res.partner').browse(self.cr,self.uid,partner).property_account_receivable
       
       
    
    def get_partners(self,partner_type):
        if partner_type == 'custumer':
            common_domain=[('customer','=',True)]
        else:
            common_domain=[('supplier','=',True)]
        partner_ids=self.pool.get('res.partner').search(self.cr,self.uid,common_domain,order="name")
        partner_obj=self.pool.get('res.partner').browse(self.cr,self.uid,partner_ids)
        return partner_obj
        


report_sxw.report_sxw('report.partner.balance','report.partner.balance.wizard', 'report_partner_balance/report/report_partner_balance.mako', parser = ReportStatus)
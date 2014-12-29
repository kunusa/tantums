# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Coded by: Said Kuri Nunez (skuri@tantums.com)
##############################################################################

import datetime
from openerp.osv import fields, osv,orm
import pdb
from openerp.tools.translate import _
	

class report_partner_balance_wizard(osv.osv_memory):
	_name = 'report.partner.balance.wizard'

	
	_columns = {
		'centro_costo_id': fields.many2one('account.cost.center', string="Cost Center"),
		'date_start': fields.date('Start date',required=True),
		'date_finish': fields.date('Date finish', required=True),
		'mov_type': fields.selection([('custumer', 'Customer'),('supplier','Supplier')],'Type',required=True,help="Select movement type"),
	}
	
	_defaults = {
		'mov_type': 'supplier',
		'date_start':  lambda *a: datetime.date.today().strftime('%Y-%m-01'),
		'date_finish':  lambda *a: datetime.date.today().strftime('%Y-%m-%d'),
	}

	def print_report(self,cr,uid,ids,context=None):
		datas = {}
		datas = {'ids': context.get('active_ids', [])}
		datas['model'] = 'report.partner.balance.wizard'
		datas['form'] = self.read(cr, uid, ids)[0]
		return {
			'type': 'ir.actions.report.xml',
			'report_name': 'partner.balance',
			'datas':datas,		
			'report_type' : 'webkit',
		}
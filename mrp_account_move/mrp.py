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
from openerp.osv import osv, fields
import datetime


class mrp_product_produce(osv.Model):
	_inherit = 'mrp.product.produce'

	def do_produce(self, cr, uid, ids, context=None):
		super(mrp_product_produce, self).do_produce(cr, uid, ids, context=context)
		try:
			mo_order=self.pool.get('mrp.production').browse(cr,uid,context['active_id'])
			print mo_order.name
			print ids
			location_id = mo_order.location_src_id.id
			warehouse_ids = self.pool.get('stock.warehouse').search(cr, uid, [('lot_stock_id', '=', location_id)])
			obj_warehouse = self.pool.get('stock.warehouse').browse(cr, uid, warehouse_ids)
			centro_costo_id = obj_warehouse[0].centro_costo_id.id
			today=datetime.date.today().strftime('%Y-%m-01')
			period_ids=self.pool.get('account.period').search(cr,uid,[('date_start','=',today),('special','=',False)])
			account_move = self.pool.get('account.move')
			account_move_line=self.pool.get('account.move.line')
			data_mp = {'name': '/','date': datetime.date.today().strftime('%Y-%m-%d'),'journal_id': 9,'period_id': int(period_ids[0]),'ref': mo_order.name + '-CONSUMO',}
			new_mp = account_move.create(cr,uid,data_mp)
			data = {'name': '/','date': datetime.date.today().strftime('%Y-%m-%d'),'journal_id': 9,'period_id': int(period_ids[0]),'ref': mo_order.name + '-PT',}
			new_pt = account_move.create(cr,uid,data)
			sum_pt=0.00
			sum_mp=0.00
			#Print Account Move Materials
			for mp in  mo_order.move_lines2:
					data_line = { 'name':mo_order.name + '-CONSUMO','journal_id':9,'ref':mo_order.name + '-CONSUMO',
					'credit':mp.product_qty * mp.product_id.standard_price,'debit':0.0,'period_id':int(period_ids[0]),'move_id':new_mp,
					'account_id': mp.product_id.categ_id.property_account_expense_categ.id,'centro_costo_id':centro_costo_id}
					new_line_mp=account_move_line.create(cr,uid,data_line)
					sum_mp += mp.product_qty * mp.product_id.standard_price
			data_line = { 'name':mo_order.name + '-CONSUMO','journal_id':9,'ref':mo_order.name + '-CONSUMO',
					'credit':0.0,'debit':sum_mp,'period_id':int(period_ids[0]),'move_id':new_mp,
					'account_id': 12621,'centro_costo_id':centro_costo_id}
			new_line_mp=account_move_line.create(cr,uid,data_line)
			print mo_order.move_created_ids2
			for pt in  mo_order.move_created_ids2:
				data_line = { 'name':mo_order.name + '-PT','journal_id':9,'ref':mo_order.name + '-PT',
				'credit':0.0,'debit':pt.product_qty * pt.product_id.standard_price,'period_id':int(period_ids[0]),'move_id':new_pt,
				'account_id': pt.product_id.categ_id.property_account_expense_categ.id,'centro_costo_id':centro_costo_id}
				new_line_pt=account_move_line.create(cr,uid,data_line)
				sum_pt += pt.product_qty * pt.product_id.standard_price
			data_line = { 'name':mo_order.name + '-PT','journal_id':9,'ref':mo_order.name + '-PT',
				'credit':sum_pt,'debit':0.0,'period_id':int(period_ids[0]),'move_id':new_pt,
				'account_id': 12621,'centro_costo_id':centro_costo_id}
			new_line=account_move_line.create(cr,uid,data_line)
		except Exception, e:
			print 'ERROR MRP do_produce' + str(e)
		finally:
			return True
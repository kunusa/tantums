#####################################################
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

from openerp.osv import fields, osv
from openerp import pooler
from openerp.tools.translate import _
import pdb


class res_company(osv.osv):
    _inherit = "res.company"
    _columns = {
        'material_process_account_id': fields.many2one(
            'account.account',
            string="Material Process Account"),
        'mrp_journal_account': fields.many2one(
            'account.journal',
            string="MFG Journal"),
    }

res_company()

class mrp_config_settings(osv.osv_memory):
    
    _inherit = 'mrp.config.settings'

    _columns = {
        'module_mrp_account': fields.many2one('account.account', 'Account for Materials on Process',   
            help="""Account for material on process."""),
        'mrp_journal_account': fields.many2one('account.journal', 'Journal for Account Mfg Movements',domain=[('type','=','general')], 
            help="""Select a jorunal for account Movements"""),
    }

    def get_default_module_mrp_account(self, cr, uid, fields, context=None):
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        return {'module_mrp_account': user.company_id.material_process_account_id.id}


    def set_default_module_mrp_account(self, cr, uid, ids, context=None):
            config = self.browse(cr, uid, ids[0], context)
            user = self.pool.get('res.users').browse(cr, uid, uid, context)
            user.company_id.write({'module_mrp_account': config.module_mrp_account.id})


    def get_default_mrp_journal_account(self, cr, uid, fields, context=None):
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        return {'mrp_journal_account': user.company_id.mrp_journal_account.id}


    def set_default_mrp_journal_account(self, cr, uid, ids, context=None):
        config = self.browse(cr, uid, ids[0], context)
        user = self.pool.get('res.users').browse(cr, uid, uid, context)
        user.company_id.write({'mrp_journal_account': config.mrp_journal_account.id})
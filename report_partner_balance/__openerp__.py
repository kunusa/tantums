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
{
    'name' : 'Balance Analityc Partner Report',
    'version' : '1.0',
    'author' : 'Tantums',
    'summary': 'Partner Balance',
    'description': """
Balance Analityc Partner Report
=====================================================
Allows get a Report from partner balance in order show to account payable or account receivable

    """,
    'category': 'Accounting & Finance',
    'sequence': 4,
    'website' : 'http://www.tantums.com',
    'images' : [],
    'depends' : ['base','account','petreo','report_webkit'],
    'demo' : [],
    'data' :       ['data.xml',
                    'wizard/report_partner_balance_view.xml',
                    'report/report_partner_balance.xml'],
    'update_xml' : ['data.xml',
                    'wizard/report_partner_balance_view.xml',
                    'report/report_partner_balance.xml'],
    'test' : [],
    'auto_install': False,  
    'application': True,
    'installable': True,
}

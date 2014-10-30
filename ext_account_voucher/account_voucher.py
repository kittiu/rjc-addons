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

import netsvc
from osv import osv, fields
from tools.translate import _

class account_voucher(osv.osv):
    _inherit = 'account.voucher'
    _columns = {
        'reference': fields.char('Ref #', size=64, readonly=False, help="Transaction reference number."),
        'date_cheque': fields.date('Cheque Date'),
    }
account_voucher()

class account_voucher_line(osv.osv):
    _order = "date_original, move_line_id"
    def _supplier_invoice_number(self, cursor, user, ids, name, arg, context=None):
        res = dict.fromkeys(ids, False)
        cursor.execute('SELECT vl.id, i.supplier_invoice_number \
                        FROM account_voucher_line vl, account_move_line ml, account_invoice i \
                        WHERE vl.move_line_id = ml.id and ml.move_id = i.move_id \
                        AND vl.id IN %s',
                        (tuple(ids),))
        for line_id, supplier_invoice_number in cursor.fetchall():
            res[line_id] = supplier_invoice_number
        return res
    
    _inherit = 'account.voucher.line'
    
    _columns = {
        'supplier_invoice_number': fields.function(_supplier_invoice_number, string='Supplier Invoice Number', type='char'),
        'date_original': fields.related('move_line_id','date', type='date', relation='account.move.line', string='Date', store=True, readonly=1),
    }

account_voucher_line()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

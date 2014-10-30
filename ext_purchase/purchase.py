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

class purchase_order(osv.osv):
    
    def _is_picking_and_service(self, cursor, user, ids, name, arg, context=None):
        res = {}
        for order in self.browse(cursor, user, ids, context=context):
            noprod = self.test_no_product(cursor, user, order, context)
            if noprod and order.invoice_method == 'picking' and order.state == 'approved':
                order.write({'invoice_method':'manual'}, context=context)
                res[order.id] = True
            else:
                res[order.id] = False
        return res

    _inherit = 'purchase.order'
    _columns = {
        # Extend length of field
        'is_picking_and_service': fields.function(_is_picking_and_service, string='No Products', type='boolean'),
    }
    
    def test_no_product(self, cr, uid, order, context):
        for line in order.order_line:
            if line.product_id and (line.product_id.type<>'service'):
                return False
        return True
    
    def test_product_mixed_type(self, cr, uid, ids, context=None):
        is_service = False
        is_non_service = False
        purchase_obj = self.pool.get('purchase.order')
        for order in purchase_obj.browse(cr, uid, ids):
            for line in order.order_line:
                if line.product_id and (line.product_id.type<>'service'):
                    is_non_service = True
                elif line.product_id and (line.product_id.type=='service'):
                    is_service = True
                
        if is_service and is_non_service:
            raise osv.except_osv(_('Warning!'), _('Services and Products can not be mixed together!'))
        return True
    
purchase_order()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

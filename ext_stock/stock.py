# BASED ON REV 8377
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

from openerp.osv import fields, osv

class stock_move(osv.osv):
    _inherit = 'stock.move'
    _order = 'name, date_expected desc, id'
    _columns = {
        'special_info': fields.text('Special Instruction', required=False, select=False, readonly=True, states={'draft': [('readonly', False)]}),
    }

stock_move()

class stock_picking(osv.osv):
    
    _inherit = 'stock.picking'

    def _prepare_invoice_line(self, cr, uid, group, picking, move_line, invoice_id,
        invoice_vals, context=None):
        
        res = super(stock_picking,self)._prepare_invoice_line(cr, uid, group, picking, move_line, invoice_id, invoice_vals, context)
        res.update({
                'special_info': move_line.special_info,
                'prodlot_id':move_line.prodlot_id.id
        })
        return res
        
stock_picking()

#class stock_picking_out(osv.osv):
#    _inherit = 'stock.picking.out'
#    _columns = {
#        'printed': fields.boolean('Printed?'),
#    }
#    _defaults = {
#        'printed': False
#    }
#        
#stock_picking_out()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

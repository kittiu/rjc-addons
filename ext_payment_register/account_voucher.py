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

import time
from lxml import etree

from openerp import netsvc
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _

class account_voucher(osv.osv):

    _inherit = 'account.voucher'
    
    def create_payment_register(self, cr, uid, ids, context=None):
        
        if context is None:
            context = {}
            
        # Validate Payment and Payment Detail Amount
        this = self.browse(cr, uid, ids[0], context=context)
        if this.type == 'receipt':
            if (this.amount_total or 0.0) <> (this.amount or 0.0):
                raise osv.except_osv(_('Unable to save!'), _('Total Amount in Payment Details must equal to Paid Amount'))
            
        payment_register_pool = self.pool.get('payment.register')
        for voucher in self.browse(cr, uid, ids, context=context):
            if voucher.type <> 'receipt': # Only on receipt case.
                continue
            # For each of the Payment Detail, create a new payment detail.
            period_pool = self.pool.get('account.period')
            ctx = context.copy()
            ctx.update({'company_id': voucher.company_id.id})
            for payment_detail in voucher.payment_details:
                pids = period_pool.find(cr, uid, payment_detail.date_due, context=ctx)
                res = { 'voucher_id':voucher.id,
                        'pay_detail_id':payment_detail.id,
                        'original_pay_currency_id':voucher.currency_id and voucher.currency_id.id or voucher.company_id.currency_id.id,
                        'original_pay_amount':payment_detail.amount,
                        'amount':payment_detail.amount,
                        'date':payment_detail.date_due,
                        'period_id':pids and pids[0] or False,
                        # kittiu
                        'name': payment_detail.name,
                        'check_no': payment_detail.check_no,
                        'date_due': payment_detail.date_due,
                }
                payment_register_pool.create(cr, uid, res, context)
                
            self.write(cr, uid, [voucher.id], {'is_paydetail_created':True})

        return True
    
account_voucher()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

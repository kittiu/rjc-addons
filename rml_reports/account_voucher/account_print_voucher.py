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

from report import report_sxw

class voucher(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(voucher, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_total': self.get_total
        })
        
    def get_total(self, voucher):
        if not voucher:
            return False
        else:
            total_amt = 0
            for line in voucher.line_ids:
                if line.type == 'cr':
                    total_amt -= line.amount or 0
                else:
                    total_amt += line.amount or 0
            return total_amt
        
        

report_sxw.report_sxw('report.account.print.voucher.rjc', 'account.voucher', '', parser=voucher, header="internal")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


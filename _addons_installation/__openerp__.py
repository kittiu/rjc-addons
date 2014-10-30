# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2009 Gábor Dukai
#    Modified by Almacom (Thailand) Ltd.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "RJC Addons Installation",
    "version" : "1.0",
    "author" : "kittiu",
    "website" : "http://ecosoft.co.th",
    "description": """
Install all requried modules
""",
    "depends" : ['l10n_th_rjc',
                 'sale','purchase','stock','account','account_voucher','account_accountant','extend_fieldlength',
                 'mrp','base_import','base_report_designer','jasper_reports','ac_report_font_thai','doc_nodelete','partner_route','invoice_cancel_ex',
                 'account_billing','purchase_product_uos','product_uom_bycategory','payment_register','hr_expense_extension','correct_delivery_bymistake',
                 'rml_reports','ext_account','ext_account_voucher','ext_procurement','ext_stock','ext_purchase','ext_sale',
                 'confirm_document_batch','product_attributes','product_variant_multi','account_invoice_merge','purchase_discount',
                 'ext_base','picking_invoice_rel','account_refund_original','security_enhanced','advance_and_additional_discount'],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


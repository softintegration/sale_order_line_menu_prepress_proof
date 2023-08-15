# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    prepress_type = fields.Many2one(related='product_id.prepress_type',store=True)


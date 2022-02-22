# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    width = fields.Integer(string="width", store=True)
    height = fields.Integer(string="height",store=True)
# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    priority_level = fields.Selection([
        ('1_low', 'Low'),
        ('2_medium', 'Medium'),
        ('3_high', 'High')
    ], string="Priority Level", default='1_low')

from odoo import models, fields

class PackConfig(models.Model):
    _name = 'pack.config'
    _description = 'Pack Configuration'

    max_single_line_orders = fields.Integer(string='Max Single Line Orders', default=20)
    max_multi_line_orders = fields.Integer(string='Max Multi Line Orders', default=5)
    single_line_tag = fields.Char(string='Single Line Tag', default='SLSU')
    multi_line_tag = fields.Char(string='Multi Line Tag', default='MLMU')

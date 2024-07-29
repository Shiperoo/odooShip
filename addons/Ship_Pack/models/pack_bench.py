from odoo import models, fields

class PackBench(models.Model):
    _name = 'pack.bench'
    _description = 'Pack Bench'

    name = fields.Char(string='Name', required=True)
    location_ids = fields.Many2many('stock.location', string='Virtual Locations')
    user_id = fields.Many2one('res.users', string='User', ondelete='set null')

from odoo import models, fields

class InventoryMessageLog(models.Model):
    _name = 'inventory.message.log'
    _description = 'Inventory Message Log'

    picking_id = fields.Many2one('stock.picking', string='Picking', required=True)
    message = fields.Text(string='Message')
    status = fields.Selection([('sent', 'Sent'), ('received', 'Received')], string='Status')
    received_at = fields.Datetime(string='Received At')

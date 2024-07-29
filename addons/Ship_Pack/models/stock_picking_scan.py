from odoo import models, fields, api
from odoo.exceptions import UserError

class StockPickingScanProduct(models.TransientModel):
    _name = 'stock.picking.scan.product'
    _description = 'Scan Product'

    picking_id = fields.Many2one('stock.picking', string='Picking')
    product_barcode = fields.Char(string='Product Barcode')

    @api.model
    def default_get(self, fields):
        res = super(StockPickingScanProduct, self).default_get(fields)
        res.update({
            'picking_id': self.env.context.get('default_picking_id')
        })
        return res

    def scan_product(self):
        self.ensure_one()
        product = self.picking_id.scan_product(self.product_barcode)
        return {'type': 'ir.actions.act_window_close'}


class StockPickingScanLocation(models.TransientModel):
    _name = 'stock.picking.scan.location'
    _description = 'Scan Virtual Location'

    picking_id = fields.Many2one('stock.picking', string='Picking')
    location_id = fields.Many2one('stock.location', string='Location')

    @api.model
    def default_get(self, fields):
        res = super(StockPickingScanLocation, self).default_get(fields)
        res.update({
            'picking_id': self.env.context.get('default_picking_id')
        })
        return res

    def scan_location(self):
        self.ensure_one()
        self.picking_id.scan_virtual_location(self.location_id.id)
        return {'type': 'ir.actions.act_window_close'}


class StockPickingScanBag(models.TransientModel):
    _name = 'stock.picking.scan.bag'
    _description = 'Scan Bag ID'

    picking_id = fields.Many2one('stock.picking', string='Picking')
    bag_id = fields.Char(string='Bag ID')

    @api.model
    def default_get(self, fields):
        res = super(StockPickingScanBag, self).default_get(fields)
        res.update({
            'picking_id': self.env.context.get('default_picking_id')
        })
        return res

    def scan_bag(self):
        self.ensure_one()
        self.picking_id.scan_bag_id(self.bag_id)
        return {'type': 'ir.actions.act_window_close'}

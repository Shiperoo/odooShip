from odoo import models, fields, api

class ScanProduct(models.TransientModel):
    _name = 'stock.picking.scan.product'
    _description = 'Scan Product'

    picking_id = fields.Many2one('stock.picking', string='Picking')
    product_barcode = fields.Char(string='Product Barcode')

    def scan_product(self):
        # Logic to scan product
        pass

class ScanLocation(models.TransientModel):
    _name = 'stock.picking.scan.location'
    _description = 'Scan Location'

    picking_id = fields.Many2one('stock.picking', string='Picking')
    location_id = fields.Many2one('stock.location', string='Location')

    def scan_location(self):
        # Logic to scan location
        pass

class ScanBag(models.TransientModel):
    _name = 'stock.picking.scan.bag'
    _description = 'Scan Bag'

    picking_id = fields.Many2one('stock.picking', string='Picking')
    bag_id = fields.Char(string='Bag ID')

    def scan_bag(self):
        self.picking_id.scan_bag_id(self.bag_id)

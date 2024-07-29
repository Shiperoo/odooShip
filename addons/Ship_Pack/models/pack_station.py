from odoo import models, fields, api

class PackStation(models.Model):
    _name = 'pack.station'
    _description = 'Pack Station'

    name = fields.Char(string='Pack Station Name', required=True)
    hu_scanned = fields.Boolean(string='HU Scanned', default=False)
    virtual_locations = fields.One2many('stock.location', 'pack_station_id', string='Virtual Locations')
    pack_bench_id = fields.Many2one('stock.location', string='Pack Bench')

    def scan_hu(self, hu_id):
        picking = self.env['stock.picking'].search([('hu_id', '=', hu_id)])
        if not picking:
            raise ValueError("HU not found.")
        self.write({'hu_scanned': True})
        return picking

    def sort_lines(self, picking):
        if not self.hu_scanned:
            raise ValueError("HU not scanned.")
        # Sorting logic for SLSU and MLMU
        for line in picking.move_lines:
            if picking.tag == 'SLSU':
                # Logic for single line orders
                pass
            elif picking.tag == 'MLMU':
                # Logic for multi line orders
                pass
        self.write({'hu_scanned': False})

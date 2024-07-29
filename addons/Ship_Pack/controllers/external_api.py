# This is an optional controller script if you need to expose any endpoints or handle external API interactions
from odoo import http

class ExternalAPIController(http.Controller):

    @http.route('/api/confirmations', type='json', auth='public')
    def receive_confirmations(self, **kwargs):
        message = kwargs.get('message')
        http.request.env['stock.picking'].receive_confirmation_message(message)
        return {'status': 'success'}

from odoo import models, fields, api


class FleetVehicleInherit(models.Model):
    _inherit = 'fleet.vehicle'

    model_id = fields.Many2one('fleet.vehicle.model', 'Model',
                               tracking=True, required=False, help='Model of the vehicle')

    indicative_value = fields.Char(string='Indicative Value', help='The indicative value of the vehicle')
    body_style = fields.Char(string='Body Style', help='The body style of the vehicle')
    registration_date = fields.Char(string='Registration Date', help='The registration date of the vehicle')
    last_inspection_date = fields.Char(string="Last Inspection Date", help='The date of the last vehicle inspection')

    def fetch_vehicle_details(self):
        """override this method to suit your api"""

    def _search_vehicle_make(self, make):
        make_id = self.env['fleet.vehicle.model.brand'].search([('name', '=ilike', make)], limit=1)
        if not make_id:
            make_id = self.env['fleet.vehicle.model.brand'].create({
                'name': make
            })
        return make_id

    def _search_vehicle_model(self, model, make):
        model_id = self.env['fleet.vehicle.model'].search([
            ('name', '=ilike', make), ('brand_id', '=', self._search_vehicle_make(make).id)], limit=1)
        if not model_id:
            model_id = self.env['fleet.vehicle.model'].create({
                'name': model,
                'brand_id': self._search_vehicle_make(make).id
            })
        return model_id


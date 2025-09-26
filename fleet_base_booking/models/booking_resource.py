from odoo import fields, models, api

class BookingResource(models.Model):
    _inherit = 'booking.resource'

    fleet_vehicle_ids = fields.One2many('fleet.vehicle', 'booking_resource_id', string='Fleet Vehicle')

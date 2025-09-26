from odoo import api, fields, models

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    booking_resource_id = fields.Many2one('booking.resource', string='Booking Resource')

    @api.model_create_multi
    def create(self, vals_list):
        fleet_vehicles = super().create(vals_list)

        for fleet_vehicle in fleet_vehicles:
            if not fleet_vehicle.booking_resource_id:
                fleet_vehicle.booking_resource_id = fleet_vehicle.env['booking.resource'].sudo().create({
                    'name': f'{fleet_vehicle.name} - {fleet_vehicle.vin_sn}',
                    'capacity': 1,
                    'fleet_vehicle_ids': fleet_vehicle,
                })

        return fleet_vehicles

    def write(self, vals):
        fleet_vehicle = super().write(vals)

        if not self.active:
            self.booking_resource_id.sudo().active = False
        else:
            if self.booking_resource_id:
                self.booking_resource_id.sudo().write({
                    'name': f'{self.name} - {self.vin_sn}',
                    'capacity': 1,
                })

        return fleet_vehicle

    def unlink(self):
        for fleet_vehicle in self:
            fleet_vehicle.booking_resource_id.sudo().unlink()

        return super().unlink()

    @api.ondelete(at_uninstall=True)
    def _delete_linked_resources(self):
        for fleet_vehicle in self:
            fleet_vehicle.booking_resource_id.unlink()
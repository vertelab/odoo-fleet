# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models

def _fleet_vehicle_booking_after_init(env):
    fleet_vehicles = env['fleet.vehicle'].search([('booking_resource_id', '=', False)])
    for fleet_vehicle in fleet_vehicles:
        fleet_vehicle.booking_resource_id = fleet_vehicle.env['booking.resource'].sudo().create({
            'name': f'{fleet_vehicle.name} - {fleet_vehicle.vin_sn}',
            'capacity': 1,
            'fleet_vehicle_ids': fleet_vehicle,
        })
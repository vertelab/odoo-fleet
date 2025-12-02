from odoo import models, fields, api, _

class AccountAsset(models.Model):
    _inherit = 'account.asset'

    vehicle_id = fields.Many2one('fleet.vehicle', readonly=True)

    def action_view_vehicle(self):
        return {
            'name': _('Vehicle'),
            'type': 'ir.actions.act_window',
            'res_model': 'fleet.vehicle',
            'view_mode': 'form',
            'res_id': self.vehicle_id.id
        }



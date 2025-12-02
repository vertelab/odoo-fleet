from odoo import models, fields, api, _

class AccountLoan(models.Model):
    _inherit = 'account.loan'

    vehicle_id = fields.Many2one('fleet.vehicle', readonly=True)

    def action_view_vehicle(self):
        return {
            'name': _('Vehicle'),
            'type': 'ir.actions.act_window',
            'res_model': 'fleet.vehicle',
            'view_mode': 'form',
            'res_id': self.vehicle_id.id
        }



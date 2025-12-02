from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _account_loan(self, line):
        res = super()._account_loan(line)
        res.vehicle_id = line.vehicle_id.id
        return res


    def action_post(self):
        res = super().action_post()
        for line in self.invoice_line_ids:
            if line.asset_profile_id and line.asset_id:
                line.vehicle_id.asset_id = line.asset_id.id
        return res
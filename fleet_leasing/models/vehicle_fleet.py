from odoo import models, fields, api, _

class VehicleFleet(models.Model):
    _inherit = 'fleet.vehicle'

    asset_id = fields.Many2one('account.asset', string="Asset")
    account_loan_ids = fields.One2many('account.loan', 'vehicle_id', string="Loan")

    @api.depends('account_loan_ids')
    def _compute_account_loan(self):
        for rec in self:
            if rec.account_loan_ids:
                rec.account_loan_count = len(rec.account_loan_ids)
            else:
                rec.account_loan_count = 0

    account_loan_count = fields.Integer(string="Loan", compute=_compute_account_loan)

    def action_view_asset(self):
        return {
            'name': _('Asset'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.asset',
            'view_mode': 'form',
            'res_id': self.asset_id.id
        }

    def action_view_loan(self):
        return {
            'name': _('Loans'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.loan',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.account_loan_ids.ids)],
            'context': {'default_vehicle_id': self.id}
        }
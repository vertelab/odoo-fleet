from datetime import timedelta
from dateutil.relativedelta import relativedelta
from odoo import _, api, fields, models, Command
from odoo.exceptions import ValidationError, UserError


class ContractLine(models.Model):
    _inherit = "contract.line"

    vehicle_id = fields.Many2one('fleet.vehicle', readonly=True, related='loan_id.vehicle_id', store=True)
    #Can't create a method called _description since it overides the attribute. Can't find the super function were extending.
    def _description_dep(self, base_sequence, total_amount):
        if self.vehicle_id:
            lines = [{
                'display_type': 'line_section',
                'name': _('Loan Details for: %s (%s) - Total: %.2f kr') % (
                    self.vehicle_id.name, self.loan_id.name, total_amount
                ),
                'sequence': base_sequence,
            }]
            return lines

        return super()._description(base_sequence, total_amount)

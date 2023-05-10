from odoo import models, fields, api
import requests
import json
from requests.auth import HTTPBasicAuth
import logging


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    vehicle_api_username = fields.Char(
        string="Vehicle API Username",
        config_parameter='vehicle_api_username')
    vehicle_api_password = fields.Char(
        string="Vehicle API Password",
        config_parameter='vehicle_api_password')
    reg_check_url = fields.Char(
        string="Reg Check URL",
        config_parameter='reg_check_url')

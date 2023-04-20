from odoo import models, fields, api
import requests
import json
from requests.auth import HTTPBasicAuth
import logging


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    biluppgifter_url = fields.Char(
        string="URL",
        config_parameter='biluppgifter_url')

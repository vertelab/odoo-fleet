from odoo import models, fields, api
import requests
import json
from requests.auth import HTTPBasicAuth
import logging
import re
from bs4 import BeautifulSoup


class FleetVehicleInherit(models.Model):
    _inherit = 'fleet.vehicle'

    def fetch_vehicle_details(self):
        data = self._api_reg_check_request(self.license_plate)
        if data:
            self.color = data.get("Colour")
            self.fuel_type = data.get('FuelType').get("CurrentTextValue", '').lower()

            car_make = data.get('CarMake', {'CurrentTextValue': ''}).get("CurrentTextValue", "")
            car_model = data.get('CarModel', {'CurrentTextValue': ''}).get("CurrentTextValue", "")

            self.model_id = self._search_vehicle_model(car_model.title(), car_make.title()).id

            engine_size = data.get('EngineSize', {'': ''}).get("CurrentTextValue", "").replace(' ', '').strip().split('/')
            if len(engine_size) > 1:
                self.horsepower = int(engine_size[1][:-2])
                self.power = int(engine_size[0][:-2])
            self.body_style = data.get('BodyStyle', {'CurrentTextValue': ''}).get("CurrentTextValue", "")
            self.indicative_value = data.get('IndicativeValue', {'CurrentTextValue': ''}).get("CurrentTextValue", "")
            seats = data.get('NumberOfSeats').get("CurrentTextValue", 0)
            self.seats = int(seats) if seats != '' else 0
            self.registration_date = data.get('RegistrationDate')

    def _api_reg_check_request(self, vehicle_reg_no):
        username = self.env['ir.config_parameter'].sudo().get_param('vehicle_api_username')
        password = self.env['ir.config_parameter'].sudo().get_param('vehicle_api_password')
        reg_check_url = self.env['ir.config_parameter'].sudo().get_param('reg_check_url')
        url = f"{reg_check_url}/{vehicle_reg_no.replace(' ', '')}"

        reg_check_response = requests.get(url, auth=HTTPBasicAuth(username, password))
        if reg_check_response.status_code == requests.codes['ok']:
            return reg_check_response.json()


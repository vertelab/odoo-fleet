from odoo import models, fields, api
import requests
import logging
import json
from requests.auth import HTTPBasicAuth
import re
from bs4 import BeautifulSoup


_logger = logging.getLogger(__name__)


class FleetVehicleInherit(models.Model):
    _inherit = 'fleet.vehicle'

    def fetch_vehicle_details(self):
        data = self._api_reg_check_request(self.license_plate)
        if data:
            self.color = data.get("Colour")
            fuel_type = data.get('FuelType').get("CurrentTextValue", '').lower()
            if fuel_type == 'bensin':
                self.fuel_type = 'gasoline'
            elif fuel_type == 'el':
                 self.fuel_type = 'electric'
            else:
                self.fuel_type = fuel_type
            
            
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
            
            transmission = data.get('Transmission').lower()
            
            if transmission == 'manuell':
                transmission = 'manual'
            else:
                transmission = 'automatic'
                
            self.transmission = transmission
         

    def _api_reg_check_request(self, vehicle_reg_no):
        username = self.env['ir.config_parameter'].sudo().get_param('vehicle_api_username')
        password = self.env['ir.config_parameter'].sudo().get_param('vehicle_api_password')
        reg_check_url = self.env['ir.config_parameter'].sudo().get_param('reg_check_url')
        url = f"{reg_check_url}/{vehicle_reg_no.replace(' ', '')}"
        reg_check_response = requests.get(url, auth=HTTPBasicAuth(username, password))
        if reg_check_response.status_code == requests.codes['ok']:
            _logger.info("API Respons %s", reg_check_response.json())
            return reg_check_response.json()


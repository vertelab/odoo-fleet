from odoo import models, fields, api
import requests
import json
from requests.auth import HTTPBasicAuth
import logging
import re
from bs4 import BeautifulSoup


class FleetVehicleInherit(models.Model):
    _inherit = 'fleet.vehicle'

    def _scrape_bluppgifter(self, plate_number):
        biluppgifter_url = self.env['ir.config_parameter'].sudo().get_param('biluppgifter_url')
        vgm_url = f"{biluppgifter_url}/{plate_number}"
        html_text = requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        crawled_data = {}

        for li in soup.find(class_="list-data enlarge").find_all('li'):
            label = li.find("span", "label").text.strip()
            value = li.find("span", "value").text.strip()
            crawled_data[label] = value
        
        for list_data_div in soup.find_all(class_="list-data mb-4 enlarge"):
            for li in list_data_div.find_all('li'):
                label = li.find("span", "label").text.strip()
                value = li.find("span", "value").text.strip()
                crawled_data[label] = value
                
        return crawled_data
    
    def fetch_vehicle_details(self):
        details = self._scrape_bluppgifter(self.license_plate)
        self.color = details.get('Färg')
        self.vin_sn = details.get('Chassinr / VIN')
        self.seats = int(''.join(re.findall(r'\d+', details.get('Passagerare')))) + 1
        fabrikat = details.get('Fabrikat').split('-')[0]
        self.model_id = self._search_vehicle_model(details.get('Modell'), fabrikat).id
        
        logging.warning(f"{details.get('Mätarställning (besiktning)')}")
        if details.get('Mätarställning (besiktning)', False):
            self.odometer = int(''.join(re.findall(r'\d+', details.get('Mätarställning (besiktning)'))))
            
        if details.get('CO2-utsläpp (NEDC)', False):
            self.co2 = int(''.join(re.findall(r'\d+', details.get('CO2-utsläpp (NEDC)'))))
        self.model_year = details.get('Fordonsår / Modellår')
        self.body_style = details.get('Kaross')
        
        self.registration_date = details.get('Först registrerad')
        self.last_inspection_date = details.get('Senast besiktigad')
        
        if details.get('Växellåda') == 'Manuell':
         self.transmission = 'manual'
        else:
            self.transmission = 'automatic'

        if details.get('Drivmedel') == 'Bensin':
            self.fuel_type = 'gasoline'
        elif details.get('Drivmedel') == 'El':
            self.fuel_type = 'electric'
        else:
            self.fuel_type = details.get('Drivmedel').lower()

        engine_size = details.get('Motoreffekt').replace(' ', '').strip().split('/')
        if len(engine_size) > 1:
            self.horsepower = int(engine_size[0][:-2])
            self.power = int(engine_size[1][:-2])
        
                                                                                                                                                                                                                                                                                                                        





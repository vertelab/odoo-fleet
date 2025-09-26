# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2023- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Fleet Booking',
    'version': '18.0.0.0.0',
    'summary': '',
    'category': 'Human Resources/Fleet',
    'description': """Vehicle Booking""",
    # 'sequence': '1',
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-fleet/fleet_base_booking',
    'images': ['static/description/banner.png'],  # 560x280 px.
    'license': 'AGPL-3',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-fleet',
    'depends': ['base_booking', 'fleet'],
    'demo': [
        'demo/fleet_booking_demo.xml'
    ],
    'data': [
        'views/fleet_vehicle_views.xml',
    ],
    'post_init_hook': '_fleet_vehicle_booking_after_init',
    'installable': True,
    'auto_install': True,
    'application': False,
}
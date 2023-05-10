from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
from babel.dates import format_datetime, format_date

from werkzeug.urls import url_encode

from odoo import http, _, fields
from odoo.http import request
from odoo.tools import html2plaintext, DEFAULT_SERVER_DATETIME_FORMAT as dtf
from odoo.tools.misc import get_lang
from odoo.addons.website_calendar_ce.controllers.main import WebsiteCalendar
import uuid
import logging

_logger = logging.getLogger(__name__)


class WebsiteVehicleCalendar(WebsiteCalendar):
    @http.route([
        '/website/calendar/search'], type='http', auth="public", website=True)
    def search_plate_number(self, **kwargs):
        return request.render("fleet_regcheck.vehicle_search")

    @http.route([
        '/website/calendar/carinput'], type='http', auth="public", website=True)
    def search_plate_number(self, **kwargs):
        return request.render("vehicle_booking_ce.carinput")

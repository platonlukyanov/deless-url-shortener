from datetime import datetime
from django.http import HttpRequest
from django.utils import timezone as set_timezone
from pytz import timezone
import requests
from user_agents import parse
from user_agents.parsers import UserAgent, Browser, OperatingSystem


class RequestParser:
    """Class for transforming request to information about request"""

    def __init__(self, request: HttpRequest):
        self.request = request

    def get_client_ip(self, request: HttpRequest) -> str:
        """Gets Clients IP Address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip)
        return ip

    def get_request_info(self) -> dict:
        """Gets referer, user ip address, user agent in dictionary from request"""
        return {
            "referer": self.request.META.get("HTTP_REFERER", ""),
            "user_ip": self.get_client_ip(self.request),
            "user_agent": self.request.headers.get("User-Agent" ""),
        }

    def get_ip_info(self, ip: str, created: datetime = set_timezone.now()) -> dict:
        """Getting IP data by ipapi.com"""
        URL = "https://ipapi.co/{}/json".format(str(ip))
        r = requests.get(URL)
        if not (200 <= r.status_code < 400):
            print(r.status_code)
            return {}
        data = r.json()

        return {
            "city": data.get("city", ""),
            "country": data.get("country_code", ""),
            "latitude": data.get("latitude", 0),
            "longitude": data.get("longitude", 0),
            "ip_datetime": self._get_zone_current_time(data.get("timezone", "Europe/Moscow"), created=created),
        }

    def get_user_agent_info(self, user_agent: str) -> dict:
        """Gets device type, browser and os from user-agent string"""
        user_agent_object = parse(str(user_agent))
        return {
            "device_type": self._recognize_device_type(user_agent_object),
            "browser": self._get_browser_fullname(user_agent_object.browser),
            "os": self._get_os_fullname(user_agent_object.os),
        }

    def set_attributes_from_dictionary(self, dictionary: dict) -> None:
        """Set attributes from dictionary by iterating on them and using setattr()"""
        for key, value in dictionary.items():
            setattr(self, key, value)

    @staticmethod
    def _get_zone_current_time(zone: str, created: datetime = None) -> datetime:
        """Gets Datetime in set timezone"""
        if created:
            now = created
        else:
            now = set_timezone.now()
        foreign_zone = timezone(str(zone))
        return now.astimezone(foreign_zone)

    @staticmethod
    def _get_os_fullname(os: OperatingSystem) -> str:
        """Creates browser fullname containing browser family and version"""
        family = getattr(os, 'family', "")
        version = getattr(os, "version_string", "")
        return family + " " + version

    @staticmethod
    def _get_browser_fullname(browser: Browser) -> str:
        """Creates browser fullname containing browser family and version"""
        family = getattr(browser, 'family', "")
        version = getattr(browser, "version_string", "")
        return family + " " + version

    @staticmethod
    def _recognize_device_type(user_agent: UserAgent) -> str:
        """Recognizes type of device by UserAgent object"""
        device_type = "desktop"
        if user_agent.is_mobile:
            device_type = "mobile"
        if user_agent.is_tablet:
            device_type = "tablet"
        elif user_agent.is_pc:
            device_type = "desktop"
        elif user_agent.is_bot:
            device_type = "bot"
        return device_type

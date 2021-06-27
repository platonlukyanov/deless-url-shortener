from django.http import HttpRequest
from django.utils import timezone
from shortener.models import Link
from pprint import pprint
from .parser import RequestParser
from .redis import redis_client
from .models import LinkOpening


def record_link_request(request: HttpRequest, link: Link) -> LinkOpening:
    """Makes a record in database about request"""
    parser = RequestParser(request)
    request_info = parser.get_request_info()
    user_agent_info = parser.get_user_agent_info(request_info.get("user_agent", ""))
    request_info = {**request_info, **user_agent_info}

    # Setting Request and User agent info into fields
    link_opening = LinkOpening()
    link_opening.ip = request_info.get("user_ip", "")
    link_opening.user_agent = request_info.get("user_agent", "")
    link_opening.from_site = request_info.get("referer", "")
    link_opening.device_type = request_info.get("device_type", "")
    link_opening.browser = request_info.get("browser", "")
    link_opening.os = request_info.get("os", "")

    # Link Relation
    link_opening.link = link
    # Saving and setting information about IP after getting created date
    link_opening.save()
    ip_info = parser.get_ip_info(request_info.get("user_ip", ""), created=link_opening.created)
    pprint(ip_info)
    request_info.update(ip_info)
    link_opening.city = request_info.get("city", "")
    link_opening.country = request_info.get("country", "")
    link_opening.latitude = request_info.get("latitude", 0)
    link_opening.longitude = request_info.get("longitude", 0)
    link_opening.time_for_opener = request_info.get("ip_datetime", link_opening.created)
    link_opening.save()
"""phone lookup requests route"""
import re

from flask import Blueprint, request
from phone_iso3166.country import *

from utils import extract_info

phone_lookup_api = Blueprint("v1", __name__)


@phone_lookup_api.route("/phone-numbers")
def phone_number_lookup():
    """phone number request handling"""
    response = dict()
    phone_number = request.args.get("phoneNumber", None)
    phone_number_len = len(phone_number.replace("+", "").replace(" ", ""))
    if (
        bool(re.match("^[0-9 ^+]*$", phone_number)) == False
        or len(phone_number.split()) > 3
        or "  " in phone_number
    ):
        return {"error": "phone number invalid"}

    try:
        extract_country_code= phone_country(phone_number)
    except:
        return {"error": "phone number invalid"}

    country_code = request.args.get("countryCode", extract_country_code)
    if country_code is None or phone_number_len < 11:
        return {
            "phoneNumber": phone_number,
            "error": {"countryCode": "required value is missing"},
        }
    response = extract_info(phone_number, country_code)
    return response

import phonenumbers
from phonenumbers.phonenumberutil import (
    region_code_for_country_code,
)


def extract_info(phone, country_code):
    """
    This function extracts the info required using the 'phone' and 'country_code' passed to it
    """
    response = dict()
    pn = phonenumbers.parse(phone, country_code)
    validity = phonenumbers.is_valid_number(pn)

    if validity:

        national_number = phonenumbers.national_significant_number(pn)
        area_code_length = phonenumbers.length_of_geographical_area_code(pn)
        country_code_string = region_code_for_country_code(pn.country_code)
        area_code = ""
        subscriber_number = ""

        if area_code_length > 0:
            area_code = national_number[:area_code_length]
            subscriber_number = national_number[area_code_length:]

        else:
            area_code = ""
            subscriber_number = national_number

        response["phoneNumber"] = phone
        response["countryCode"] = country_code_string
        response["areaCode"] = area_code
        response["localPhoneNumber"] = subscriber_number
        return response

    return {"error": "phone number invalid"}

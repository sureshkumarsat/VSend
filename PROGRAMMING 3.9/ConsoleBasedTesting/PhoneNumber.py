import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


number = input("Enter Number : ")
ch_number = phonenumbers.parse(number, "CH")

print(geocoder.description_for_number(ch_number, "en"))

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

gb_number = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(gb_number))

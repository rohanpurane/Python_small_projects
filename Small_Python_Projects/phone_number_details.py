import string
import phonenumbers
from phonenumbers import timezone,geocoder,carrier


# phone no. must be a string
# phone no. must be after country code

number = input('Enter your Phone-Number with country-code: ')
phone = phonenumbers.parse(number)   # "parse" gives us all details of number 

time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")   # "en" is language
registration = geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(car)
print(registration)
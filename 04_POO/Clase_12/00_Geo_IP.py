#181.9.198.73
#pip install geocoder
import geocoder as geo

info = geo.ip("181.9.198.73")

print(info.city)
print(info.country)
print(info.address)
print(info.hostname)
print(info.latlng)
# pip install geocoder
import geocoder as geo

# info = geo.ip("181.2.54.100")
# print(info.city)
# print(info.country)
# print(info.address)
# print(info.hostname)
# print(info.latlng)

# import geocoder

# Obtener información de geolocalización de la IP pública
info = geo.ip('181.2.54.100')

# Función para imprimir información si está disponible
def print_info(label, value):
    if value:
        print(f"{label}: {value}")
    else:
        print(f"{label}: No disponible")

# Imprimir la información
print_info("City", info.city)
print_info("LatLng", info.latlng)
print_info("Country", info.country)
print_info("State", info.state)
print_info("Postal", info.postal)
print_info("Org", info.org)
#print_info("Timezone", info.timezone)
print_info("Address", info.address)
print_info("IP", info.ip)
print_info("Hostname", info.hostname)
#print_info("Continent", info.continent)
#print_info("Region", info.region)

from trips import trips, city_not_avaible, new_trip, country_by_city
from passengers import pasajeros, new_passenger, search_passenger, passenger_data, filter_by_city, filter_by_country

def ask():
  return input("\nElige una opción \n[a] Registrar un nuevo pasajero.\n[b] Registrar una nuevo viaje.\n[c] Ver pasajeros.\n[d] Ver destinos\n[e] Buscar pasajero\n[f] Buscar pasajeros por ciudad\n[g] Buscar pasajeros por país\n[x] Salir.\nR. ")

def registrar_pasajero():
  nombre= input("\tDigite el nombre del pasajero: ")
  dni= int(input("\tDigite el número de identificación del pasajero: "))
  ciudad= input("\tDigite la ciudad destino del pasajero: ")
  while city_not_avaible(ciudad):
    print("\t[x] ciudad no disponible.")
    ciudad= input("\tDigite la ciudad destino del pasajero: ")
  if new_passenger((nombre, dni, ciudad)):
    print("\nSe ingresó un nuevo pasajero\n")

def registrar_viaje():
  ciudad= input("\tDigite la ciudad: ")
  pais= input("\tDigite el pais: ")
  if new_trip((ciudad, pais)):
    print("\nSe ingresó un nuevo destino\n")
  
def pasajeros_list():
  for i, n in enumerate(n for n, t, c in pasajeros):
    print("\t%s. %s" % (i, n))

def passenger():
  name, dni, city= search_passenger(int(input("\tDigite el DNI del pasajero\n\tR.")))
  print("\nEl pasajero %s viaja a %s, %s" % (name, city, country_by_city(city)))

def viajes_list():
  for i, (c, p) in enumerate(trip for trip in trips):
    print("\t%s. %s, %s" % (i+1, c, p))

def passengers_to_city():
  city= input("\tDigite la ciudad donde quiere obtener los pasajeros\n\tR. ")
  pasajeros= filter_by_city(city)
  print("\nHacia %s van a ir.\n" % (city))
  for i, p in enumerate(n for n, d, c in pasajeros):
    print("\t%s. %s" % (i+1, p))

def passengers_to_country():
  country= input("\tDigite el país donde quiere obtener los pasajeros\n\tR. ")
  pasajeros= filter_by_country(country)
  print("\nHacia %s van a ir.\n" % (country))
  for i, p in enumerate(n for n, d, c in pasajeros):
    print("\t%s. %s" % (i+1, p))

def options(opt):
  action= {
    'a': registrar_pasajero,
    'b': registrar_viaje,
    'c': pasajeros_list,
    'd': viajes_list,
    'e': passenger,
    'f': passengers_to_city,
    'g': passengers_to_country
  }
  return action[opt]()

"""
INICIO DEL PROGRAMA
"""

entrada= ask()

while entrada != 'x':
  options(entrada)
  entrada= ask()
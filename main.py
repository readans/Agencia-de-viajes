from trips import trips, city_not_avaible, new_trip
from passengers import pasajeros, new_passenger, search_passenger, passenger_data, filter_by_city, filter_by_country

def ask():
  return input("\nElige una opción \n[a] Registrar un nuevo pasajero.\n[b] Registrar una nuevo viaje.\n[c] Ver pasajeros.\n[d] Ver destinos\n[x] Salir.\nR. ")

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

def viajes_list():
  for i, (c, p) in enumerate(trip for trip in trips):
    print("\t%s. %s, %s" % (i, c, p))

def options(opt):
  action= {
    'a': registrar_pasajero,
    'b': registrar_viaje,
    'c': pasajeros_list,
    'd': viajes_list
  }
  return action[opt]()

"""
INICIO DEL PROGRAMA
"""

entrada= ask()

while entrada != 'x':
  options(entrada)
  entrada= ask()

# result= new_passenger(('Juan Alberto Acosta', 43567892, 'Lisboa'))
# if result == None:
#   print("No se pudo registrar al pasajero")

# passenger_found= search_passenger(578673423)
# name, dni, city, country= passenger_data(passenger_found)
# print(f"El pasajero {name} se dirije al destino {city}, {country}")
# print("la cantidad de pasajeros que viajan a %s son %s" % (city, len(filter_by_city(city))))
# print("La cantidad de pasajeros que se dirigen a %s son %s" % ('Escocia', len(filter_by_country('Escocia'))))
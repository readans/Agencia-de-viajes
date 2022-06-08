from trips import city_by_country, city_not_avaible, country_by_city

pasajeros= [('Leider Juarez', 22356789, 'Madrid'), ('Philip Figeroa', 578673423, 'Lisboa'), ('Carla Putin', 235678342, 'Glasgow'), ('Manuel Suarez', 19823451, 'Liverpool'), ('Silvana Paredes', 22709128, 'Buenos Aires'), ('Rosa Ortiz', 15123978, 'Glasgow'), ('Luciana Hernández', 38981374, 'Lisboa')] # Default passengers

def search_passenger(dni: int):
  return tuple(filter(lambda p: p[1] == dni, pasajeros))[0]

def passenger_data(pasajero: tuple):
  data= list(pasajero)
  data.append(country_by_city(pasajero[-1]))
  return data

def filter_by_city(city: str):
  return list(filter(lambda p: p[-1] == city, pasajeros))

def filter_by_country(country: str):
  city= city_by_country(country)
  return list(filter(lambda p: p[-1] == city, pasajeros))

def new_passenger(pasajero: tuple):
  # if city_not_avaible(pasajero[2]):
  #   print("No contamos con disponibilidad hasta esa zona")
  #   return
  pasajeros.append(pasajero)
  return True
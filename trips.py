trips= [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Lisboa", "Portugal"), ("Liverpool", "Inglaterra"), ("Madrid", "España")] # Default trips

#countries= tuple(y for x, y in trips)

def city_not_avaible(city):
  cities= tuple(x for x, y in trips)
  return city not in cities

def country_by_city(city):
  for x, y in trips:
    if x == city:
      return y

def city_by_country(country):
  for x, y in trips:
    if y == country:
      return x

def new_trip(trip: tuple):
  trips.append(trip)
  return True
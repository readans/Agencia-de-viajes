from trips import trips
pasajeros= []

def new_passenger(pasajero: tuple):
  if pasajero[2] not in trips:
    print("No contamos con disponibilidad hasta esa zona")
    return
  pasajeros.append(pasajero)

new_passenger(('Juan Alberto Acosta', 43567892, 'Oslo'))
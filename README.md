# Por qué se hizo este programa?

Bueno. Este programa python se realizó para la solución de un problema propuesto como recuperación del ciclo uno en MinTic

# Descripción del problema

Escribir un programa que permita procesar información de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, cedula, destino).

### Ejemplo

~~~
[(“Manuel Suarez”, 19823451, “Liverpool”), (“Silvana Paredes”, 22709128, “Buenos Aires”), (“Rosa Ortiz”, 15123978, “Glasgow”), (“Luciana Hernández”, 38981374, “Lisboa”)]
~~~

Además, en otra lista de tuplas, se almacenan los datos de cada ciudad y el país al que pertenece.

~~~
[(“Buenos Aires”, “Argentina”), (“Glasgow”, “Escocia”), (“Lisboa”, “Portugal”),
(“Liverpool”, “Inglaterra”), (“Madrid”, “España”)].
~~~

Hacer un menú iterativo que permita al usuario realizar las siguientes
operaciones:
- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de ciudades.
- Dado el DNI (cédula) de un pasajero, ver a que ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dado el DNI (cédula) de un pasajero, ver a que país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a esa ciudad.
- Salir del programa.
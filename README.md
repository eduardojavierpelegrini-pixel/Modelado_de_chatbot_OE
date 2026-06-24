#TPI-Organizacion Empresarial

#Modelado de chatbot para la asignación de turnos médicos

#Tecnicatura Universitaria en Programacion a Distancia-UTN

---

##Integrantes
.Eduardo Pelegrini

---

#Descripcion del proyecto
Este proyecto presenta el diseño,arquitectura y funcionamiento
de un chatbot destinado a la asignacion de turnos medicos a través 
de Wathsapp.
#Objetivo del proyecto
Desarrollar un modelo conceptual y técnico de un chatbot
que permita:

Validar el DNI del paciente
Mostrar especialidades disponibles
Ofrecer turnos según disponibilidad
Confirmar la reserva
Registrar el turno en una base simulada

El trabajo se centra en la estrategia de la automatización
a fin de ponderar la eficiencia para la relacion servicio/usuario
centradose en la arquitectura y el flujo de funcionamiento.

-----------------------

#Arquitectura del sistema 
El sistema se compone de tres módulos principales:

1.Interfaz conversacional-Whatsapp Business API
Permite que el usuario interactúe mediante mensajes.
Es la capa visible del sistema.
2.Lógica del chatbot-Python
Implementada mediante una máquina de estados que controla:
. Inicio
. Validación de DNI
. Seleccion de especialidad
. Oferta de turnos 
. Confirmacion 
. Cierre
---------
#Base de datos simulada
Representada mediante un archivo .CSV ubidacdo en /datos/turnos.csv
Contiene:
.DNI
.Especialidad
.Día
.Hora
.Disponibilidad
---------
#Flujo conversacional
1.Estado 0-inicio
El bot saluda y da la bienvenida
2. Estado 1-Validación del DNI
verifica si el DNI existe en la base simulada.
Si no existe, solicita reingreso.
3.Estado 2-Seleccion de especialidad
Muestra un menú y el usuario elige una opcion
4. Estado 3-Oferta de turnos
el boot consulta el archivo turnos.csv y muestra los turnos disponibles
5.Estado 4-Confirmación
El usuario confirma el turno.
El sistema registra la elección
5.Estado 5-Cierre
El boot agradece y finaliza la conversacion
---------
#Estructura del repositorio
El proyecto se encuentra organizado en distintas carpetas
para separar correctamente los datos, el código y los resulltados
.datos/
Contiene el archivo CSV utilizado para el diccionario de datos simulado
y los turnos
scripts/
Contiene el script principal desarrollado en Python
resultados/
Carpeta donde se guardan las capturas, los diagramas, informes
README.md
Archivo de documentación general del proyecto
.gitignore
Archivo utilizado para evitar subir archivos innecesarios
en el repositorio
#Tecnologias utilizadas
Python(lógica del bot)
Whatsapp Business API(interfaz convencional)
CSV como base de datos simulada
Github para control de versiones y documentación
#Ejemplo de interacción
Bot: Bienvenido al sistema de turnos. Ingrese su DNI.
Usuario: 12345678
Bot: DNI válido. Seleccione especialidad:

Clínica Médica

Odontología

Pediatría
Usuario: 1
Bot: Turnos disponibles:

Lunes 10:00

Martes 14:00
Seleccione uno.
Usuario: Lunes 10:00
Bot: Turno confirmado. ¡Gracias por utilizar el sistema!



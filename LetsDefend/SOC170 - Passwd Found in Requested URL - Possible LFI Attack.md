<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Audiowide&size=42&duration=3000&pause=1000&color=0DD41E&center=true&vCenter=true&width=1000&height=80&lines=SOC170+Passwd+Found+in+Requested+URL" />
</p>

---

# Recopilar datos

Reúna algo de información que pueda obtenerse rápidamente para comprender mejor el tráfico. Esto puede resumirse de la siguiente manera.

![Descripción de la imagen](./capturas/captura0054.png)

El tráfico proviene de fuera (Internet).

![Descripción de la imagen](./capturas/captura0055.png)

**Reputación de la dirección IP:** Según Cisco Talos y Virustotal, la IP es neutral.

Buscando información en el Log Management, encontramos un solo registro relacionado a esta IP.

![Descripción de la imagen](./capturas/captura0056.png)

Analizando la URL solicitada, encontramos que intento inyectar un payload en el parámetro file.

![Descripción de la imagen](./capturas/captura0057.png)

No hay registros que indiquen que hubo pruebas de penetración contra este servidor.

![Descripción de la imagen](./capturas/captura0058.png)

Si vemos la respuesta, podemos observar que hubo un error de servidor, el ataque no fue exitoso. No hay necesidad de escalar al SOC nivel 2.

**VEREDICTO:** `VERDADERO POSITIVO`

# Conclusión

Desde la página de Log Management, se debe realizar el filtrado según la dirección IP de origen y se debe llegar a la solicitud relevante. 
Cuando examinamos los detalles de la solicitud, se ve que el código de estado es 500 y el tamaño de la respuesta es 0. Por esta razón, el ataque no tuvo éxito. No hay necesidad de contener el dispositivo ni escalar el incidente al siguiente nivel.

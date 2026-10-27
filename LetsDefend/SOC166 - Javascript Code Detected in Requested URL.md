<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Audiowide&size=48&duration=3000&pause=1000&color=0DD41E&center=true&vCenter=true&width=1000&height=80&lines=SOC166+JS+Code+Detected+in+URL" />
</p>

---

# Recopilar datos

![Descripción de la imagen](./capturas/captura0029.png)

Reúna algo de información que pueda obtenerse rápidamente para comprender mejor el tráfico. Esto puede resumirse de la siguiente manera.

El tráfico proviene de una IP pública, así que viene de afuera.

![Descripción de la imagen](./capturas/captura0030.png)

**Propiedad de la dirección IP:** El registro indica Asia Pacific Network Information Centre (APNIC), una organización que administra y distribuye recursos de direcciones IP en la región de Asia-Pacífico.

![Descripción de la imagen](./capturas/captura0031.png)

**Reputación de la dirección IP:** Según Cisco Talos esta IP tiene una reputación mala.

# Examinar el tráfico HTTP

Verifique el contenido del tráfico en busca de cualquier condición sospechosa, como payloads de ataques web (Inyección SQL, XSS, Inyección de Comandos, IDOR, RFI/LFI). Encontramos 8 registros.

![Descripción de la imagen](./capturas/captura0032.png)

Examine todos los campos en la Solicitud HTTP. Dado que los atacantes no solo atacan a través de la URL, todos los datos de la fuente deben ser examinados para comprender si realmente existe un ciberataque.

![Descripción de la imagen](./capturas/captura0033.png)

![Descripción de la imagen](./capturas/captura0034.png)

Encontramos payloads de javascript incrustados.

En la búsqueda de emails de pruebas de penetración agendadas, no se encontró nada relacionado al objetivo analizado.

![Descripción de la imagen](./capturas/captura0035.png)

Tampoco se encontró el uso de comandos maliciosos.

No es necesario escalar el caso al SOC level 2.

**VEREDICTO:** `VERDADERO POSITIVO`

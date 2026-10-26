<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Audiowide&size=46&duration=3000&pause=1000&color=0DD41E&center=true&vCenter=true&width=1000&height=80&lines=SOC114+Malicious+Attachment+Detected" />
</p>

---

# Analizar correo electrónico

Antes de comenzar el análisis, se debe obtener información sobre el correo electrónico entrante.

![Descripción de la imagen](./capturas/captura0016.png)

### ¿Cuándo se envió?

**Respuesta:** `2021-01-31 07:48:30`

### ¿Cuál es la dirección SMTP del correo electrónico?

**Respuesta:** `49.234.43.39`

### ¿Cuál es la dirección del remitente?

**Respuesta:** `accounting@cmail.carleton.ca`

### ¿Cuál es la dirección del destinatario?

**Respuesta:** `richard@letsdefend.io`

### ¿Es sospechoso el contenido del correo?

**Respuesta:** `Es la supuesta factura de una compra.`

### ¿Hay archivos adjuntos o URLs en el correo electrónico?

**Respuesta:** `Si, un archivo de excel.`

---

# Analizar URL/Archivo adjunto

![Descripción de la imagen](./capturas/captura0017.png)

Según VirusTotal estamos ante un archivo malicioso.

# Verificar si el correo fue entregado al usuario

![Descripción de la imagen](./capturas/captura0018.png)

El correo si fue entregado al usuario.

# Verificar si alguien abrió el archivo/URL malicioso

![Descripción de la imagen](./capturas/captura0019.png)

Buscando una conexión con la IP 5.135.143.133, encontramos un dispositivo que si tuvo conexión.

![Descripción de la imagen](./capturas/captura0020.png)

Debemos contener este host.

![Descripción de la imagen](./capturas/captura0021.png)

**VEREDICTO:** `VERDADERO POSITIVO`

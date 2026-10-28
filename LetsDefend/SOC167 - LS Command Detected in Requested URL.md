<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Audiowide&size=50&duration=3000&pause=1000&color=0DD41E&center=true&vCenter=true&width=1000&height=80&lines=SOC167+LS+Command+Detected" />
</p>

---

# Recopilar datos

Reúna algo de información que pueda obtenerse rápidamente para comprender mejor el tráfico. Esto puede resumirse de la siguiente manera.

![Descripción de la imagen](./capturas/captura0043.png)

El tráfico proviene de la red de la empresa.

![Descripción de la imagen](./capturas/captura0044.png)

**Nombre del host del dispositivo:** `EliotPRD`

**Quién es el propietario del dispositivo (nombre de usuario):** `eliot`

**Hora del último inicio de sesión del usuario:** `2022-02-26 16:00:01`

En el Log Management encontramos 7 registros que tienen que ver con la interacción que estamos analizando.

![Descripción de la imagen](./capturas/captura0045.png)

Encontramos búsquedas normales.

![Descripción de la imagen](./capturas/captura0046.png)

# Conclusión
Cuando se examina la URL de la Solicitud, se ve que la palabra "skills" se busca en la página del Blog de LetsDefend. Sin embargo, las letras "ls" al final de la palabra hicieron que la regla se activara incorrectamente. 
Es una alarma de falso positivo. Para estar seguro, cuando se examina el Historial del Navegador del dispositivo desde la página de Endpoint Security, se confirma que no hay ataque.

**VEREDICTO:** `FALSO POSITIVO`

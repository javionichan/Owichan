# Owichan
 Open Wireless Security Assessment Methodology

# 🛡️ Owichan - Herramientas OWISAM para Auditoría Wi-Fi

Owichan es un conjunto de herramientas diseñadas para evaluar la seguridad de redes inalámbricas, basadas en la metodología **OWISAM** (Open Wireless Security Assessment Methodology). Este proyecto busca facilitar auditorías Wi-Fi mediante la automatización de controles y pruebas de seguridad, ayudando a identificar vulnerabilidades en infraestructuras inalámbricas.

## 📌 Objetivos del Proyecto

- Desarrollar herramientas prácticas para evaluar redes Wi-Fi según los estándares OWISAM.
- Facilitar auditorías de seguridad inalámbrica mediante scripts y utilidades especializadas.
- Crear reportes detallados de vulnerabilidades detectadas en redes Wi-Fi.
- Educar sobre mejores prácticas en ciberseguridad para redes inalámbricas.

## 🚨 Principales Vulnerabilidades Detectadas

El proyecto Owichan está diseñado para analizar y detectar las siguientes vulnerabilidades de seguridad en redes inalámbricas:

1. **Red de comunicaciones Wi-Fi abierta.**  
   - Riesgo: Permite el acceso sin autenticación, exponiendo la red a ataques MITM y robo de datos.  
   - 🔗 [Fuente](https://www.tarlogic.com/) | 🔗 [Fuente](https://www.dragonjar.org/) | 🔗 [Fuente](https://www.crowe.com/)  

2. **Uso de cifrado WEP en redes de comunicaciones.**  
   - Riesgo: WEP es un cifrado obsoleto y fácilmente vulnerable a ataques de cracking.  
   - 🔗 [Fuente](https://www.tarlogic.com/) | 🔗 [Fuente](https://www.inprosec.com/) | 🔗 [Fuente](https://www.dragonjar.org/)  

3. **Algoritmos inseguros de generación de claves en dispositivos (contraseñas y WPS).**  
   - Riesgo: Contraseñas predecibles o vulnerables facilitan ataques de fuerza bruta.  
   - 🔗 [Fuente](https://www.dragonjar.org/) | 🔗 [Fuente](https://www.tarlogic.com/) | 🔗 [Fuente](https://www.crowe.com/)  

4. **Claves WEP/WPA/WPA2 basadas en diccionarios.**  
   - Riesgo: Uso de contraseñas débiles que pueden ser descifradas con ataques de diccionario.  
   - 🔗 [Fuente](https://www.crowe.com/) | 🔗 [Fuente](https://www.dragonjar.org/) | 🔗 [Fuente](https://www.tarlogic.com/)  

5. **Mecanismos de autenticación inseguros (como LEAP, PEAP-MD5).**  
   - Riesgo: Estos protocolos pueden ser explotados para capturar credenciales.  
   - 🔗 [Fuente](https://www.dragonjar.org/) | 🔗 [Fuente](https://www.crowe.com/) | 🔗 [Fuente](https://www.tarlogic.com/)  

6. **Dispositivos con soporte activo de Wi-Fi Protected Setup PIN (WPS).**  
   - Riesgo: WPS PIN es altamente vulnerable a ataques de fuerza bruta.  
   - 🔗 [Fuente](https://www.crowe.com/) | 🔗 [Fuente](https://www.tarlogic.com/) | 🔗 [Fuente](https://www.dragonjar.org/)  

7. **Redes Wi-Fi no autorizadas por la organización.**  
   - Riesgo: Redes clandestinas pueden representar un punto de acceso no controlado.  
   - 🔗 [Fuente](https://www.ctxdetectives.com/) | 🔗 [Fuente](https://www.dragonjar.org/) | 🔗 [Fuente](https://www.crowe.com/)  

8. **Portales hotspot inseguros.**  
   - Riesgo: Hotspots sin cifrado pueden ser interceptados fácilmente.  
   - 🔗 [Fuente](https://www.tarlogic.com/) | 🔗 [Fuente](https://www.crowe.com/) | 🔗 [Fuente](https://www.dragonjar.org/)  

9. **Clientes intentando conectar a redes inseguras.**  
   - Riesgo: Dispositivos conectándose a redes sospechosas pueden ser atacados.  
   - 🔗 [Fuente](https://www.crowe.com/) | 🔗 [Fuente](https://www.dragonjar.org/) | 🔗 [Fuente](https://www.tarlogic.com/)  

10. **Cobertura de la red demasiado extensa.**  
    - Riesgo: Un alcance excesivo puede permitir el acceso no autorizado desde fuera de la organización.  
    - 🔗 [Fuente](https://www.tarlogic.com/) | 🔗 [Fuente](https://www.crowe.com/) | 🔗 [Fuente](https://www.dragonjar.org/)  

## 🛠️ Tecnologías Utilizadas

- **Python / Bash** para scripts de auditoría.
- **Wireshark / Tshark** para captura y análisis de tráfico.
- **Aircrack-ng** para pruebas de penetración en redes Wi-Fi.
- **Scapy** para manipulación de paquetes de red.
- **Metasploit / Bettercap** para pruebas avanzadas.

## 🔍 Metodología de Evaluación

El análisis de redes se realiza siguiendo las directrices de OWISAM, cubriendo:
- **Análisis de cobertura de señal Wi-Fi.**
- **Pruebas de autenticación y cifrado.**
- **Evaluación de puntos de acceso no autorizados.**
- **Auditoría de dispositivos cliente en la red.**
- **Pruebas de seguridad en portales de acceso público.**

## 📜 Licencia

Este proyecto está distribuido bajo la **GPL v3**, lo que significa que es de código abierto y cualquier modificación debe mantenerse en la misma licencia.

## 🚀 Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar con el proyecto Owichan:
1. Haz un **fork** del repositorio.
2. Crea una **rama** con tu funcionalidad.
3. Envía un **pull request** para revisión.

## 📞 Contacto

Si tienes preguntas, sugerencias o quieres colaborar, puedes encontrarnos en:

- [🔗 DragonJar](https://www.dragonjar.org/)
- [🔗 Tarlogic Security](https://www.tarlogic.com/)
- [🔗 Crowe Ciberseguridad](https://www.crowe.com/)

¡Gracias por apoyar Owichan! 🛡️🔥

# Instrucciones OWISAM-TR-007-009: WiGuard Auditoría de Seguridad Wi-Fi y DNS

Para instalar la tarjeta de red, primero debemos comprobar que nuestro equipo principal no la detecte , para ello debemos irnos a administrador de dispositivos >
adaptadores red , buscar nuestro adaptador de red y desactivarlo.

![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/dispositivos.png)


Una vez desactivado nos vamos a nuestra maquina kali, donde deberemos de activar el usb3.0 e añadir el adaptador de red, luego debemos reactivar 
el adaptador de red y ya detectaria la red.

![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/usb.png)

Ahora se deben descargar los drivers:

``git clone https://github.com/Khatcode/AWUS036ACH-Automated-Driver-Install``

``sudo chmod +x AlfaSetup.sh``

``./AlfaSetup.sh``
![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/git.PNG)

Una vez descargados los drivers, podremos ver que tenemos una nueva interfaz de red llamada Wlan0.

![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/wlan0.PNG)

Descargamos hostapd para configurar la red.

`` sudo apt-get install hostapd `` 

Creamos el fichero de configuración de /etc/hostapd/hostapd.conf con la siguiente información:

![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/hostapd.PNG)

Comprobamos que el nuevo servicio esté activo, de no estarlo, lo activaremos.

``sudo systemctl unmask hostapd``

``sudo systemctl status hostapd``
![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/servicio.PNG)

`` sudo systemctl start hostapd``

`` sudo hostapd /etc/hostapd/hostapd.conf``
![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/servicio2.PNG)

Ahora debemos descargar las siguientes librerias para poder asignarle una IP a nuestra tarjeta de red.

``sudo apt install build-essential libelf-dev dkms``

``sudo ip addr add 192.168.1.1/24 dev wlan0``
![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/ip.PNG)


## **Características para que el script.py funcione**

Para que el script.py funcione debemos hacer lo siguiente:

Para instalar python debemos de usar el comando: ``sudo apt install python3 -y``
![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/python3.png)

Para crear el script y pegar su contenido dentro de el usamos el comando ``sudo nano nombredelarchivo.py`` y pegamos dentro el script, nosotros recomendamos que descargues el script.py desde el repositorio de github.
![](https://github.com/CarlosBasulto/Owichan/blob/main/OWISAM-TR-007-009-Mario-Zayas-Mario-Moreno/imagenes/archivo.png)

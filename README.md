# Script para extraccion de datos en inversor Solis
Este repositorio contiene el servicio que se encarga de extraer los datos desde un inversor marca Solis para enviarlo mediante una peticion POST a un servidor backend.

## Comenzando 🚀
Este servicio se puede ejecutar en cualquier dispositivo que tenga conexion WiFi, se va a describir las instrucciones para ejecutarlo en raspbian (raspberry pi 3)

### Pre-requisitos 📋
* Python 3.7 en adelante
* Libreria requests, pint

### Instalación 🔧
Se debe descargar el codigo en una carpeta independiente
```
git clone https://github.com/MatthewTroya/SolisTest.git
```
Posteriormente se debe editar los siguientes parametros en el codigo
* PORT - puerto de escucha para la conexion TCP
* SERVER_IP - direccion IP del backend al cual se le realiza una peticion POST

### Despliegue 📦
Una vez que ya tengamos descargado el repositorio, se ejecuta el servicio 
```
python3.7 server.py
```
## Adicional 🛠️
Para que el script se ejecute en como un servicio daemon se debe realizar los pasos que se describen en la siguiente guia
[Medium](https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267)
Los comandos para revisar el estado del servicio y revisar el output del programa son
```
sudo systemctl status --nameservice
```
```
journalctl -f -u --nameservice
```
## Referencia ✒️
Este proyecto fue desarrollado utilizando como guia el siguiente repositorio [Planet Marshall](https://github.com/planetmarshall/solis-service.git)

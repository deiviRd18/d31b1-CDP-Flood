# 💀 D31B1 - CDP Flood Tool (DoS)

**Herramienta de prueba de estrés para dispositivos Cisco (CDP Table Exhaustion).**

Este script implementa un ataque de Denegación de Servicio (DoS) saturando la tabla de vecinos del protocolo CDP (Cisco Discovery Protocol). A diferencia de otras herramientas, utiliza **Raw Sockets** para inyectar paquetes directamente desde el kernel, logrando una velocidad de ataque masiva capaz de agotar la memoria y CPU del objetivo en segundos.

> **⚠️ Disclaimer:** Herramienta desarrollada con fines estrictamente académicos para la asignatura de Seguridad Informática. El autor no se hace responsable del uso en redes no autorizadas.

## 📋 Características Técnicas
* **Motor High-Speed:** Uso de `AF_PACKET` (Raw Sockets) para bypass de la pila de red tradicional, permitiendo >50,000 pps.
* **Payload Dinámico:** Generación aleatoria de miles de identidades falsas (Ej. `D31B1_Ghost_XXXX`) para llenar la memoria RAM del dispositivo.
* **Objetivo:** Dispositivos Cisco con CDP habilitado (Routers, Switches).

## ⚙️ Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/deiviRd18/d31b1-CDP-Flood.git](https://github.com/deiviRd18/D31B1-CDP-Flood.git)
   cd D31B1-CDP-Flood
---

## Instalar dependencias: Se requiere Python 3 y la librería Scapy.

`
pip3 install scapy`

## 🚀 Uso (Usage)
Todas las herramientas requieren privilegios de root (sudo) debido al uso de sockets crudos y manipulación de red.

## Ejecutar CDP Flood:

`
sudo python3 d31b1_cdp_flood.py`


Author: Junior (D31B1)

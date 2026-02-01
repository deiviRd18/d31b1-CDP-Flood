# ⚔️ d31b1-Pentest-Suite

**Custom Python Pentesting Suite for Network Security Assessments.**

Este repositorio contiene una colección de herramientas ofensivas desarrolladas en Python para auditoría de redes, pruebas de estrés (Stress Testing) y análisis de protocolos.

> **⚠️ Disclaimer:** Herramientas creadas con fines estrictamente educativos y de investigación académica. El autor no se hace responsable del mal uso.

## 🧰 Herramientas Incluidas (Tools)

### 1. 💀 CDP Flood (Raw Socket Edition)
* **Objetivo:** Denegación de Servicio (DoS) en dispositivos Cisco.
* **Técnica:** Utiliza **Raw Sockets** para inyección de paquetes a alta velocidad (>50k pps), saturando la tabla de vecinos CDP y agotando la CPU/RAM del objetivo.
* **Estado:** `Stable`

### 2. 🕵️‍♂️ ARP Spoofing (MitM)
* **Objetivo:** Interceptación de tráfico (Man-in-the-Middle).
* **Técnica:** Envenenamiento de tablas ARP (ARP Poisoning) con IP Forwarding automático para mantener la conectividad de la víctima.
* **Estado:** `Stable`

---

## ⚙️ Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/deiviRd18/d31b1-Pentest-Suite.git](https://github.com/deiviRd18/d31b1-Pentest-Suite.git)
   cd d31b1-Pentest-Suite

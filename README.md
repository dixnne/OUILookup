# OUILookup - Tarea 2

Integrantes del equipo:

- Diana Paola Narváez Martínez: dianapa.narvaez@gmail.com
- Diego Ruan Padilla: ruan.padilla.diego@gmail.com
- Bruno Guerra Uteau: guerrauteaub@gmail.com

## Instalación

Clona el repositorio en terminal mediante los siguientes comandos:

```bash
git clone https://github.com/dixnne/OUILookup.git
cd OUILookup
chmod +x OUILookup.py
```

## Uso

```bash
python3 OUILookup.py [-a,-m {aa:bb:cc...}]
```

## Diagrama de flujo de la solución

flowchart TD
%% Nodes
    A("Inicio")
    B("Importar librerías (getopt, sys, requests)")
    C("Hacer parse de los argumentos")
    D("¿Se dieron argumentos?")
    E("Termina la ejecución")
    F("Opciones de verificación")
    G("--mac options")
    H("--arp options")
    I("Hacer el API Request")
    J("Muestra la tabla ARP")
    K("Muestra el resultado o el mensaje de error")
    L("Muestra mensaje de ayuda")

%% Edge connections between nodes
    A --> B --> C --> D 
    D -- No --> E
    D -- Si --> F -- Si --> G --> I --> K
    F -- No --> H --> J --> L

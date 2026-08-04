# WORKSTATION INICIALIZADOR DE TRABAJO

Este aplicativo sirve para inicializar mi entorno de trabajo como VPN, Bria, Escritorio Remoto y marcar mi asistencia 
de forma automatica.

# Realizado por
- Eduardo Orjeda figueroa 

# Versión
* 1.0.0


# Dependencias instaladas
- python 3.11
- PyautoGUI


# Para capturar las posiciones de la pantalla

```python
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
```

# Coordenadas de cada aplicativo a capturar

## CiscoAnyConnect
## Bria
## Escritorio Remoto
## ECC LOGER
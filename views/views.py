import time

from model.navOpera import Opera
from model.CiscoAnyConnect import CiscoAnyConnect
from model.briaRemote import BriaRemote


class WorkstationInitializer:

    def __init__(self, pyautogui):
        self.pyautogui = pyautogui

        self.opera = Opera(pyautogui)
        self.cisco = CiscoAnyConnect(pyautogui)
        self.bria_remote = BriaRemote(pyautogui)

    def iniciar(self):

        print("======================================")
        print(" WORKSTATION INITIALIZER SECURITY")
        print("======================================")

        try:
            print("[1/5] Iniciando Navegador Opera...")
            self.opera.ejecutarOpera()
            time.sleep(2)

            print("[2/5] Registrando asistencia...")
            # Aquí puedes agregar la lógica adicional
            time.sleep(2)

            print("[3/5] Iniciando Cisco AnyConnect VPN...")
            self.cisco.ejecutarCisco()
            time.sleep(2)

            print("[4/5] Iniciando Bria Enterprise...")
            self.bria_remote.ejecutarBria()
            time.sleep(2)

            print("[5/5] Conectando Escritorio Remoto...")
            self.bria_remote.ejecutarEscritorioRemoto()




            print("\n✔ Proceso completado correctamente.")

        except Exception as e:
            print(f"\n✘ Error en inicializar: {e}")
import time

from model.CiscoAnyConnect import CiscoAnyConnect
from model.workstation import WorkInitializer


class WorkstationInitializer:

    def __init__(self, pyautogui):
        self.pyautogui = pyautogui

        self.cisco = CiscoAnyConnect(pyautogui)
        self.work = WorkInitializer(pyautogui)

    def iniciar(self):

        print("======================================")
        print(" WORKSTATION INITIALIZER SECURITY")
        print("======================================")
        print("Creador por: Eduardo Orjeda Figueroa")
        print("version: 1.0.0")

        try:

            print("[1/4] Iniciando Cisco AnyConnect VPN...")
            self.cisco.ejecutarCisco()
            time.sleep(2)

            print("[2/4] Iniciando Bria Enterprise...")
            self.work.ejecutarBria()
            time.sleep(2)

            print("[3/4] Conectando Escritorio Remoto...")
            self.work.ejecutarEscritorioRemoto()

            print("[3/4] Iniciando ECC Loger...")
            self.work.ejecutarEccloger()

            print("\n✔ Proceso completado correctamente.")

        except Exception as e:
            print(f"\n✘ Error en inicializar: {e}")
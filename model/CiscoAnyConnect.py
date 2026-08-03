#Creación de una clase para Cisco AnyConnect


class CiscoAnyConnect:
    def __init__(self, pyautogui):
        self.pyautogui = pyautogui

    def ejecutarCisco(self):
        #Mostrar iconos ocultos
        self.pyautogui.moveTo(1121, 749, 1)
        self.pyautogui.click()

        #Ejecutar Cisco AnyConnect
        self.pyautogui.moveTo(1082, 627, 1)
        self.pyautogui.click()

        #Ejecutar connect
        self.pyautogui.moveTo(1279, 639, 1)
        self.pyautogui.click()

        #Ingresar contraseña
        self.pyautogui.moveTo(744, 600, 6)
        self.pyautogui.click()
        self.pyautogui.write('#P330666.TTo1344606.#', interval=0.25)
        #Presionar enter
        self.pyautogui.press('enter')
        #Pulsa Aceptar
        self.pyautogui.moveTo(705, 465, 12)
        self.pyautogui.click()
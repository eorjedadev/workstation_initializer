#Creación de la clase para el navegador Opera
class Opera:
    def __init__(self, pyautogui):
        self.pyautogui = pyautogui

    def ejecutarOpera(self):
        #Ingresar al navegador Opera
        #teclas de acceso rapido
        self.pyautogui.hotkey('win', 'r')

        # Escribirá lo que le estoy pidiendo
        self.pyautogui.write('opera.exe', interval=0.25)
        self.pyautogui.press('enter')

        # Ingresar al Reloj GPS
        self.pyautogui.moveTo(670, 95, 2)
        self.pyautogui.click()

        # Ingresar usuario y contraseña
        self.pyautogui.moveTo(670, 525, 3)
        self.pyautogui.click()

        #self.pyautogui.moveTo(224, 67, 1)

        # Minimizar ventana de opera
        self.pyautogui.hotkey('win', 'd')
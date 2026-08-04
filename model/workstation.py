# Se realiza la clase para el bria y escritorio remoto

class WorkInitializer:
    def __init__(self, pyautogui):
        self.pyautogui = pyautogui

    def ejecutarBria(self):
        # Ejecutar Bria
        self.pyautogui.moveTo(432, 147, 5)
        self.pyautogui.click(clicks=2)

    def ejecutarEscritorioRemoto(self):
        # Ejecutar Escritorio remoto
        self.pyautogui.moveTo(336, 149, 7)
        self.pyautogui.click(clicks=2)
        # Ejecutar Portapapel
        self.pyautogui.moveTo(490, 402, 2)
        self.pyautogui.click()
        # Ejecutar Conectar
        self.pyautogui.moveTo(815, 550, 1)
        self.pyautogui.click()

    def ejecutarEccloger(self):
        # Ejecutar Ingresar usuario
        self.pyautogui.moveTo(600, 345, 60)
        self.pyautogui.click()
        self.pyautogui.write('47981033', interval=0.25)
        # Ejecutar Ingresar contraseña
        self.pyautogui.moveTo(900, 36, 5)
        self.pyautogui.click()
        self.pyautogui.write('*A0108#h1732Sab+', interval=0.25)
        self.pyautogui.press('enter')
        self.pyautogui.press('enter')
        # Iniciar sesión workdesktop
        self.pyautogui.moveTo(221, 746, 3)
        self.pyautogui.click()
        # minimizar ventana de escritorio remoto
        self.pyautogui.moveTo(885, 9, 2)
        self.pyautogui.click()
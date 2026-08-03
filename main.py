import pyautogui

from views.views import WorkstationInitializer


def main():

    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 1

    app = WorkstationInitializer(pyautogui)
    app.iniciar()


if __name__ == "__main__":
    main()
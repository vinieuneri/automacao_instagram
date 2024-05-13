import webbrowser
import pyautogui
from time import sleep

def acessando_pagina():
    pyautogui.move(300,350, duration=2)
    pyautogui.click()
    sleep(2)
def logout():
    pyautogui.click(118,623,duration=2)
    pyautogui.click(1098,164,duration=2)
    pyautogui.click(708,576,duration=2)


paginas = ['nike', 'adidas','disney']

webbrowser.open('https://www.instagram.com')

#Entrando campo usuario
sleep(5)
campo_usuario = pyautogui.locateCenterOnScreen('campo_usuario.png')
pyautogui.click(campo_usuario[0], campo_usuario[1], duration=1)
sleep(1)
pyautogui.typewrite('email@gmail.com')

sleep(1)
pyautogui.hotkey('tab')

sleep(2)
pyautogui.typewrite('*********')

sleep(0.5)
pyautogui.move(0,80, duration=1)
pyautogui.click()

sleep(5)
notificacao_1 = pyautogui.locateCenterOnScreen('notificacao_1.png')
pyautogui.click(notificacao_1[0], notificacao_1[1], duration=1)

for pagina in paginas:
    sleep(5)
    #instagram = pyautogui.locateCenterOnScreen('pesquisa.png')
    #pyautogui.moveTo(instagram[0], instagram[1], duration=1)
    #pyautogui.move(0, 110, duration=1)
    sleep(2)
    pyautogui.click(115,282,duration=2)


    sleep(2)
    pyautogui.typewrite(pagina)
    pyautogui.move(80,-30, duration=3)
    pyautogui.click()
    acessando_pagina()
    sleep(10)

    comentario = pyautogui.locateCenterOnScreen('add_comen.png')
    pyautogui.moveTo(comentario[0],comentario[1],duration=2)
    pyautogui.click()
    #pyautogui.typewrite('Legal!')
    pyautogui.hotkey('enter')
    pyautogui.click(1355,351,duration=2)
logout()

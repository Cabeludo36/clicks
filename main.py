import pyautogui as pg # para controlar mause e teclado
import time # tempo
import pyperclip as pc # para copiar e colar
import keyboard # para receber input
from webbrowser import open_new #para abrir a aba no browser
from pathlib import Path #para var se a o arquivo exixte
from time import sleep

funcao = input('Que função quer usar: ')
tempo = float(input('Coloque o tempo que quer entre ações: '))
while True:
    #pega link
    if Path(f'setings{funcao}.txt').is_file():
        f = open(f'setings{funcao}.txt', 'r') 
    else:
        time.sleep(5)
        pg.alert('Você precisa colocar as configurações.\n\nPara confirmar posicões aperte ctrl + q\n\nPara colocar uma menssagem aperte ctrl + m\n\nPara usar o "scroll" para baixo aperte ctrl + alt\n\nQuando terminar aperte ctrl + l')
        f = open(f'setings{funcao}.txt', 'a')
        while True:
            if(keyboard.is_pressed('ctrl') and keyboard.is_pressed('q')):
                xy = pg.position()
                f.write(f'({xy[0]}, {xy[1]})\n')
                time.sleep(1)
            if(keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt')):
                xy = pg.position()
                f.write(f'scroll\n')
                time.sleep(1)
            if(keyboard.is_pressed('ctrl') and keyboard.is_pressed('m')):
                xy = pg.position()
                men = input("Coloque o texto que quer escrever:")
                f.write(f'({xy[0]}, {xy[1]})\nmenssagem:{men}\n')
                time.sleep(1)
            if(keyboard.is_pressed('ctrl') and keyboard.is_pressed('l')):
                f.close()
                f = open(f'setings{funcao}.txt', 'r')
                break
    time.sleep(5)
    for x in f:
        if(x[0]=="("):
            time.sleep(tempo)
            s = x[1:-2]
            xy = s.split(', ')
            pg.click(int(xy[0]), int(xy[1]))
        elif(x[:6]=="scroll"):
            time.sleep(tempo)
            pg.scroll(-100)
        elif(x[:10]=="menssagem:"):
            time.sleep(tempo)
            pc.copy(x[10:])
            pg.hotkey('ctrl', 'v')
    f.close()
    if(input("Quer continuar?[s/n]").lower() == "n"):
        break

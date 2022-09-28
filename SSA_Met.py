#Developer: https://github.com/VegaCenturion
#Special thanks : https://github.com/Ala-R-F
#               : https://github.com/annapss
#               : https://github.com/LuisHTVRS
#=========================================(//||^Progranadores^||\\)============================================

#print("rodando")                            	# Checa se o programa foi iniciado
#browser = webdriver.Firefox()               	# Recebe drives do nevegador a ser usado || recomenda-se Firefox por ser mais leve
#print("Peguei o Navegador")		    	    # Teste
#browser.get('http://172.16.8.79/monitora')  	# Abre a janela na qual será alvo da captura
#print("Abri a URl")				            # Teste
#print("carregando programa")                	# Teste de carregamento da página
#sleep(5)                                    	# Espera para carregamento das informações da Estação
#while True:                                	# Condição de automação para Screenshot
#print("funcionando")                    	    # Teste
#browser.save_screenshot('Teste.png')        	# Timer para o espaçamento das capturas
#print("A mimir")                            	# Finaliza o progama

#=========================================(//||^Função_Primitiva^||\\)=========================================

#'C:\Users\comet\Downloads\ScreeshotMet\Versao ESP_32_1'

#===========================================(//||^Path_Arquivo^||\\)===========================================
import tkinter
from tkinter import filedialog
import os 
from PySimpleGUI import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep
from threading import Thread

#=====================================(//||^Imports utilizados^||\\)=========================================

winOpen = True
state = False
timeSet = 30
url = 'http://172.16.8.151/monitora'
arqNome = 'Est3_padrao.png'
path = r'C:\temp'
#("C:\\Users\\Aluno\\Desktop\\Guilherme_3binfo\\Python\\Teste.png", "C:\\temp\\Teste.png")

#=====================================(//||^Variaveis globais^||\\)=========================================
def search_for_file_path ():
    root = tkinter.Tk()
    root.withdraw()
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Selecione a pasta Desejada')
    return tempdir

def Rodando():                              #Função de Screenshot do programa
    global winOpen, timeSet, state
    browser = webdriver.Firefox()           # Recebe drives do nevegador a ser usado || recomenda-se Firefox por ser mais leve
    browser.get(url)                        # Abre a janela na qual será alvo da captura
    browser.set_window_position(0, 0)
    browser.set_window_size(476, 719)
    sleep(5)                                # tempo para carregar a pagina
    while True:
        browser.save_screenshot(f"{path}/{arqNome}")        # salva a screenshot
        state = True
        timeSet = int(timeSet)
        sleep(timeSet)                          # Timer para o espaçamento das captura


def window():                               # Inteface grafica do programa
    sg.theme('LightGray1')
    global winOpen

    layout = [[sg.Text('Tempo entre capturas (Segundos):'),sg.Text(size=(15,1),key='-OUTPUT1-')], 
                [sg.Input(key='-IN1-',default_text='30'),sg.Button('Definir Segundos',button_color=('purple')),],
                [sg.Text('URL completa do alvo para a captura: [https://www."site".com]: '), sg.Text(size=(40,1), key='-OUTPUT2-')], 
                [sg.Input(key='-IN2-', default_text='http://172.16.8.151/monitora'), sg.Button('Definir URL',button_color=('purple'))],
                [sg.Text('Nome do Arquivo[.png]: '), sg.Text(size=(40,1),key='-OUTPUT3-')], 
                [sg.Input(key='-IN_ARQ-', default_text='Est3_padrao.png'), sg.Button('Definir Nome',button_color=('purple'))],
                [sg.Text('Caminho da pasta:'), sg.Button('Mudar pasta')],
                [sg.Text(size=(50,1), key='-OUT_PATH-')],
                [sg.Button('Iniciar Programa', button_color=('purple')), sg.Text(size=(15,1), key='-STATE-')]]


    window = sg.Window('SSA_Est_Met', layout)

    try:
        while True: 
            global url, timeSet, winOpen, state, browser, arqNome, path
            event, values, = window.read(timeout=500)        # returns every 500 ms
            print(event, values) 
            if event in (None, 'Sair'): 
                state = False
                winOpen = False
                browser.close()
                window.close
                break

            if event == 'Definir Segundos': 
                window['-OUTPUT1-'].update(values['-IN1-']) 
                timeSet = (values['-IN1-'])

            if event == 'Definir URL': 
                window['-OUTPUT2-'].update(values['-IN2-']) 
                url = (values['-IN2-'])

            if event == 'Definir Nome': 
                window['-OUTPUT3-'].update(values['-IN_ARQ-']) 
                arqNome = (values['-IN_ARQ-'])

            if event == 'Mudar pasta':
                path = search_for_file_path()
                window['-OUT_PATH-'].update(path)

            if event == 'Iniciar Programa':
                if state == False:
                    state = True
                    window['-STATE-'].update('Ligado')
                    winOpen = True
                    while(state == True):
                        Rodando()
                else:
                    state = False
                    window['-STATE-'].update('Desligado')  
                    browser.close()               

    except:
        winOpen = False            #pop-up de erro
        sg.popup_error(f'ERRO. Tente novamente.')
        window.close()

#======================================(//||^Botões da Interface^||\\)======================================
Thread(target = window).start()
window.daemon = True 
window.run()
window.join()


#======================================(//||^Thread dos programas^||\\)======================================
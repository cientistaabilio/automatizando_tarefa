pip install pyautogui
import pyautogui
import pyperclip
import time  

pyautogui.PAUSE = 1 #tempo de pausa entre comandos

# 1ª passo: Acessar o google drive através do link

pyautogui.hotkey("ctrl", "t")#combinar teclas
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")#suporta caracteres especiais
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

time.sleep(5) # esperar carregar totalmente a página

pyautogui.click(x=434, y=384, clicks=2)

# 2ª Passo: Navegar até o local do relatório(entrar na pasta exportar)
time.sleep(2) # novamente aguardar a tela de loading

pyautogui.click(x=455, y=469)
pyautogui.click(x=721, y=273)
pyautogui.click(x=741, y=356)
time.sleep(5) # Tempo para garantir que deu tempo de fazer o download, caso precise aumente.



# Observações 
#Achando a sua posição para mandar o click - no meu caso eu usei o google colab pois achei prático para ficar pegando o valor.
time.sleep(5) # Isso faz o código aguardar 5 segundos, assim vc pode mover o mouse até a janela/aba e deixar o ponteiro parado para saber a posição
pyautogui.position()#Ele irá retornar o x e y da posição do mouse e assim basta copiar e substituir o x e y da linha 19

#Abaixo seria o código sem o caracter especial ?, no caso do google ele coloca esse simbolo, porem o pyautogui não reconhece simbolos, apeans informação extra.
#pyautogui.write("https://docs.google.com/spreadsheets/d/1nsHbr-DpinKM_XL1qPnh76aSh3aOs3K2/edit#gid=1634402548")# não suportar caracter especial

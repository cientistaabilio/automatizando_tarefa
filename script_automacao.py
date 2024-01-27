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

# 2ª Passo: Navegar até o local do relatório(entrar na pasta exportar)
pyautogui.click(x=434, y=384, clicks=2)
time.sleep(2) # novamente aguardar a tela de loading

# 3ª Passo:  Fazer o download do relatório
pyautogui.click(x=455, y=469)
pyautogui.click(x=721, y=273)
pyautogui.click(x=741, y=356)
time.sleep(5) # Tempo para garantir que deu tempo de fazer o download, caso precise aumente.

# 4ª Passo: Calcular os indicadores

# 5ª Passo: Entrar no email



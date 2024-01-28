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
import pandas as pd

# o r antes do endereço garante que o python irá executar independente se for com / ou \.
tabela = pd.read_excel(r"C://Users/Abilio/Downloads/Vendas - Dez.xlsx")
display(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# 5ª Passo: Entrar no email

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# Passo 6: Enviar por e-mail o resultado
pyautogui.click(x=113, y=208)
time.sleep(3)
pyautogui.write("email@gmail.com")#coloque aqui o email de destino, para onde será selecionado
pyautogui.press("tab") # seleciona o email

pyautogui.press("tab") # pula pro campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v") # escrever o assunto
pyautogui.press("tab") #pular pro corpo do email

#abaixo a mensagem que irá aparecer no corpo do texto
texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Abilio"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar

# apertar Ctrl Enter
pyautogui.hotkey("ctrl", "enter")



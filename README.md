# automatizando_tarefa
Código para executar programas de forma automático, no caso acessar um arquivo do google drive

# Observações 
### Achando a sua posição para mandar o click - no meu caso eu usei o google colab pois achei prático para ficar pegando o valor.
```py
time.sleep(5) # Isso faz o código aguardar 5 segundos, assim vc pode mover o mouse até a janela/aba e deixar o ponteiro parado para saber a posição
pyautogui.position()#Ele irá retornar o x e y da posição do mouse e assim basta copiar e substituir o x e y da linha 19
```

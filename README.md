# Automação de Sistemas e Processos com Python

### Desafio:

Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior

E-mail da diretoria: seugmail+diretoria@gmail.com<br>
Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

Comandos pyautogui: https://pyautogui.readthedocs.io/en/latest/quickstart.html

# Observações 
### Achando a sua posição para mandar o click - no meu caso eu usei o google colab pois achei prático para ficar pegando o valor.
```py
time.sleep(5) # Isso faz o código aguardar 5 segundos, assim vc pode mover o mouse até a janela/aba e deixar o ponteiro parado para saber a posição
pyautogui.position()#Ele irá retornar o x e y da posição do mouse e assim basta copiar e substituir o x e y da linha 19
```

```py
# caso precise selecionar a aba sem ser a primeira
# o r antes do endereço garante que o python irá executar independente se for com / ou \.
tabela = pd.read_excel(r"C://Users/Abilio/Downloads/Vendas - Dez.xlsx", sheets=2)

````
Esse código é baseado no canal do youtube.
[HashTag Treinamentos](https://www.youtube.com/@HashtagTreinamentos)

Pode haver alguma modificações e o objetivo do código é o autoconhecimento.

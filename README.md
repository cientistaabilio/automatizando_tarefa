# Automação de Sistemas e Processos com Python

### Desafio:

Rotineiramente, o sistema atualiza as vendas do dia anterior, e como analista, sua tarefa diária é enviar um e-mail à diretoria assim que iniciar o trabalho, contendo o faturamento e a quantidade de produtos vendidos no dia anterior.

E-mail da diretoria: seugmail+diretoria@gmail.com<br>
Local dos Dados de Vendas: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

Para automatizar esse processo, utilizaremos o pyautogui, uma biblioteca de automação de comandos do mouse e teclado.

[Documentação do PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/quickstart.html)

# Observações 
### Encontrando a posição para clicar - Exemplo no Google Colab
```py
time.sleep(5) # Aguarde 5 segundos para posicionar o mouse
pyautogui.position()# Retorna as coordenadas x e y, substitua na linha 19
```
### Selecionando uma aba específica em caso de múltiplas abas no Excel
```py
# o r antes do endereço garante que o python irá executar independente se for com / ou \.
# Use se precisar selecionar uma aba específica (sheets=2 indica a terceira aba, por exemplo)
tabela = pd.read_excel(r"C://Users/Abilio/Downloads/Vendas - Dez.xlsx", sheets=2)

````
Este código foi inspirado no canal do YouTube 
[HashTag Treinamentos](https://www.youtube.com/@HashtagTreinamentos)

Pode sofrer modificações e seu propósito é o autoconhecimento.

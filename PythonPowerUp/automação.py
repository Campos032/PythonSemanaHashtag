# Passo a passo do projeto
import time

# pip install pyautogui para instalar a biblioteca que usaremos no projeto
import pyautogui as pygui

# clicar > pyautogui.click
# escrever > pyautogui.write
# apertar > pyautgui.press
# apertar/atalho > pyautogui.hotkey(ctrl + v)
# Exemplo - pygui.press('win')
# scoll (rolar) > pyautogui.scroll(1000) número negativo rola para baixo e positivo para cima

# Passo 1 - Entrar no sistema da empresa # https://dlp.hashtagtreinamentos.com/python/intensivao/login
pygui.PAUSE = 0.3  # A cada comando terá uma pausa de 1 segundohttps://dlp.hashtagtreinamentos.com/python/intensivao/login
# aperta a tecla do windows
pygui.press('win')
# digita o nome do programa
pygui.write('edge')
# aperta enter
pygui.press('enter')
# escrever o link na barra de pesquisa e dar enter
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pygui.write(link)
# apertar enter
pygui.press('enter')
# espera 5 segundos
time.sleep(2)

# Passo 2 - Fazer Login
# clicar no espaço do email
pygui.click(x=583, y=356)
# escrever email
pygui.write('pythonimpressionador@gmail.com')
# clicar no espaço da senha
pygui.press('tab')  # tab pula para o próximo campo
# escrever a senha
pygui.write('minha senha')
# apertar no login
pygui.click(x=632, y=509)
time.sleep(2)

# Passo 3 - Importar um produto
# pip install pandas numpy openpyxl
import pandas

# ler a base de dados
tabela = pandas.read_csv('produtos.csv')

# Passo 4 - Cadastrar um produto
for linha in tabela.index:
    # clicar no espaço código do produto
    pygui.click(x=549, y=239)
    # código
    codigo = tabela.loc[linha, 'codigo']
    pygui.write(codigo)
    pygui.press('tab')
    # marca
    pygui.write(tabela.loc[linha, 'marca'])
    pygui.press('tab')
    # tipo
    pygui.write(tabela.loc[linha, 'tipo'])
    pygui.press('tab')
    # categoria
    pygui.write(str(tabela.loc[linha, 'categoria']))
    pygui.press('tab')
    # preço
    pygui.write(str(tabela.loc[linha, 'preco_unitario']))
    pygui.press('tab')
    # custo do produto
    pygui.write(str(tabela.loc[linha, 'custo']))
    pygui.press('tab')
    # obs
    obs = str(tabela.loc[linha, 'custo'])
    if not pandas.isna(obs):
        pygui.write(obs)
    pygui.press('tab')
    # cadastrar produto
    pygui.press('enter')
    # voltar para o início da página
    pygui.scroll(5000)

# Passo 5 - Repetir isso até acabar a base de dados

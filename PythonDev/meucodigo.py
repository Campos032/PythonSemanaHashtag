# FrontEnd -> Usuário vê
# BackEnd -> Lógica por trás do site

# Frameworks - Usados para criar projetos
# Django, Flask, Flet

# Será usado o framework flet - o flet permite que com o mesmo código seja criado sites, appsdesktop e appsmobile

# Anotar o que terá no site
# Título HashZap
# Botão de iniciar o chat
#       PopUp
#       - Bem-Vindo ao Hashzap
#       - Escreva seu nome
#       - Entrar no chat
# Chat
#     - Lira entrou no chat
#     - Mensagens do usuário
# Campo para enviar a mensagem 
# Botão de enviar 

import flet as ft


def main(pagina):
    titulo = ft.Text('HashZap')
    pagina.add(titulo)  # Adiciona algo na página
   
    def iniciarchat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        # Adiciona qual será o popup da página, no flet os popups são chamados dialog
        # Quando o usuário chamar a função iniciarchat clicando no botão, o parâmetro open tornará True e o popup abrirá
        # Atualiza a página com as novas informações, sempre deve ter um update dentro de cada função

    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciarchat)
    # ElevatedButton é um botão estilizado com o texto e o que fazer ao ser acionado
    pagina.add(botao_iniciar)

    def entrarchat(evento):  # Toda função associada ao click de um botão, tem que receber um evento como parâmetro
        # Feche o popup
        popup.open = False
        # Tire o botão iniciarchat
        pagina.remove(botao_iniciar)
        # Criar o campo do chat
        pagina.add(chat)
        # Criar o campo enviar mensagem
        linha_mensagem = ft.Row(
            [chatfield, botao_enviar_mensagem]
            )  # Row cria uma linha, e nós adicionamos as informações nessa linha 
        pagina.add(linha_mensagem)
        
        # Botão de enviar mensagem
        texto = f"{nome_usuario.value} entrou no chat"
        # chat.controls.append(ft.Text(texto))  # Isso virou a linha debaixo 
        pagina.pubsub.send_all(texto)
        pagina.update()

    # TextField cria um campo de texto, e label é um rótulo de sugestão
    nome_usuario = ft.TextField(label='Escreva seu nome', on_submit=entrarchat)

    popup = ft.AlertDialog(open=False,
                           modal=True,
                           title=ft.Text('Bem-vindo ao HashZap'),
                           content=nome_usuario,
                           actions=[ft.ElevatedButton('Entrar', on_click=entrarchat)])

    # AlertDialog É a caixa que irá aparecer na tela do usuário quando for chamada a função x
    # Open=false diz que não será aberto ao iniciar o app
    # modal=True diz que a caixa de diálogo aparecerá no meio da tela
    # Title é o texto do popup
    # Content é a variável que terá dento do campo de texto
    # Actions é uma lista de ações(botões no popup)
    
    chat = ft.Column()  # Campo de texto onde aparece as mensagens que o usuário enviou e recebeu

    def enviar_mensagem_tunel(informacoes):  # Faz a comunicação entre os usuários
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    # Cria um tunel onde irá fazer com que todos no chat recebam as mensagens uns dos outros
    
    def enviar_mensagem(evento):
        # Colocar o nome do usuário na mensagem 
        texto_campo_mensagem = f"{nome_usuario.value}: {chatfield.value}"
        # chat.controls.append(ft.Text(texto_campo_mensagem)) # foi para a função enviar_mensagem_tunel
        pagina.pubsub.send_all(texto_campo_mensagem)  # Define a mensagem que será enviada no túnel
        
        # Limpar o campo mensagem
        chatfield.value = '' 
        pagina.update()

    # Campo de texto onde o usuário escreve a mensagem
    chatfield = ft.TextField(label='Escreva sua mensagem', on_submit=enviar_mensagem)

    # Botão que envia a mensagem do usuário
    botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)


# ft.app(main)  # Formato de app
ft.app(main, view=ft.WEB_BROWSER)  # Formato de site

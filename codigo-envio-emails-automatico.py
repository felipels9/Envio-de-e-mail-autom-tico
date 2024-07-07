import smtplib
from email.message import EmailMessage
import os


def enviar_email():
    # Corpo do e-mail com formatação HTML e CSS
    corpo_email = """
    <html>
        <head>
            <style>
                body {font-family: Arial, sans-serif;}
            </style>
        </head>

        <body>
            <p>Prezados,</p> 
            <p>Venho por meio deste e-mail...<br>A presença de todos...</p>
            <p>At.te,<br>felipels9</p>
        </body>
    </html>
    """

    # Criação do objeto EmailMessage
    msg = EmailMessage()
    msg['Subject'] = 'Reunião Extraordinária'  # Título do e-mail
    msg['From'] = 'felipels9...@gmail.com'  # E-mail do remetente
    msg['To'] = 'l...@gmail.com, ...@hotmail.com, ....@edu.br'  # E-mails dos destinatários
    password = 'Inclua sua senha de app aqui'  # Substitua pela senha de app gerada
    msg.add_header('Content-Type', 'text/html')
    msg.set_content(corpo_email, subtype='html')

    # Adicionando anexos
    arquivos = [
        r'C:\Users\lf\OneDrive\Área de Trabalho\documento-teste-pdf.pdf',
        r'C:\Users\lf\OneDrive\Área de Trabalho\documento-teste-word.docx',
        r'C:\Users\lf\OneDrive\Área de Trabalho\arquivo-teste-exel.xlsx'
    ]
    for arquivo in arquivos:
        try:
            with open(arquivo, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(arquivo)
                msg.add_attachment(file_data, maintype='application', subtype=os.path.splitext(arquivo)[1][1:],
                                   filename=file_name)
        except Exception as e:
            print(f"Erro ao anexar o arquivo {arquivo}: {e}")

    # Enviando o e-mail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(msg['From'], password)
        server.send_message(msg)
        server.quit()
        print("Email enviado com sucesso")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")


# Chamando a função para enviar o e-mail
enviar_email()


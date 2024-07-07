O script Python permite enviar mensagens de e-mail e arquivos anexos durante a transmissão, basta apenas preencher as credenciais SMTP e os detalhes do e-mail para o envio.

É necessário que a conta de e-mail configurada permita o uso de aplicativos menos seguros, ou mesmo uma senha de app para serviços do Gmail, que foi o método utilizado neste exemplo.

Para usar o script de forma correta, basta editar as variáveis 'msg' ['Subject'] com o título de e-mail desejado, 'msg' ['From'] com o e-mail do remetente e 'msg' ['To'] com os endereços de e-mail dos destinatários no PyCharm. Além disso, substitua na variável 'password' a informação pela senha de app gerada.

Para adicionar arquivos anexos ao corpo do e-mail, será necessário copiar os respectivos caminhos dentro da variável 'arquivos'.

Desta forma, o script funcionará perfeitamente, permitindo ao remetente enviar e-mails de forma automática.

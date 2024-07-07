O script Python permite enviar mensagens de e-mail e arquivos anexos de forma segura durante a transmissão, basta apenas preencher as credenciais SMTP e os detalhes do e-mail para o envio.

É necessário que a conta de e-mail configurada permita o uso de aplicativos menos seguros, ou mesmo uma senha de app para serviços do Gmail, que foi o método utilizado neste exemplo.

Para usar o script de forma correta, basta editar as variáveis 'msg' ['From'] com o e-mail do remetente e 'msg' ['To'] com os endereços de e-mail dos destinatários no PyCharm. É necessário também, que a variável 'Inclua sua senha do aplicativo aqui' seja substituida pela senha de app gerada.

Para adicionar arquivos anexos ao corpo do e-mail, será necessário copiar os respectivos caminhos dentro da variável 'arquivos'.

Desta forma, o script funcionará perfeitamente, permitindo ao remetente enviar e-mails de forma automática e segura.

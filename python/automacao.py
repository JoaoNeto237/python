import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p> Tudo .</p>
    <p>aaaa </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Automacao de e-mail em python"
    msg['From'] = "kenedy.rodriguesdealmeida@gmail.com"
    msg['To'] = "vouvendercontas@gmail.com"
    password = "mipaldptclanfeai"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )


    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado!')
enviar_email()
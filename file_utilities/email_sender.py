import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jproperties import Properties

configs = Properties()

with open('config.properties', 'rb') as config_file:
    configs.load(config_file)

def send_email(subject, message, to_email, attachment_path=None):
    from_email = configs.get("from_email").data
    password = configs.get("password").data

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    body = MIMEText(message, "plain")
    msg.attach(body)

    if attachment_path:
        with open(attachment_path, "r") as attachment:
            attachment_content = attachment.read()
            attachment_part = MIMEText(attachment_content, "plain")
            msg.attach(attachment_part)

    try:
        server = smtplib.SMTP_SSL(configs.get("smtp_host").data, configs.get("smtp_port").data)  # Usar SMTP_SSL para SSL/TLS
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Correo electrónico enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")

import smtplib

def send_notification(msg):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('idpmeaslant@gmail.com', 'bonkersdonkers')
    mail.sendmail('idpmeaslant@gmail.com', 'Ykorringa@gmail.com', 'code: ' + msg)
    mail.close()


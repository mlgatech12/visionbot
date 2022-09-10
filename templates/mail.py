import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to) :
    print('hello')
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'caltechytes@gmail.com'
    password = 'qqutaqybvfhtfczz'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)

    server.quit()

if __name__ == '__main__':
    email_alert("Hey", "Hello World", "nidhivivek@gmail.com")





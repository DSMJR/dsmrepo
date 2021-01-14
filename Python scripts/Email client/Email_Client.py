
import smtplib, ssl
import easyimap
import os
login = False
def init(login):
    mode = ''
    if login == False:
        print('\n---Login---\n')
        my_email = input("Email: ")
        my_pass = input("Password: ")
        login = True


    try:
    	server_id = my_email.strip()
    	key = my_pass.strip()
    	connection = easyimap.connect('imap.gmail.com', server_id, key)
    	print('\n\n\nLogged in (' + server_id + ') Successful')
    except:
    	print('\n\n\nLog in failed')
    	login = False
    	init(login)

    mode = input('Send(1) or Receive(2): ')
    try:
        mode = int(mode)
    except:
        print('Please enter "1" or "2"')
        init(login)
    if mode == 1:
        print('Mode: "Send"')
        send(my_email, my_pass)
    if mode == 2:
        print('Mode: "Receive"')
        Recve(my_email, my_pass)
    else:
        print('Please enter "1" or "2"')
        init(login)


def Recve(my_email, my_pass):
    os.system('cls')
    server_id = my_email.strip()
    key = my_pass.strip()
    count = 0
    recount = 0
    connection = easyimap.connect('imap.gmail.com', server_id, key)
    for mail_id in connection.listids(limit=100):
        server_request = connection.mail(mail_id)
        print(server_request.title.strip())
        print(server_request.body.strip())
        
def send(my_email, my_pass):
    try:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"

        sender_email = my_email.strip()
        receiver_email = input("Email to? : ".strip())  # Enter receiver address
        password = my_pass.strip()

        Subject = input('Subject: ')
        Body = input('Body: ')

        message = "Subject: " + Subject + "\n\n" + Body
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print('\nsent!\n')
        redo(my_email, my_pass)
    except:
        print('ERROR')
        input('Press Enter to continue...')
        quit()

def redo(my_email, my_pass):
    mode = input('Send(1) or Receive(2): ')
    try:
        mode = int(mode)
    except:
        print('Please enter "1" or "2"')
        redo(my_email, my_pass)
    if mode == 1:
        print('Mode: "Send"')
        send(my_email, my_pass)
    if mode == 2:
        print('Mode: "Receive"')
        Recve(my_email, my_pass)
    else:
        print('Please enter "1" or "2"')
        redo(my_email, my_pass)
init(login)
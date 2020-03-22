import imapclient, pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl= True)

conn.login('email', 'password')

conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SINCE 20-Aug-2015'])

print(UIDs)

rawMessage = conn.fetch(['UID number goes here'], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage['UID number'][b'BODY[]'])

message.get_subject()

message.get_addresses('from') # See who the email is from

message.get_addresses('to') # See who the email was sent to

message.text_part.get_payload().decode('UTF-8') # Get the message as a string

conn.logout()

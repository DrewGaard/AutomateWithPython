import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

type(conn)

print(conn)

conn.ehlo()

conn.starttls()

conn.login('email', 'password')

conn.sendmail('from address', 'to address', 'Subject: subject\n\n Main body of the email')


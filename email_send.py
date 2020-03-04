from email.message import EmailMessage
from datetime import datetime
from getpass import getpass
from pathlib import Path
from random import randint
import time
import sys
import smtplib

#Inserting emails
try:
	account = sys.argv[1]
	towho = sys.argv[2]

except:
	print('Please try again. Make sure you have provided emails from and to who.')
else:
	if 'hotmail' in account:
		 inhost = 'smtp.live.com' 
		 inport=587
	elif 'gmail' in account:
		 inhost='smtp.gmail.com' 
		 inport=587
	elif 'yahoo' in account:
		 inhost='smtp.mail.yahoo.com'
		 inport=465
	else: 
		inhost=input('What is the smtp host for your mailbox? (Please follow the format: your.smtp.host.com)')
		inport=input('What is the smtp port for your mailbox?')

	passwd = getpass('password:')	#Inserting password(hidden)
	
	while True:
		#Chosing random number from 1 to 7.
		num = randint(1,7) 
		#Assigning current time to variable and chosing format.
		now = datetime.now()
		current_time = now.strftime('%H:%M:%S')
		if current_time == '09:30:00':
		
			email = EmailMessage()
			email['from'] = account
			email['to'] = towho				
			email['subject'] = ''
			#Chosing random text message form the folder and using it as a content in mail.
			random_image = Path(f'{num}.txt').read_text()
			email.set_content(random_image)
			#Assigning smtp server (here we've got hotmail) and port to 'smtp'
			try:	
				with smtplib.SMTP(host = inhost, port=inport) as smtp:
					#Identify yourself to an ESMTP server 
					smtp.ehlo()
					#Put the SMTP connection in TLS mode.
					smtp.starttls()
					#Loging to your account
					smtp.login(account, passwd)
					#Sending email with previously declareted values.
					smtp.send_message(email)
				print("Done")
			except:
			 	print('Issue while sending an email. Please, check provided emails or your password. Make sure you have internet connection.')
			 	break

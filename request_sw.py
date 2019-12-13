import smtplib
from email.mime.multipart import MIMEMultipart
import datetime
from datetime import date
import calendar 

today = date.today()
print("Today's date:", today)

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow_nr = str(tomorrow.day)

gds = {'Monday':'Lunedi','Tuesday':'Martedi','Wednesday':'Mercoledi','Thursday':'Giovedi','Friday':'Venerdi','Saturday':'Sabato','Sundey':'Domenica'}

me = "antonio.cantelli@cmcc.it"
#to = "silvio.gualdi@cmcc.it"
#cc = "loredana.amato@cmcc.it"

tod = tomorrow.hour
if tod >= 0 & tod < 12:
	form = "Buongiorno"
if tod >= 12 & tod < 18:
	form = "Buonpomeriggio"
if tod >= 18 & tod < 24:
	form = "Buonasera"

my_msg_body = str(form  + " Silvio,\r\n" 
						+ "per motivi di ottimizzazione dei tempi di lavoro che devo svolgere, chiederei il telelavoro per domani " 
						+ gds[calendar.day_name[tomorrow.weekday()]]+" "+tomorrow_nr+", "
						+ "dalla sede di Venezia. Approvi? \r\n"
						+ "\r\n"
						+ "Grazie,\r\n"
						+ "\r\n"    	
						+ "Antonio\r\n")

to  = me
cc  = me
bcc = me


rcpt = cc.split(",") + bcc.split(",") + [to]
msg = MIMEMultipart('alternative')
msg['Subject'] = "Richiesta telelavoro per "+gds[calendar.day_name[tomorrow.weekday()]]+" "+tomorrow_nr
msg['To'] = to
msg['Cc'] = cc
msg.attach(my_msg_body)
server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.login(me,'cmccbo1*')
server.sendmail(me, rcpt, msg.as_string())
server.quit()


server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login('myname@gmail.com','mypass')
server.sendmail('myname@gmail.com','somename@somewhere.com',msg)
server.close()
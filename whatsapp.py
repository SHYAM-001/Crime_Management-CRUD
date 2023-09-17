import pywhatkit
import datetime

current_time = datetime.datetime.now().strftime("%H:%M")
l=list(current_time.split(':'))
l1=int(l[0])
l2=int(l[1])+3
pywhatkit.sendwhatmsg("+919789043358","HELLO WORLD",l1,l2)






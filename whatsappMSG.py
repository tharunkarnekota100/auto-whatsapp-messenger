import pywhatkit

#when we are designing a app for school
#when we want to sent fee due message to parents by entering there mobile number
#it automatically sents the message

mobno = input('enter whatsapp mobile number: ')
msg = input('message: ')
hr = int(input('hours(24 hours format): '))
mint = int(input('minutes: '))
pywhatkit.sendwhatmsg('+91'+ mobno, msg, hr, mint)

#pywhatkit.sendwhatmsg('+916303542909', 'hello', 18, 7)

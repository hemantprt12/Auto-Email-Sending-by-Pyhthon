# Import SMTM
import smtplib as s
ob=s.SMTP("smtp.gmail.com", 587)    # creating Object

# Function started for encryption
ob.starttls()

ob.login('hemantprt12@gmail.com','Password')
subject= 'Information about Email'
body='''Electronic mail (email or e-mail) is a method of exchanging messages ("mail") between people using electronic devices.
Email entered limited use in the 1960s, but users could only send to users of the same computer, and some early email systems
required the author and the recipient to both be online simultaneously, similar to instant messaging. Ray Tomlinson is credited
as the inventor of email;in 1971, he developed the first system able to send mail between users on different hosts across the ARPANET,
using the @ sign to link the user name with a destination server. By the mid-1970s, this was the form recognized as email.
Email operates across computer networks, primarily the Internet. Today's email systems are based on a store-and-forward model.
Email servers accept, forward, deliver, and store messages. Neither the users nor their computers are required to be online
simultaneously; they need to connect, typically to a mail server or a webmail interface to send or receive messages or download it.
Originally an ASCII text-only communications medium, Internet email was extended by Multipurpose Internet Mail Extensions (MIME)
to carry text in other character sets and multimedia content attachments. International email, with internationalized email addresses
using UTF-8, is standardized but not widely adopted.The history of modern Internet email services reaches back to the early ARPANET,
with standards for encoding email messages published as early as 1973. An email message sent in the early 1970s is similar to a basic
email sent today.
Originally an ASCII text-only communications medium, Internet email was extended by Multipurpose Internet Mail Extensions (MIME) to
carry text in other character sets and multimedia content attachments. International email, with internationalized email addresses
using UTF-8, is standardized but not widely adopted.
The history of modern Internet email services reaches back to the early ARPANET, with standards for encoding email messages published
as early as 1973. An email message sent in the early 1970s is similar to a basic email sent today.'''

massage="Subject:{}\n\n{}".format(subject,body)
listofaddress=["hemant.parate@outlook.com"]
ob.sendmail('hemantprt12@gmail.com',listofaddress,massage)

print("Email has sent successfully...!")
ob.quit()

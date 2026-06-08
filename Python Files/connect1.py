# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 22:14:02 2021

@author: Ramya
"""


import smtplib as s

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def country(m,statename):
   
    ob= s.SMTP("smtp.gmail.com",587)

    ob.starttls()

    ob.login("infotech2k22@gmail.com","Infotech@2k22")
    
    body = '''Storm Prediction Dashboard details... Safe zone areas'''
    msg = MIMEMultipart()
    msg['Subject'] = 'Hi '+m+ ' ....Welcome!!'
    msg['From'] = "infotech2k22@gmail.com"
    msg['To'] = m
    msg.attach(MIMEText(body, 'plain'))

    
    pdfname = statename+' safe.pdf'
    
    binary_pdf = open(pdfname, 'rb')
 
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
   
# payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    
   # body = record 
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    msg.attach(payload)
 
 
  #  msg = "Subject:{}\n\n{}\n".format(subject,body)
    #print(msg)
    text = msg.as_string()
 
    ob.sendmail("infotech2k22@gmail.com",m,text)

    print("Sent Successfully")

    ob.quit()

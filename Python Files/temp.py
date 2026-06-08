import smtplib as s
 
def usermail(m):
    ob= s.SMTP("smtp.gmail.com",587)

    ob.starttls()

    ob.login("infotech2k22@gmail.com","Infotech@2k22")

    subject = "Msg from Ramya"
    body ="Our project mail is working cheers"

    msg = "Subject:{}\n\n{}{}\n".format(subject,body)
    #print(msg)

    ob.sendmail("infotech2k22@gmail.com",m,msg)

    print("Sent Successfully")

    ob.quit()

import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

  
server.login('devk.241202@gmail.com', "qfslxedjaeszwtya")

subject = "CHALLENGES COMPLETED"
body = " NAME: Akhilesh yadav \n Email: akhileshyaduvanshi9015@gmail.com \n Ph.No:6388552830 \nB.Tech IT \n 2nd year \n2100290130017 \n photo: https://drive.google.com/file/d/13j1eX-bBwnybnVVMIMJRWypK_IJNDnoc/view?usp=drivesdk \n Git : https://github.com/Akki9015/Cabin-4j/upload"
msg = f"subject: {subject} \n\n\n {body}"

server.sendmail(
        'devk.241202@gmail.com',
        'sales@cabin4j.com',
    msg
    )
print('Message is sent succesfully!')


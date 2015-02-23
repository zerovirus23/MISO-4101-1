# -*- coding: utf-8 -*- 
import smtplib 
from email.mime.text import MIMEText

import mimetypes

#from email.MIMEText import MIMEText
#from email.Encoders import encode_base64

 
class myCorreo:
    def enviarLocal(self):
        remitente = "Desde gnucita <jhonyt37@gmail.com>" 
        destinatario = "Mama de Gnucita <jhonyt37@gmail.com>" 
        asunto = "E-mal HTML enviado desde Python" 
        mensaje = """Hola!<br/> <br/> 
    	Este es un <b>e-mail</b> enviando desde <b>Python</b> 
        """	 
        email = """From: %s 
        To: %s 
        MIME-Version: 1.0 
        Content-type: text/html 
        Subject: %s 	 
        %s
        """ % (remitente, destinatario, asunto, mensaje) 
        try: 
            smtp = smtplib.SMTP('localhost') 
            smtp.sendmail(remitente, destinatario, email) 
            print ("Correo enviado" )
        except: 
            print ("""Error: el mensaje no pudo enviarse. 
            Compruebe que sendmail se encuentra instalado en su sistema""")

    def enviarGmail(self):
        
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        
        mailServer.ehlo()
        
        mailServer.starttls()
        
        mailServer.ehlo()
        
        mailServer.login("mysmarthome4101@gmail.com","zvjktuetqawucpqk")
        

        print (mailServer.ehlo())

        # Construimos el mensaje simple
        mensaje = MIMEText("""Correo electronico de pruebas
        Verificacion de envio exitosa. No contestar""")
        mensaje['From']="mysmarthome4101@gmail.com"
        mensaje['To']="jhonyt37@gmail.com"
        mensaje['Subject']="Correo de pruebas"

        # Envio del mensaje
        mailServer.sendmail("mysmarthome4101@gmail.com",
	                "jhonyt37@gmail.com",
                     mensaje.as_string())

        # Cierre de la conexion
        mailServer.close()

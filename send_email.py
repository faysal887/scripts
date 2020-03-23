import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 

def send_email(files, to_addr):
    """
    :to_addr = list of receiver(s) address
    :files = dictionary containing file name as key and contant as value for attachment. i.e. content can be dataframe to be sent as excel file
    """

    fromaddr = {your email address}
    pswd     = {your password}
    subject  = {email subject line}
    body     = {email body}

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ", ".join(addr)
    msg['Subject'] = subject
    body = body

    msg.attach(MIMEText(body, 'plain'))
    for name, file in files.items():
        file = open(name, "rb").read()
        part = MIMEBase('application', "octet-stream")
        part.set_payload(file)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={name}.xlsx')
        msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, pswd)
    text = msg.as_string()
    server.sendmail(fromaddr, addr, text)
    server.quit()    
    print("email sent successfully !")
    return True



















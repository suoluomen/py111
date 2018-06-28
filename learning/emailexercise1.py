from email.mime.text import MIMEText
#创建邮件
msg = MIMEText('hello, send by Python...this is my first email!', 'plain', 'utf-8')

# 输入Email地址和口令:
#邮箱  mail.yyyy.com  25 发邮件
#账号 
from_addr = '@yyyy.com'#input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = 'mail.yyyy.com' #input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
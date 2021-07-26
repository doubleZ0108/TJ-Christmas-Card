from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib
import csv
import time

def _format_addr_(s):
    name, addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

# 上传图片附件，pic_path为贺卡路径
def load_pic(msg,pic_path):
    f=open(pic_path,'rb')
    name=pic_path.split('\\')[-1]
    type=name.split('.')[-1]
    mime = MIMEBase('image', type, filename=name)

    mime.add_header('Content-Disposition', 'attachment', filename=name)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', str(0))

    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

# 编写邮件
# pic_path--待发送的贺卡路径； from_addr--发件邮箱；to_addr--收件邮箱
def write_email(pic_path,from_addr,to_addr):
    msg = MIMEMultipart()
    msg['From'] = _format_addr_('二十二点零六团队 <%s>' % from_addr)
    msg['To'] = to_addr
    msg['Subject'] = Header('【二十二点零六】圣诞快乐🎄', 'utf-8').encode()

    text=MIMEText(r"<html><head>"+
        r"<meta charset='UTF-8'><meta name='viewport' content='width=device-width initial-scale=1'>"+
        r"<title>README</title></head>"+
        r"<body>"+
        r'<p>“把袜子翻过来，里朝外，挂起来，整个世界都是你的礼物”<br></br>'+
        r"圣诞愿望是你天天开心 所有惊喜都会如期而至📦<br></br>"+
        r"你有一份礼物请接收🎁<br></br>"+
        r"然后 晚安好梦🌙<br></br><br></br>"+
        r"/* zzzzzzzzzzzzzzzz<br></br>"+
        r"同济大学软件学院<br></br>"+
        r"造梦工程师🌨<br></br></p>"+
        r'<p><br></br><img src="cid:0"></p>'+
        r"</body>"+
        r"</html>",'html','utf-8')
    load_pic(msg, pic_path)
    msg.attach(text)
    return msg


from_addr="Six_past_Twenty4@163.com" # 发件邮箱
password="" # 发件邮箱的psd
smtp_server="smtp.163.com" # 邮箱的smtp

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)







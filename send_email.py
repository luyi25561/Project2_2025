import smtplib
from email.message import EmailMessage

# 👇 这里必须改成你自己的
from_addr = "3264812538@qq.com"
from_pwd = "hnwpikeskvwxdbca"
to_addr = "3533438190@qq.com"

msg = EmailMessage()
msg.set_content("植物状态正常！")
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "🌱 植物湿度提醒"

try:
    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(from_addr, from_pwd)
    server.send_message(msg)
    print("邮件发送成功！")
    server.quit()
except Exception as e:
    print("发送失败：", e)

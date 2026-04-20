import RPi.GPIO as GPIO
import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

# 邮箱配置
FROM_EMAIL = "1794302485@qq.com"
FROM_PWD = "lxgzrskjolbtcefb"
TO_EMAIL = ["3533438190@qq.com","3264812538@qq.com"]

# GPIO设置
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# 发邮件函数
def send_email(status):
    msg = EmailMessage()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f"📅 {now}\n{status}"
    msg.set_content(body)
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = "🌱 植物浇水提醒"

    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(FROM_EMAIL, FROM_PWD)
    server.send_message(msg)
    server.quit()
    print("提醒邮件已发送")

# 单次检测
def check_soil():
    moisture = GPIO.input(channel)
    if moisture == 1:
        status = "土壤湿润 ✅ 无需浇水"
    else:
        status = "土壤干燥 ⚠️ 请立即浇水！"
    print(status)
    send_email(status)

# 主程序：每天测4次（每6小时一次）
if __name__ == "__main__":
    try:
        print("植物湿度监测已启动...")
        while True:
            check_soil()
            print("等待6小时后下次检测...\n")
            time.sleep(6 * 3600)  # 6小时
    except KeyboardInterrupt:
        GPIO.cleanup()

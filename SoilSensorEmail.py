import RPi.GPIO as GPIO
import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

# Email Configuration
FROM_EMAIL = "1794302485@qq.com"
FROM_PWD = "lxgzrskjolbtcefb"
TO_EMAIL = ["3533438190@qq.com","3264812538@qq.com"]

# GPIO Settings
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# Send Email
def send_email(status):
    msg = EmailMessage()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f"📅 {now}\n{status}"
    msg.set_content(body)
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = "🌱 Plant Watering Reminder"

    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(FROM_EMAIL, FROM_PWD)
    server.send_message(msg)
    server.quit()
    print("Reminder email sent")

# Single check
def check_soil():
    moisture = GPIO.input(channel)
    if moisture == 1:
        status = "Soil is moist ✅ No watering needed"
    else:
        status = "Soil is dry ⚠️ Please water the plant now!"
    print(status)
    send_email(status)

# Main program
if __name__ == "__main__":
    try:
        print("Plant soil moisture monitoring has been activated...")
        while True:
            check_soil()
            print("Next check in 4 hours...\n")
            time.sleep(4 * 3600)  # 4小时
    except KeyboardInterrupt:
        GPIO.cleanup()

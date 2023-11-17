import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."
msg["From"] = "<SendEMailAddress>"
msg["To"] = "<ReceiveEMailAddress>"

# 여러 명에게 메일을 보낼때...
# msg["To"] = "abc@gmail.com, def@gmail.com, fgh@gmail.com"

# 참조
msg["Cc"] = "aaa@gmail.com"

# 비밀참조
msg["Bcc"] = "aaa@gmail.com"

msg.set_content("테스트 본문입니다.")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # SMTP 서버와 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login("<EMailAddress>", "<Password>") # 로그인
    
    smtp.send_message(msg)
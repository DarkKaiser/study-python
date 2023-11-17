import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."
msg["From"] = "<SendEMailAddress>"
msg["To"] = "<ReceiveEMailAddress>"

msg.set_content("테스트 본문입니다.")

# 첨부파일 추가
with open("btn_brush.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # SMTP 서버와 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login("<EMailAddress>", "<Password>") # 로그인
    
    smtp.send_message(msg)
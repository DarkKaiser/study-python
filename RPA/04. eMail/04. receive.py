from imap_tools import MailBox

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login("<EMailAddress>", "<Password>", initial_folder="INBOX")

# 최신 메일부터 최대 1개의 메일을 받아온다.
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    print("참조자", msg.cc)
    print("비밀참조자", msg.bcc)
    print("날짜", msg.date)
    print("본문", msg.text)
    print("HTML 메시지", msg.html)
    
    # 첨부파일
    for attach in msg.attachments:
        print("첨부파일 이름", attach.filename)
        print("타입", attach.content_type)
        print("크기", attach.size)
        
        # 파일 다운로드
        with open("download_" + attach.filename, "wb") as f:
            f.write(attach.payload)
    
mailbox.logout()

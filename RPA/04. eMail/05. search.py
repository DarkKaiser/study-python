from imap_tools import MailBox

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login("<EMailAddress>", "<Password>", initial_folder="INBOX")
# mailbox.logout()

# 위의 코드와 똑같은 코드, logout()을 따로 하지 않아도 된다.
with MailBox("imap.gmail.com", 993).login("<EMailAddress>", "<Password>", initial_folder="INBOX") as mailbox:
    # 전체 메일 가져오기
    # for msg in mailbox.fetch():
    #     print(f"[{msg.from_}] {msg.subject}")
    
    # 읽지 않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'):
    #     print(f"[{msg.from_}] {msg.subject}")
    
    # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM abc@gmail.com)'):
    #     print(f"[{msg.from_}] {msg.subject}")
    
    # 어떤 글자를 포함하는 메일 가져오기(제목, 본문)
    # for msg in mailbox.fetch('(TEXT "test mail")'):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 어떤 글자를 포함하는 메일 가져오기(제목만)
    # for msg in mailbox.fetch('(SUBJECT "test mail")'):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 특정 날짜 이후의 메일 가져오기
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)'):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 특정 날짜에 온 메일 가져오기
    # for msg in mailbox.fetch('(ON 07-Nov-2020)'):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 2가지 이상의 조건을 모두 만족하는 메일 가져오기
    # for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "test mail")'):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 2가지 이상의 조건 중 하나라도 만족하는 메일 가져오기
    for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "test mail")'):
        print(f"[{msg.from_}] {msg.subject}")

import os
import time
import datetime

print(os.getcwd()) # 현재 작업 공간
os.chdir("RPA") # RPA로 작업 공간 이동
print(os.getcwd())
os.chdir("..") # 부모 폴더로 이동
print(os.getcwd())

# 파일 경로 만들기
print(os.path.join(os.getcwd(), "my_file.txt"))

# 파일 경로에서 폴더 정보 가져오기
print(os.path.dirname(r"C:\Solutions-GitHub\study-python\my_file.txt"))

# 파일 정보 가져오기
ctime = os.path.getctime("LICENSE") # 파일 생성 날짜
print(ctime)
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

mtime = os.path.getmtime("LICENSE") # 파일 수정 날짜
print(mtime)

atime = os.path.getatime("LICENSE") # 파일의 마지막 접근 날짜
print(atime)

size = os.path.getsize("LICENSE")
print(size)
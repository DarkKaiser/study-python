import os
import time
import datetime
import fnmatch
import shutil

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

# 파일 목록 가져오기
print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
print(os.listdir("RPA")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# 파일 목록 가져오기(하위 폴더 모두 포함)
result = os.walk("RPA") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
for root, dirs, files in result:
    print(root, dirs, files)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
pattern = "*.py"
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern):
            result.append(os.path.join(root, name))
print(result)

# 주어진 경로가 파일인지 폴더인지 확인
print(os.path.isdir("RPA"))
print(os.path.isfile("RPA"))

# 만약에 지정된 경로에 해당하는 파일/폴더가 없다면?
print(os.path.isfile("NoRPA"))

# 주어진 경로가 존재하는가?
if os.path.exists("RPA"):
    print("파일 또는 폴더가 존재합니다.")
else:
    print("파일 또는 폴더가 존재하지 않습니다.")

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt")

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준으로 폴더를 생성
# os.makedirs("new_folders/a/b/c") # 하위 폴더를 가지는 폴더를 생성

# 폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folder") # 폴더 안이 비었을때만 삭제 가능
# shutil.rmtree("new_folders") # 폴더 안이 비어있지 않아도 완전 삭제 가능

# 파일 복사하기
shutil.copy("run_btn.png", "test_folder") # 어떤 파일을 폴더 안으로 복사하기
shutil.copy("run_btn.png", "test_folder/copied_run_btn.png") # 어떤 파일을 폴더 안에 새로운 파일 이름으로 복사하기
shutil.copyfile("run_btn.png", "test_folder/copied_run_btn_2.png") # 어떤 파일을 폴더 안에 대상 파일 이름으로 복사하기(대상 파일에 폴더가 들어갈 수 없다)

shutil.copy2("run_btn.png", "test_folder")
shutil.copy2("run_btn.png", "test_folder/copied_run_btn.png")
# copy, copyfile : 메타정보 복사 X
# copy2 : 메타정보 복사 O

# 폴더 복사
shutil.copytree("test_folder", "test_folder2")

# 폴더 이동
shutil.move("test_folder", "test_folder2")

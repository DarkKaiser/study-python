from openpyxl import Workbook

wb = Workbook()         # 새 워크북 생성
ws = wb.active          # 현재 활성화된 시트 가져옴
ws.title = "변경시트1"   # 시트의 이름을 변경
wb.save("sample.xlsx")
wb.close()

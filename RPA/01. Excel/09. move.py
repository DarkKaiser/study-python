from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

# 선택된 범위의 데이터를 열 기준으로 오른쪽으로 1칸 이동
ws.move_range("B1:C11", rows=0, cols=1)

wb.close()

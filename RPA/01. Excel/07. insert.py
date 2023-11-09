from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

# 8번째 줄 위치에 빈 줄을 추가
ws.insert_rows(8)

# 8번째 줄 위치에 5줄을 추가
ws.insert_rows(8, 5)

# B번째 열 위치에 빈 열을 추가
ws.insert_cols(2)

# B번째 열 위치에 3열을 추가
ws.insert_cols(2, 3)

wb.close()

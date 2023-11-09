from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

# 8번째 줄 삭제
ws.delete_rows(8)

# 8번째 줄부터 3줄 삭제
ws.delete_rows(8, 3)

# 2번째 열(B) 삭제
ws.delete_cols(2)

# 2번째 열(B)부터 2열 삭제
ws.delete_cols(2, 2)

wb.close()

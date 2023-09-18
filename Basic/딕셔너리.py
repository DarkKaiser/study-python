product = {
    "제품" : "망고",
    "타입" : "건망고"
}

if "제품" in product:
    print(product["제품"])
else:
    print("제품 요소가 없습니다.")
    
if product.get("가격") != None:
    print(product["가격"])
else:
    print("가격 요소가 없습니다.")

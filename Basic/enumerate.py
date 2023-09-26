fruits = ['바나나', '사과', '망고']

for fruit in enumerate(fruits):
    print(f'{fruit[0]} {fruit[1]}')
    
print('---------------------')

for i, fruit in enumerate(fruits):
    print(f'{i} {fruit}')

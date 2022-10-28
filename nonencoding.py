# 讀取檔案
# split(x)切割x
# strip處理換行符號
# 現在Excel不需要encoding 'utf-8'也可開啟
# if os.path.isfile檢查檔案是否存在(作業系統模組)

import os # operating system
# 讀取檔案
products = []
if os.path.isfile('product.csv'):
    print('Yaeh 找到檔案了!')
    with open('product.csv', 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('找不到檔案')

# 讓使用者輸入新的商品
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = int(input('請輸入商品價格: '))
    products.append([name, price])
print(products)

# 印出所有的購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
with open('product.csv', 'w',) as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(str(p[0]) + ',' + str(p[1]) + '\n')
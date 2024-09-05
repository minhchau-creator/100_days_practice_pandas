import pandas as pd
import matplotlib.pyplot as plt

# Excelファイルを読み込む
df = pd.read_excel("C:/Users\minhc\Downloads\アセスメントテスト回答用ファイル.xlsx", sheet_name='商品の日別販売個数')

# 商品Aと商品Bのデータを取り出す
product_data = df[['商品Aの販売個数', '商品Bの販売個数']]

# 散布図を描画
plt.scatter(product_data['商品Aの販売個数'], product_data['商品Bの販売個数'])
plt.xlabel('Product A Sales Volume')
plt.ylabel('Product B Sales Volume')
plt.title('Relationship between Product A and Product B Sales')
plt.grid(True)
plt.show()
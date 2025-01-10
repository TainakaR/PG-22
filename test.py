import random as r
def random_greeting():
  arr = ('こんにちは','お疲れ様です','ごきげんよう')
  return r.choice(arr)

# メイン処理
name = '高専太郎'
print(f'{random_greeting()}、{name}さん')
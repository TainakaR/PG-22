import random as r
def random_greeting():
  arr = ('こんにちは','お疲れ様です','ごきげんよう')
  return r.choice(arr)

def morning_greeting():
  arr = ('おはよう','おっは','おはようございます')
  return r.choice(arr)
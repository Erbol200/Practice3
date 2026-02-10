balance,amount=map(int,input().split())
if amount>balance:
    print("Insufficient Funds")
else:
    print(balance-amount)    
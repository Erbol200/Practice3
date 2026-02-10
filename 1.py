n=input()
er=True

for c in n:
    if int(c)%2!=0:
        er=False

if(er):
    print("Valid")
else:
    print("Not valid")                    
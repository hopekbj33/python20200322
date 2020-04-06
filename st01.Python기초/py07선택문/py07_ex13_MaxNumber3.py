num1=int(input("첫 번째 수를 입력하세요"))
num2=int(input("두 번째 수를 입력하세요"))
num3=int(input("세 번째 수를 입력하세요"))
if num1>num2:
    print(num1)
    else:
        print(num2)
if num1>num3:
    print(num1)
    else:
        print(num3)
if num2>num3:
    print(num2)
    else:
        print(num3)

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

numlist=[x,y,z]
max(numlist)
print("가장 큰 수는", max(numlist), "입니다.")
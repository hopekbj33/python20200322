#500과 1000사이에 있는 홀수의 합계를 구하시오.
sum=0
for i in range(501, 1001, 2):
    sum=sum+i
print(sum)

#0과 100사이에 있는 7의 배수의 합계를 구하시오.
sum=0
for i in range(0,101,7):
    sum=sum+i
print(sum)
#정수 값을 입력받고 1부터 입력 받은 정수까지의 합계를 구하시오.
sum=int(input("숫자를 입력하세요."))
for i in range(1,sum,1):
    sum=sum+i
print(sum)
#시작값 입력
#끝값 입력
#증가값을 입력
#2~300까지 3씩 증가시킨 값의 합계 :15050

num1=int(input("시작값을 입력하세요."))
num2=int(input("끝값을 입력하세요."))
num3=int(input("증가값을 입력하세요."))
sum=0
for i in range(num1,num2+1,num3):
    sum=sum+i
print("%s에서 %s까지 %s씩 증가시킨 합계: %s" % (num1, num2, num3, sum))
# 2단의 구구단을 출력하는 프로그램을 만드시오
two=0
for i in range(1,10,1):
    two=two+i
    str = "2*%s=%2s" %(i, 2*i)
    print(str)
# 1부터 9까지 2단의 구구단을 출력하시오.
# range()함수를 사용한다.
dan=int(input("단을 입력하세요"))
start=0
for i in range(1,10,1):
    start=start+i
    str = "%s*%s=%2s" %(dan, i, dan*i)
    print(str)

dan=int(input("단을 입력하세요"))
start=0
for i in range(1,10,1):
    start=start+i
    str = "%s*%s=%2s" %(dan, i, dan*i)
    if i==9:
        print(str+".",end="")
    else:
        print(str+",", end="")
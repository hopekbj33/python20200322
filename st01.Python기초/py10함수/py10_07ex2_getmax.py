# 사용자 함수 만들기
# 두 개의 정수가 주어지면 두수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자. 

# 함수 정의
# x : 매개변수
# y : 매개변수

# 왜 main() 함수를 만들어 사용하는가?
# 프로그래밍에서 지향하는 방식은 전역변수를 사용하지 않는다 

# main 함수 호출 
"""
def main()
    x=int(input("첫 번째 수?"))
    y=int(input("두 번째 수?"))
    value=get_max(10,20)
    print(value)
main()
"""

def get_max(x,y):
    result=None
    try:
        if(x>y):
            result=x
        else:
            result=y
    except Exception as identifier:
        pass
    return result

#value=get_max(10)
x=input("첫 번째 수?")
x=int(x)

y=input("두 번째 수?")
y=int(y)

def main():
    x=input("첫 번째 수?")
    x=int(x)

    y=input("두 번째 수?")
    y=int(y)

    value=get_max(x,y)
    print(value)
main()





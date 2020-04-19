# 사용자 함수 만들기
# 정수를 입력받아서 제곱한 값을 반환하는 square() 함수를 만들어보자.
# 함수 정의, 함수이름, 매개변수, result=none, return result
# 함수호출 value= 함수명(인수)

x=int(input("숫자를 입력하세요"))
def square(x):
    result=None
    try:
        result=x*x
    except Exception as identifier:
        pass
    return result

value=square(x)
print(value)


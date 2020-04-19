
# 숫자가 아닌 것을 정수로 변환하려고 할 때

# 숫자가 아닌 것을 실수로 변환 할 때

# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환하려고 할 때

# IndexError
"""
입력값=input("숫자를 입력하세요")
정수값=int(입력값)
실수값=float(입력값)
"""

try:
    입력값=input("숫자를 입력하세요")
    정수값=int(입력값)
    실수값=float(입력값)
except Exception as i:
    pass
print("정상종료")
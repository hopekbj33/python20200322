
def add(x, y):
    result = None
    try:
        result = x+y
    except Exception as ex:
        pass
    return result

def minus(x, y):
    result = None
    try:
        result = x-y
    except Exception as ex:
        pass
    return result
def mul(x, y):
    result = None
    try:
        result = x*y
    except Exception as ex:
        pass
    return result
def div(x, y):
    result = None
    try:
        result = x%y
    except Exception as ex:
        pass
    return result

def my_input():
    result = None
    try:
        result = int(input("숫자를 입력하세요"))
    except Exception as ex:
        pass
    return result

def main():
    x = my_input()
    y = my_input()
    value1 = add(x,y)
    value2 = minus(x,y)
    value3 = mul(x,y)
    value4 = div(x,y)
    print(value1, value2,value3,value4)
    return

main()


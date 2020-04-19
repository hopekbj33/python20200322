def 마침표():
    result = None
    try:
        str1 = input("교열할 문장을 입력하세요") 
        if str1.find(".")>0 or str1.find("?")>0 or str1.find("!")>0:
            print(str1)
        else:
            print("마침표가 없습니다. 마침표를 넣어주세요.")
    except Exception as ex:
            pass
    return result

if __name__ == "__마침표__":
    pass

마침표()

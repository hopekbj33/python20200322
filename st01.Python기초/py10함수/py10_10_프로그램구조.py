# 데이터 수집
def readlist():
    result=None
    result=[]
    while True:
        result=int(input("성적을 입력하세요"))
        if (result<0):
            break
        else :
            result.append()
    return result

# 데이터 처리
def processlist(nlist)
    result=None
    result=sorted(nlist)
    return return

# 데이터 출력
def printlist(nlist):
    result=None
    for i in nlist:
        str="성적: %s" % i
        print(str)
    else:
        pass
    return result

# 프로그램 시작
def main():
    result=None
    result=readlist()
    result=processlist(result)
    result=printlist(result)
    return result
    
# 이 모듈이 단독으로 사용되면 main()를 호출하라.
if __name__ == "__main__":
    main()

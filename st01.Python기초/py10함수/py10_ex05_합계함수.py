# 데이터 수집
def readlist():
    result=None
    result=[]
    result=int(input("시작값을 입력하세요", "종료값을 입력하세요"))  
    return result

# 데이터 처리1
def processlist(nlist):
    result=None
    result=0
    result=sorted(nlist)
    return result

# 데이터 처리2
def sumlist(nlist):
    #result=None
    result=0
    for i in range(nlist[0], nlist[1],1):
        result = result+i
    return result

# 데이터 출력
def printlist(nlist): 
    result=None
    result="%s부터 %s까지의 합계는 %s입니다." % (nlist[0], nlist[1], nlist[2])
    print(result)
    return result

# 프로그램 시작
def main():
    result=None
    result=readlist()
    result=processlist(result)
    result=sumlist()
    result.append()
    result=printlist(result)
    return result
main()
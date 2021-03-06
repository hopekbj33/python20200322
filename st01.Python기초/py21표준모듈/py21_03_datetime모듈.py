#################################
# datetime 모듈의 사용법을 익힌다.
#
#datetime.now()	현재 년월일시분초 가져오기
#datetime.timedelta()	시간 가감로세스를 주어진 초만큼 정지
#datetime.replace()	시간 교체
#################################


# 모듈을 읽어 들입니다.


########################
# 현재 년,월,일,시,분,초 출력하기
# 2020-03-08 16:23:20.943650
# 예시)  년 2020
#        월 3
#        일 2
#        시 15
#        분 15
#        초 58

########################
# 시간 출력 방법
# 예시) 15:15:58

########################
# 시간 출력 방법
# 예시) 15시 15분 58초

########################
# 현재 시간이 오전/오후 인지를 출력하시오.
# 파이썬에서 오전/오후 구별하는 방법이 없다.
# 시간으로 오전/오후를 판별해야 한다. 
# hour가 12다 크면 오후 아니면 오전 ==> if ~ else 사용 
# 예시) 현재 시간은 15시로 오후입니다!


########################
# 계절을 확인합니다.
# 현재 날짜/시간을 구하고 월을 변수에 저장합니다.
# 조건문으로 계절을 확인합니다. now.month 를 이용하여 판별해야 하다.
# 예시) 현재는 봄입니다.


########################
# date 출력 함수 만들기. 예시) 2020-03-02 16:42:06


########################
# 특정 시간 구하기 : datetime.timedelta() 메서드
# datetime.timedelta()로 시간 더하기 >> 현재에 1주 1일 1시간 1분 1초를 더해서 출력하시오.
# 예시) 현재 2020-03-02 16:42:06
#       수정 2020-03-10 17:43:07


########################
# 도전. datetime.timedelta()로 시간 더하고 빼기 >> 오늘부터 100일 전 날짜를 출력하시오.


########################
# 특정 시간 요소 교체하기 : replace() 메서드
# datetime.replace()로 시간 더하기 >> 1년 1주 더하기
# 예시) 현재 2020-03-02 16:44:19
#       수정 2021-03-09 16:44:19

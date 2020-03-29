# 교열할 텍스트 입력 받기
# 문자열을 다루는 string 라이브러리를 불러 온다.

import string
import kss
# f = open(input("교열할 텍스트를 넣어주세요")
text = input("교열할 텍스트를 넣어주세요")
for paragraph in text:
    lines = string(paragraph, ".", "?", "!")
    for each_line in lines:
        if each_line(".", "?", "!") > 0:
            print(each_line)
        else:
            pass


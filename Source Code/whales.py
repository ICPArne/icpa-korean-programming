#whales.py
#메인 실행

from whales_make_code import *
from sys import exit


def kor_input():
    result = list()
    while True:
        text = input("> ")
        if text == '작성시작':
            while True:
                more_text = input()
                if more_text != '작성종료':
                    result.append(more_text)
                else:
                    break
            break
        elif text == '종료':
            exit()
        else:
            result.append(text)
            last_text = text.replace(' ', '')
            if last_text[len(last_text) - 1] == ':':
                while True:
                    more_text = input()
                    if more_text.replace(' ', '') != '':
                        result.append(more_text)
                    else:
                        break
                break
            else:
                break

    return '\n'.join(result)


if __name__ == "__main__":
    while True:
        try:
            exec(main(kor_input()))
        except NameError as name:
            print("이름 오류: 변수, 함수명을 확인하세요")
        except TypeError as value:
            print("자료형 오류: (연산, 함수에 쓰인) 자료형을 확인하세요")
        except RecursionError as recur:
            print("재귀 오류: 함수의 재귀가 무한정으로 일어나는지 확인하세요")
        except Exception as e:
            print('오류:', e.args)

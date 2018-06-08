# 최종 수정: 2018-06-08
# 수정자: 20307 박진철

def modify(text):
    text = text.replace('더하기', '+')
    text = text.replace('빼기', '-')
    text = text.replace('곱하기', '*')
    text = text.replace('나누기', '/')
    return text

#입력 형식: a (더하기|빼기|곱하기|나누기) b ... (띄어쓰기 상관X)
#         : a (+|-|*|/) b ...
def main():
    print("한글로 작성하는 계산기")
    while True:
        try:
            text = input("> ")
            if text.replace(' ', '') == '':
                print()
                continue
            text = modify(text)
            try:
                print(eval(text), end='\n\n')
            except ZeroDivisionError:
                print("0으로 나눌 수 없습니다.", end='\n\n')
        except:
            print("[오류] 다시 시도해주세요.", end='\n\n')
        
if __name__ == "__main__":
    main()


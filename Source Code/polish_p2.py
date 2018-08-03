#역폴란드 표기법
#중치 표기를 후치 표기로 변환
#최종 수정일: 2018-08-03

class Stack:                                             #메모리 구현을 위한 스택
    def __init__(self, size = 20):
        """클래스 Stack의 생성자"""
        self.size = size                                 #스택의 최대 크기
        self.count = 0                                   #현재 자료의 개수
        self.list = list()                               #자료가 담기는 곳(자료형 구분 X)

    def push(self, thing = None):
        """스택에 자료를 추가"""
        if len(self.list) + 1 > self.size:               #스택의 최대 크기를 초과할 경우: 스택 오버플로우
            raise Exception("스택 오버플로우")
            return
        self.count += 1                                  #자료의 개수 증가
        self.list.append(thing)                          #자료 추가

    def pop(self):
        """스택에서 자료를 제거 및 반환"""
        if self.count == 0:                              #아무 것도 들어있지 않은 스택에서 자료를 가져올 경우: 스택 언더플로우
            raise Exception("스택 언더플로우")
            return
        self.count -= 1                                  #자료의 개수 감소
        return self.list.pop()                           #자료 제거 및 반환

    def get_top(self):
        """스택의 최상단부 정보 획득"""
        if self.count == 0:                              #아무 것도 들어있지 않은 스택에서 자료를 가져올 경우: 스택 언더플로우
            raise Exception("스택 언더플로우")
            return
        return self.list[self.count - 1]                 #스택의 최상단부 정보 획득

def main():
    text = input("> ")
    result = polish(text)                                #역폴란드 표기법 실시
    if result == '':                                     #사용자가 정상적으로 입력한 식이 없을 경우
        print("유효한 식이 없습니다.")
        return

    print("변환:", result)
    return 0

def polish(txt):
    """역폴란드 표기법 실시"""
    global stack
    text = txt + '\0'
    result = list()                                      #변환된 식이 저장되는 곳
    for index in range(len(text)):                       #입력된 식에 대하여 한 글자씩 검사 및 추가
        word = text[index]

        if isspace(word):                                #공백을 건너뜀
            continue

        if word=='\0':                                   #행의 끝이면 괄호 검사 및 출력 진행
            while stack.count > 0:
                #스택의 나머지를 출력
                a = stack.pop()
                result.append(a)
                if result[len(result) - 1] == '(':       #사용자가 입력한 식의 맨 마지막에 괄호 '('가 있을 경우
                    raise Exception("괄호 ( 오류")        #적절하지 않은 식
                    return

        if islower(word) or isdigit(word):               #변수(영어 소문자) 혹은 정수일 경우 추가
            result.append(word)
            continue

        if word == '(':                                  #식에 괄호 (가 있을 경우 스택에 추가
            stack.push(word)
        elif word == ')':                                #식에 괄호 )가 있을 경우 스택을 검사하여 ( 탐색
            while True:
                temp = stack.pop()
                if temp == '(':                          #괄호 (가 있을 경우 탐색 중단
                    break
                result.append(temp)
                if stack.count == 0:
                    raise Exception("괄호 ( 오류")       #괄호 (가 없을 경우 에러
                    return    
        else:
            if order(word) == -1:                       #적절하지 않은 문자 탐색(정수, 연산자, 변수가 아닌 문자들)
                print("바르지 않은 문자 {0}이 입력되었습니다.".format(word))
                return
            
            temp = stack.get_top()                      #연산자 우선 순위 파악 및 추가
            while stack.count > 0 and order(temp) >= order(word):
                temp = stack.pop()
                result.append(temp)
                
            stack.push(word)
    return "".join(result)
       
def isspace(word):                                      #공백 판별
    return word.split() == list()

def islower(word):                                      #변수(영어 소문자) 판별
    return word.islower()

def isdigit(word):                                      #정수 판별
    return word.isdigit()

def order(word):                                        #연산자 우선 순위 판별
    if word == '*' or word == '/':
        return 3
    elif word == '+' or word == '-':
        return 2
    elif word == '(':
        return 1
    elif word =='\0':
        return 0
    else:
        return -1

stack = Stack()                                        #스택을 전역 변수로 선언 및 
if __name__ == '__main__':
    main()

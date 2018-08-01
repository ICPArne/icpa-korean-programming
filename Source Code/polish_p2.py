class Stack:
    def __init__(self, size = 20):
        """자료의 개수: count / 스택 크기: size"""
        self.size = size
        self.count = 0
        self.top = None; self.bottom = None
        self.list = list()

    def push(self, thing = None):
        """스택에 자료를 추가"""
        if len(self.list) + 1 > self.size:
            #print("스택 오버플로우")
            return
        self.count += 1
        self.list.append(thing)

    def pop(self):
        """스택에서 자료를 제거 및 반환"""
        if self.count == 0:
            #print("스택 언더플로우")
            return
        self.count -= 1
        a=self.list.pop()
        return a

    def get_top(self):
        if self.count == 0:
            #print("스택 언더플로우")
            return
        return self.list[self.count - 1]

def main():
    """메인 함수"""
    text = input("> ")
    result = polish(text)
    if result == '':
        print("유효한 식이 없습니다.")
        return
    #answer = execute(result)

    print("변환:", result)
    #print("결과:", answer)

    return "정상적으로 실행 완료"

def polish(txt):
    """역폴란드 표기법"""
    global stack
    text=txt+'\0'
    result = list()
    for index in range(len(text)):
        word = text[index]

        #공백 건너뛰기
        if isspace(word):
            continue

        #행의 끝이면
        if word=='\0':
            while stack.count > 0:
                #스택의 나머지를 출력
                a=stack.pop()
                result.append(a)
                if result[len(result) - 1] == '(':
                    print("괄호 (가 바르지 않음")
                    return

        #변수(여기선 소문자 영어 알파벳)나 숫자면 출력
        if islower(word) or isdigit(word):
            result.append(word)
            continue

        if word == '(':
            stack.push(word)
        elif word == ')':
            while True:
                temp = stack.pop()
                if temp=='(':
                    break
                result.append(temp)
                if stack.count == 0:
                    print("괄호 (가 바르지 않음")
                    return    
        else:
            if order(word) == -1:
                print("바르지 않은 문자 {0}이 입력되었습니다.".format(word))
                return
            
            temp = stack.get_top()
            while stack.count > 0 and order(temp) >= order(word):
                temp = stack.pop()
                result.append(temp)
                
            stack.push(word)
    return "".join(result)

#공백 판별        
def isspace(word):
    return word.split() == list()

#소문자(a-z = 1-26)
def islower(word):
    return word.islower()

#정수
def isdigit(word):
    return word.isdigit()

#우선순위
def order(word):
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

#전역(global)
stack = Stack()
if __name__ == '__main__':
    main()

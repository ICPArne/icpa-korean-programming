#whales_make_code.py
#토큰을 파이썬 코드롤 변경

from enum import Enum, auto
from token_p import *


class customLine(Enum):
    출력 = auto()
    입력 = auto()
    범위반복 = auto()
    조건반복 = auto()
    만약 = auto()
    대신 = auto()
    아니면 = auto()
    함수선언 = auto()
    구=auto()
    반환=auto()
    정수변환 = auto()
    실수변환 = auto()
    문자열변환 = auto()
    대입값 = auto()
    또는 = auto()
    그리고 = auto()


codeText = '''
숫자 = 5
숫자 < 10인 동안 반복:
	숫자 += 1
	숫자 출력하기
'''

factorial_code = '''
숫자 받는 팩토리얼 선언:
    만약 숫자 <= 1면:
        1 반환하기
    아니면:
        숫자 * 팩토리얼(숫자 - 1) 반환하기

팩토리얼(5) 출력하기
'''

factorial_python_code = '''
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
'''

fibonacci_code = '''
숫자 받는 피보나치 선언:
    만약 숫자 <= 2면:
        1 반환하기
    아니면:
        피보나치(숫자 - 1) + 피보나치(숫자 - 2) 반환하기

피보나치(5) 출력하기
'''

fibonacci_python_code = '''
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(5))
'''

def isCustom(lis):
    customLis = [
        TknKind.반복,
        TknKind.만약,
        TknKind.대신,
        TknKind.아니면,
        TknKind.출력,
        TknKind.입력,
        TknKind.동안,
        TknKind.참,
        TknKind.거짓,
        TknKind.또는,
        TknKind.그리고,
        TknKind.받는,
        TknKind.선언,
        TknKind.반환,
        TknKind.정수변환,
        TknKind.실수변환,
        TknKind.문자열변환,
        TknKind.대입값
    ]
    kindLis = [i.kind for i in lis]
    for i in kindLis:
        if i in customLis:
            return True
    return False

def delCharReToken(lis,index,num):
    lis[index].text=lis[index].text[:-num]
    lis[index]=reToken(lis[index])

def getKind(lis):
    kindLis=[i.kind for i in lis]
    if TknKind.출력 in kindLis:
        return customLine.출력
    if TknKind.입력 in kindLis:
        return customLine.입력
    if TknKind.반환 in kindLis:
        return customLine.반환
    if TknKind.반복 in kindLis:
        if TknKind.동안 in kindLis:
            return customLine.조건반복
        else:
            return customLine.범위반복
    if TknKind.만약 in kindLis:
        return customLine.만약
    if TknKind.대신 in kindLis:
        return customLine.대신
    if TknKind.선언 in kindLis:
        return customLine.함수선언
    if TknKind.대입값 in kindLis:
        return customLine.대입값
    return customLine.구



def reToken(tkn):
    a=getToken(tkn.text)
    if len(a)==0:
        return Token(TknKind.Empty,'')
    else:
        return a[0]

def translate(lis):
    kindLis = [i.kind for i in lis]
    lineKind = getKind(lis)
    if lineKind==customLine.함수선언:
        num=kindLis.index(TknKind.받는)
        argLis=lis[:num]
        argText=''
        for i in argLis:
            argText+=i.text
        return 'def '+lis[num+1].text+'('+argText+'):'
    if lineKind==customLine.만약 or lineKind==customLine.대신:
        num=kindLis.index(TknKind.Colon)-1 # ~면 문자열
        delCharReToken(lis,num,1)
        guCode=translate(lis[1:-1])
        firstWord=''
        if lineKind==customLine.만약:
            firstWord='if'
        elif lineKind==customLine.대신:
            firstWord='elif'
        return firstWord+' ('+guCode+'):'
    if lineKind==customLine.범위반복:
        hasDis=False
        if TknKind.간격 in kindLis:
            hasDis=True
        iterNum=-1
        fromNum=-1
        endNum=-1
        for i in range(len(lis)):
            if iterNum==-1:
                if lis[i].text[-1] in ['을','를']:
                    iterNum=i
                    delCharReToken(lis,i,1)
            elif fromNum==-1:
                if lis[i].text.endswith('부터'):
                    fromNum=i
                    delCharReToken(lis,i,2)
            else:
                if lis[i].text.endswith('까지'):
                    endNum=i
                    delCharReToken(lis,i,2)
                    break
        if hasDis:
            disNum=kindLis.index(TknKind.간격)
            forNum=kindLis.index(TknKind.반복)
            roNum=forNum-1
            delCharReToken(lis,roNum,1)
            roGuCode=translate(lis[disNum+1:roNum+1])
        iterGuCode=translate(lis[:iterNum+1])
        fromGuCode=translate(lis[iterNum+1:fromNum+1])
        endGuCode=translate(lis[fromNum+1:endNum+1])
        if hasDis:
            return 'for '+iterGuCode+' in range('+fromGuCode+',('+endGuCode+')+1,'+roGuCode+'):'
        else:
            return 'for '+iterGuCode+' in range('+fromGuCode+',('+endGuCode+')+1):'
    if lineKind==customLine.조건반복:
        whileNum=kindLis.index(TknKind.동안)
        delCharReToken(lis,whileNum-1,1)
        whileGuCode=translate(lis[:whileNum])
        return 'while ('+whileGuCode+'):'
    if lineKind==customLine.입력:
        return lis[0].text+'=input("입력: ")'
    if lineKind==customLine.출력:
        guCode=translate(lis[:-1])
        return 'print('+guCode+')'
    if lineKind==customLine.반환:
        guCode=translate(lis[:-1])
        return 'return '+guCode
    if lineKind==customLine.대입값:
        ofNum=-1
        eqNum=kindLis.index(TknKind.대입값)
        for i in range(len(lis)):
            if lis[i].text.endswith('의'):
                ofNum=i
                break
        delCharReToken(lis,ofNum,1)
        strGuCode=translate(lis[:ofNum+1])
        formatGuCode=translate(lis[ofNum+1:eqNum])
        return strGuCode+'.format'+formatGuCode
    if lineKind==customLine.구:
        changeDict={
            TknKind.아니면: 'else',
            TknKind.참: 'True',
            TknKind.거짓: 'False',
            TknKind.문자열변환: 'str',
            TknKind.실수변환: 'float',
            TknKind.정수변환: 'int',
            TknKind.또는: ' or ',
            TknKind.그리고: ' and '
        }
        result=''
        for i in lis:
            if i.kind in changeDict:
                result+=changeDict[i.kind]
            else:
                result+=i.text
        return result




def delTabTranslate(lis):
    i=0
    while True:
        if lis[i].kind==TknKind.Tab:
            i+=1
        else:
            break
    a=translate(lis[i:])
    return ('\t'*i)+str(a)

def rawToCode(rawText):
    lis=getToken(rawText)
    if isCustom(lis):
        return delTabTranslate(lis)
    else:
        return rawText

def main(codeText):
    codeLis = codeText.split('\n')
    resultCode = ''
    for i in codeLis:
        resultCode += str(rawToCode(i)) + '\n'
    return resultCode

if __name__ == '__main__':
    code=main(codeText)
    print(code)
    exec(code)

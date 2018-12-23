from enum import Enum, auto
from .token_p import *

class customLine(Enum):
    출력     = auto()
    삭제     = auto()
    입력     = auto()
    범위반복 = auto()
    조건반복 = auto()
    만약     = auto()
    대신     = auto()
    아니면   = auto()
    함수선언 = auto()
    구       = auto()
    반환     = auto()
    대입값   = auto()
    아님     = auto()
    있음     = auto()
    않음     = auto()
    길이     = auto()
    추가     = auto()
    위치     = auto()
    비우기   = auto()
    지우기   = auto()
    꺼내기   = auto()
    대입     = auto()


codeText = '''
그래프, 출발점을 받는 BFS 선언하기:
    큐 = []
    방문한곳 = []

    큐에 출발점 추가하기
    방문한곳에 출발점 추가하기

    큐의 길이 > 0인 동안 반복하기:
        현재위치 = 큐에서 꺼낸 값
        현재위치 출력하기

        번호를 0부터 그래프[현재위치]의 길이까지 반복하기:
            다음위치 = 그래프[현재위치][번호]
            
            만약 다음위치가 방문한곳 안에 있지 않음이면:
                큐에 다음위치 추가하기
                방문한곳에 다음위치 추가하기

그래프 = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

BFS(그래프, 1)

'''

def isCustom(lis):
    customLis = [
        TknKind.반복,
        TknKind.만약,
        TknKind.대신,
        TknKind.아니면,
        TknKind.출력,
        TknKind.삭제,
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
        TknKind.배열변환,
        TknKind.대입값,
        TknKind.탈출,
        TknKind.돌아가기,
        TknKind.길이,
        TknKind.아님,
        TknKind.있음,
        TknKind.않음,
        TknKind.추가,
        TknKind.위치,
        TknKind.비우기,
        TknKind.지우기,
        TknKind.꺼내기,
        TknKind.없음
    ]
    kindLis = [i.kind for i in lis]
    for i in kindLis:
        if i in customLis:
            return True
    return False

def delCharReToken(lis, index, num):
    tempStr = lis[index].text[:-num]
    temp = reToken(tempStr)
    lis[index] = temp

def lisTranslate(lis):
    temp = []
    for i in lis:
        if type(i) == list:
            temp += i
        else:
            temp.append(i)
    return translate(temp)

def getKind(lis):
    kindLis = [i.kind for i in lis]
    if TknKind.Assign in kindLis:
        return customLine.대입
    if TknKind.출력 in kindLis:
        return customLine.출력
    if TknKind.삭제 in kindLis:
        return customLine.삭제
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
    if TknKind.추가 in kindLis:
        return customLine.추가
    if TknKind.위치 in kindLis:
        return customLine.위치
    if TknKind.비우기 in kindLis:
        return customLine.비우기
    if TknKind.지우기 in kindLis:
        return customLine.지우기
    if TknKind.꺼내기 in kindLis:
        return customLine.꺼내기
    if TknKind.대입값 in kindLis:
        return customLine.대입값
    if TknKind.아님 in kindLis:
        return customLine.아님
    if TknKind.길이 in kindLis:
        return customLine.길이
    if TknKind.있음 in kindLis:
        return customLine.있음
    if TknKind.않음 in kindLis:
        return customLine.않음
    return customLine.구



def reToken(text):
    a = getToken(text)
    if len(a) == 0:
        return [Token(TknKind.Empty, '')]
    else:
        return a

def translate(lis):
    kindLis = [i.kind for i in lis]
    lineKind = getKind(lis)
    if lineKind == customLine.대입:
        eqNum = kindLis.index(TknKind.Assign)
        leftGuCode = lisTranslate(lis[:eqNum])
        rightGuCode = lisTranslate(lis[eqNum+1:])
        return leftGuCode + '=' + rightGuCode
    if lineKind == customLine.함수선언:
        num = kindLis.index(TknKind.받는)
        argLis = lis[:num]
        argText = ''
        for i in argLis:
            argText += i.text
        return 'def ' +lis[num+1].text + '('+argText[:-1] + '):'
    if lineKind == customLine.만약 or lineKind == customLine.대신:
        num = kindLis.index(TknKind.Colon) - 1 # ~이면 문자열
        delCharReToken(lis, num, 2)
        guCode = lisTranslate(lis[1:-1])
        firstWord = ''
        if lineKind == customLine.만약:
            firstWord = 'if'
        elif lineKind == customLine.대신:
            firstWord = 'elif'
        return firstWord + ' (' + guCode + '):'
    if lineKind == customLine.범위반복:
        hasDis = False
        if TknKind.간격 in kindLis:
            hasDis = True
        iterNum = -1
        fromNum = -1
        endNum = -1
        for i in range(len(lis)):
            if iterNum == -1:
                if lis[i].text[-1] in ['을','를']:
                    iterNum = i
                    delCharReToken(lis, i, 1)
            elif fromNum == -1:
                if lis[i].text.endswith('부터'):
                    fromNum = i
                    delCharReToken(lis, i, 2)
            else:
                if lis[i].text.endswith('까지'):
                    endNum = i
                    delCharReToken(lis, i, 2)
                    break
        if hasDis:
            disNum = kindLis.index(TknKind.간격)
            forNum = kindLis.index(TknKind.반복)
            roNum = forNum-1
            delCharReToken(lis, roNum, 1)
            roGuCode = lisTranslate(lis[disNum+1:roNum+1])
        iterGuCode = lisTranslate(lis[:iterNum+1])
        fromGuCode = lisTranslate(lis[iterNum+1:fromNum+1])
        endGuCode = lisTranslate(lis[fromNum+1:endNum+1])
        if hasDis:
            return 'for ' + iterGuCode + ' in range(' + fromGuCode + ',(' + endGuCode + '),' + roGuCode + '):'
        else:
            return 'for ' + iterGuCode + ' in range(' + fromGuCode + ',(' + endGuCode + ')):'
    if lineKind == customLine.조건반복:
        whileNum = kindLis.index(TknKind.동안)
        delCharReToken(lis, whileNum - 1, 1)
        whileGuCode = lisTranslate(lis[:whileNum])
        return 'while (' + whileGuCode + '):'
    if lineKind == customLine.입력:
        return lis[0].text + '=input("입력: ")'
    if lineKind == customLine.삭제:
        guCode = lisTranslate(lis[:-1])
        return 'del ' + guCode
    if lineKind == customLine.출력:
        guCode = lisTranslate(lis[:-1])
        return 'print(' + guCode + ')'
    if lineKind == customLine.반환:
        guCode = lisTranslate(lis[:-1])
        return 'return ' + guCode
    if lineKind == customLine.대입값:
        ofNum = -1
        eqNum = kindLis.index(TknKind.대입값)
        for i in range(len(lis)):
            if lis[i].text.endswith('의'):
                ofNum = i
                break
        delCharReToken(lis, ofNum, 1)
        strGuCode = lisTranslate(lis[:ofNum+1])
        formatGuCode = lisTranslate(lis[ofNum+1:eqNum])
        return strGuCode + '.format' + formatGuCode + lisTranslate(lis[eqNum+1:])
    if lineKind == customLine.아님:
        notNum = kindLis.index(TknKind.아님)
        ofNum = notNum - 1
        delCharReToken(lis, ofNum, 1)
        guCode = lisTranslate(lis[:ofNum+1])
        return 'not (' + guCode + ')'
    if lineKind == customLine.길이:
        lenNum = kindLis.index(TknKind.길이)
        ofNum = lenNum - 1
        delCharReToken(lis, ofNum, 1)
        guCode = lisTranslate(lis[:ofNum + 1])
        restCode=lisTranslate(lis[lenNum+1:])
        return 'len(' + guCode + ')' + restCode
    if lineKind == customLine.있음:
        isNum = -1
        for i in range(len(lis)):
            if lis[i].text[-1] in ['이','가']:
                isNum = i
                delCharReToken(lis, isNum, 1)
                break
        inNum = kindLis.index(TknKind.안에)
        lisGuCode = lisTranslate(lis[isNum+1:inNum])
        findGuCode = lisTranslate(lis[:isNum+1])
        return '(' + findGuCode + ') in (' + lisGuCode + ')'
    if lineKind == customLine.않음:
        isNum = -1
        for i in range(len(lis)):
            if lis[i].text[-1] in ['이', '가']:
                isNum = i
                delCharReToken(lis, isNum, 1)
                break
        inNum = kindLis.index(TknKind.안에)
        lisGuCode = lisTranslate(lis[isNum+1:inNum])
        findGuCode = lisTranslate(lis[:isNum+1])
        return '(' + findGuCode + ') not in (' + lisGuCode + ')'
    if lineKind == customLine.추가:
        atNum = -1
        for i in range(len(lis)):
            if lis[i].text.endswith('에'):
                atNum = i
                break
        delCharReToken(lis, atNum, 1)
        lisGuCode = lisTranslate(lis[:atNum+1])
        addGuCode = lisTranslate(lis[atNum+1:-1])
        return '(' + lisGuCode + ').append(' + addGuCode + ')'
    if lineKind == customLine.위치:
        fromNum = -1
        placeNum = kindLis.index(TknKind.위치)
        findNum = placeNum-1
        for i in range(len(lis)):
            if lis[i].text.endswith('에서'):
                fromNum = i
                break
        delCharReToken(lis, fromNum, 2)
        delCharReToken(lis, findNum, 1)
        lisGuCode = lisTranslate(lis[:fromNum+1])
        findGuCode = lisTranslate(lis[fromNum+1:findNum+1])
        return '(' + lisGuCode + ').index(' + findGuCode + ')' + lisTranslate(lis[placeNum+1:])
    if lineKind == customLine.지우기:
        fromNum = -1
        for i in range(len(lis)):
            if lis[i].text.endswith('에서'):
                fromNum = i
                break
        remNum = kindLis.index(TknKind.지우기)
        delCharReToken(lis, fromNum, 2)
        lisGuCode = lisTranslate(lis[:fromNum+1])
        remGuCode = lisTranslate(lis[fromNum+1:remNum])
        return '(' + lisGuCode + ').remove(' + remGuCode + ')'
    if lineKind == customLine.비우기:
        lisGuCode = lisTranslate(lis[:-1])
        return '(' + lisGuCode + ').clear()'
    if lineKind == customLine.꺼내기:
        isIndex = False
        indexNum = -1
        lisNum = -1
        lastNum = -1
        indexGuCode = ''
        for i in range(len(lis)):
            if lis[i].text.endswith('번을'):
                indexNum = i
                isIndex = True
                delCharReToken(lis, indexNum, 2)
                break
        if isIndex:
            for i in range(len(lis)):
                if lis[i].text.endswith('의'):
                    lisNum = i
                    delCharReToken(lis, lisNum, 1)
                    break
            indexGuCode = lisTranslate(lis[lisNum+1:indexNum+1])
            lastNum = indexNum + 1
        else:
            for i in range(len(lis)):
                if lis[i].text.endswith('에서'):
                    lisNum = i
                    delCharReToken(lis, lisNum, 2)
                    break
            indexGuCode = ''
            lastNum = lisNum+1
        lisGuCode = lisTranslate(lis[:lisNum+1])
        if lis[lastNum].text == '꺼낸':
            lastNum += 1
        return '(' + lisGuCode + ').pop(' + indexGuCode + ')' + lisTranslate(lis[lastNum+1:])


    if lineKind == customLine.구:
        changeDict = {
            TknKind.아니면:     'else',
            TknKind.참:         'True',
            TknKind.거짓:       'False',
            TknKind.문자열변환: 'str',
            TknKind.실수변환:   'float',
            TknKind.정수변환:   'int',
            TknKind.배열변환:   'list',
            TknKind.또는:       ' or ',
            TknKind.그리고:     ' and ',
            TknKind.탈출:       'break',
            TknKind.돌아가기:   'continue',
            TknKind.없음:       'None'
        }
        result = ''
        for i in lis:
            if i.kind in changeDict:
                result += changeDict[i.kind]
            else:
                result += i.text
        return result


def rawToCode(rawText):
    j = 0
    for i in range(len(rawText)):
        if rawText[i] == ' ' or rawText[i] == '\t':
            pass
        else:
            j = i
            break
    lis = getToken(rawText[j:])
    if isCustom(lis):
        return rawText[:j] + translate(lis)
    else:
        return rawText

def main(codeText):
    codeLis = codeText.split('\n')
    resultCode = ''
    for i in codeLis:
        resultCode += str(rawToCode(i)) + '\n'
    return resultCode

if __name__ == '__main__':
    code = main(codeText)
    print(codeText)
    print(code)
    exec(code)

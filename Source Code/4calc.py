import re
def checkGobNa(a): #곱하기/나누기 연산
    reRule=re.compile('([0-9.-]+)(곱하기|나누기)([0-9.-]+)')
    searchResult=reRule.search(a)
    if searchResult==None: #곱하기 또는 나누기가 더이상 없으면
        return a           #결과 반환
    if searchResult.group(2)=='곱하기': #곱하기일 때, 두 수 곱셈
        calc=float(searchResult.group(1))*float(searchResult.group(3))
    elif searchResult.group(2)=='나누기':
        calc=float(searchResult.group(1))/float(searchResult.group(3))
    result=a[:searchResult.span()[0]]+str(calc)+a[searchResult.span()[1]:] #나머지 내용+연산결과+나머지 내용
    return checkGobNa(result) #재귀

def checkPlusMinus(a):
    reRule=re.compile('([0-9.-]+)(더하기|빼기)([0-9.-]+)')
    searchResult=reRule.search(a)
    if searchResult==None:
        return a
    if searchResult.group(2)=='더하기':
        calc=float(searchResult.group(1))+float(searchResult.group(3))
    elif searchResult.group(2)=='빼기':
        calc=float(searchResult.group(1))-float(searchResult.group(3))
    result=a[:searchResult.span()[0]]+str(calc)+a[searchResult.span()[1]:]
    return checkPlusMinus(result)

def doCalc(a):
    return float(checkPlusMinus(checkGobNa(a))) #연산 순서

asdf='1빼기100곱하기3나누기5곱하기2더하기10'
print(doCalc(asdf))

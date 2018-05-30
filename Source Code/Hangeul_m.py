import re, ast

class Hangeul(object):
    @classmethod
    def checkMulDiv(cls, text):
        rule = re.compile('([0-9]+[.0-9]*[0-9]*)(곱하기|나누기)([0-9]+[.0-9]*[0-9]*)')
        searchResult = rule.search(text)
        
        if searchResult == None:
            return text.strip()
        if searchResult.group(2) == '곱하기':
            calc = float(searchResult.group(1)) * float(searchResult.group(3))
        elif searchResult.group(2) == '나누기':
            try:
                calc = float(searchResult.group(1)) / float(searchResult.group(3))
            except ZeroDivisionError:
                print("0으로 나눌 수 없습니다.")
                return

        result = text[:searchResult.span()[0]] + str(calc) + text[searchResult.span()[1]:]
        return cls.checkMulDiv(result)

    @classmethod
    def checkPluMin(cls, text):
        rule = re.compile('([0-9]+[.0-9]*[0-9]*)(더하기|빼기)([0-9]+[.0-9]*[0-9]*)')
        searchResult = rule.search(text)

        if searchResult == None:
            return text.strip()
        if searchResult.group(2) == '더하기':
            calc = float(searchResult.group(1)) + float(searchResult.group(3))
        elif searchResult.group(2) == '빼기':
            calc = float(searchResult.group(1)) - float(searchResult.group(3))

        result = text[:searchResult.span()[0]] + str(calc) + text[searchResult.span()[1]:]
        return cls.checkPluMin(result)

    @classmethod
    def doCalc(cls, text):
        text = text.replace(' ', '')
        text = cls.checkMulDiv(text)
        if text == None:
            return
        text = cls.checkPluMin(text)
        if float(text) % 1.0 != 0:
            return float(text)
        else:
            return int(text[:text.find('.')])


print(Hangeul.doCalc("0.5 더하기 1"))

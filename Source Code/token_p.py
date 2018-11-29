#token_p.py
#토큰, 키워드 설정 및 

from enum import *
import string
import sys

class TknKind(Enum):
    Lparen = auto()
    Rparen = auto()
    Plus = auto()
    Minus = auto()
    Multi = auto()
    Divi = auto()
    Modulo = auto()
    Assign = auto()
    Comma = auto()
    DblQ = auto()
    Equal = auto()
    NotEq = auto()
    Less = auto()
    LessEq = auto()
    Great = auto()
    GreatEq = auto()
    If = auto()
    Else = auto()
    End = auto()
    Print = auto()
    Ident = auto()
    IntNum = auto()
    String = auto()
    Letter = auto()
    Digit = auto()
    반복 = auto()
    만약 = auto()
    대신 = auto()
    아니면 = auto()
    출력 = auto()
    입력 = auto()
    동안 = auto()
    Colon = auto()
    참 = auto()
    거짓 = auto()
    또는 = auto()
    그리고 = auto()
    받는 = auto()
    선언 = auto()
    간격 = auto()
    반환 = auto()
    정수변환 = auto()
    실수변환 = auto()
    문자열변환 = auto()
    대입값 = auto()
    Empty = auto()
    Tab = auto()
    FloatNum = auto()
    EofTkn = auto()
    Others = auto()
    Hashtag = auto()

class Token:
    def __init__(self, kind = TknKind.Others, text = "", intVal = 0):
        self.kind = kind          #토큰의 종류
        self.text = text          #토큰 문자열
        self.intVal = intVal      #상수일 때의 값



class Keyword:
    def __init__(self, keyName = "", keyKind = TknKind.Others):
        self.keyName = keyName
        self.keyKind = keyKind

KeyWdTbl = [
    Keyword('if', TknKind.If),
    Keyword('else', TknKind.Else),
    Keyword('반복', TknKind.반복),
    Keyword('만약', TknKind.만약),
    Keyword('대신', TknKind.대신),
    Keyword('아니면', TknKind.아니면),
    Keyword('출력하기', TknKind.출력),
    Keyword('입력받기', TknKind.입력),
    Keyword('반환하기', TknKind.반환),
    Keyword('정수', TknKind.정수변환),
    Keyword('실수', TknKind.실수변환),
    Keyword('문자열', TknKind.문자열변환),
    Keyword('대입값', TknKind.대입값),
    Keyword('동안',TknKind.동안),
    Keyword('참',TknKind.참),
    Keyword('거짓',TknKind.거짓),
    Keyword('또는', TknKind.또는),
    Keyword('그리고', TknKind.그리고),
    Keyword('받는',TknKind.받는),
    Keyword('선언',TknKind.선언),
    Keyword('간격',TknKind.간격),
    Keyword('end', TknKind.End),
    Keyword('print', TknKind.Print),
    Keyword(':', TknKind.Colon),
    Keyword('(', TknKind.Lparen),
    Keyword(')', TknKind.Rparen),
    Keyword('+', TknKind.Plus),
    Keyword('-', TknKind.Minus),
    Keyword('*', TknKind.Multi),
    Keyword('/', TknKind.Divi),
    Keyword('%', TknKind.Modulo),
    Keyword('=', TknKind.Assign),
    Keyword(',', TknKind.Comma),
    Keyword('==', TknKind.Equal),
    Keyword('!=', TknKind.NotEq),
    Keyword('<', TknKind.Less),
    Keyword('<=', TknKind.LessEq),
    Keyword('>', TknKind.Great),
    Keyword('>=', TknKind.GreatEq),
    Keyword('\t', TknKind.Tab),
    Keyword('#', TknKind.Hashtag)
]

ch=' '
ctyp = {}
token = Token()
index = 0
c = ' '
text = ''
char=0

def init():
    global ch, ctyp, token, index, c, text, char
    ch=' '
    ctyp = {}
    token = Token()
    index = 0
    c = ' '
    text = ''
    char=0


def getToken(t):
    global token, text
    init()
    text=t
    tknLis=[]
    initChTyp()
    token = nextTkn()
    while token.kind != TknKind.EofTkn:
        tknLis.append(token)
        token = nextTkn()
    return tknLis

def initChTyp():
    for i in '0123456789.':
        ctyp[i]=TknKind.Digit
    for i in string.ascii_letters:
        ctyp[i]=TknKind.Letter
    ctyp['('] = TknKind.Lparen
    ctyp[')'] = TknKind.Rparen
    ctyp['<'] = TknKind.Less
    ctyp['>'] = TknKind.Great
    ctyp['+'] = TknKind.Plus
    ctyp['-'] = TknKind.Minus
    ctyp['*'] = TknKind.Multi
    ctyp['/'] = TknKind.Divi
    ctyp['%'] = TknKind.Modulo
    ctyp['_'] = TknKind.Letter
    ctyp['='] = TknKind.Assign
    ctyp[','] = TknKind.Comma
    ctyp['"'] = TknKind.DblQ
    ctyp['\t'] = TknKind.Tab
    ctyp['#'] = TknKind.Hashtag
        
def getChTyp(a):
    if a in ctyp:
        return ctyp[a]
    if 12593<=ord(a)<=55203:
        return TknKind.Letter
    else:
        return TknKind.Others

def nextTkn():
    num=0
    global ch
    txt=''

    while ch==' ':
        ch=nextCh()
    if ch=='\0':
        return Token(TknKind.EofTkn,txt)
    knd=getChTyp(ch)
    if knd==TknKind.Letter:
        while getChTyp(ch)==TknKind.Letter or getChTyp(ch)==TknKind.Digit:
            txt+=ch
            ch=nextCh()
    else:
        if knd==TknKind.Digit:
            numTxt=''
            while getChTyp(ch)==TknKind.Digit:
                numTxt+=ch
                ch=nextCh()
            floatNum=float(numTxt)
            if floatNum%1==0:
                return Token(TknKind.IntNum,str(int(floatNum)),int(floatNum))
            else:
                return Token(TknKind.FloatNum,str(floatNum),floatNum)
        elif knd==TknKind.DblQ:
            txt+='"'
            ch=nextCh()
            while ch!='\0' and ch!='\n' and ch!='"':
                txt+=ch
                ch=nextCh()
            txt+='"'
            if ch!='"':
                #print('문자열 리터럴을 닫지 않았습니다.')
                #sys.exit(1)
                raise Exception("문자열 리터럴을 닫지 않았습니다.")
            ch=nextCh()
            return Token(TknKind.String,txt)
        else:
            txt+=ch
            ch0=ch
            ch=nextCh()
            if is_ope2(ch0,ch):
                txt+=ch
                ch=nextCh()
    kd=get_kind(txt);
    if kd==TknKind.Others:
        #print('잘못된 토큰 {0}이 입력되었습니다.'.format(txt))
        #sys.exit(1)
        raise Exception("잘못된 토큰 {0}이/가 입력되었습니다.".format(txt))
    return Token(kd,txt)

def nextCh():
    global char, text
    char=0
    if len(text)==0:
        return '\0'
    else:
        a=text[0]
        text=text[1:]
        return a

def is_ope2(c1,c2):
    if c1=='\0' or c2=='\0':
        return False
    s=c1+c2
    return s in ['<=','>=','==','!=']

def get_kind(s):
    for i in KeyWdTbl:
        if s==i.keyName:
            return i.keyKind
    typ=getChTyp(s[0])
    if typ==TknKind.Letter:
        return TknKind.Ident
    if typ==TknKind.Digit:
        return TknKind.IntNum
    return TknKind.Others

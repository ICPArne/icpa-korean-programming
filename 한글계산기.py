def check(s):
    s = s.split()
    for x in s:
        if x == '더하기':
            change(s,'더하기','+')
        elif x == '빼기':
            change(s,'빼기','-')
        elif x == '곱하기':
            change(s,'곱하기','*')
        elif x == '나누기':
            change(s,'나누기','/')

    s = " ".join(s)
    
    return s

def change(s,a,b):
    x = s.index(a)
    s[x] = b


s = input("입력 : ")
print(s)
print(s.split())
print(check(s))
print(eval(check(s)))

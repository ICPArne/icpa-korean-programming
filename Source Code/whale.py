from silhaeng import *
from sys import exit

from tkinter import *
from tkinter import scrolledtext
import random

scr = None
i = None
gui_txt = None


def click():
    global scr, i, gui_txt

    gui_txt = scr.get(1.0, END)
    i.withdraw()
    i.destroy()


def turn_on_gui(before=False):
   global scr, i, gui_txt

   i = random.random
   i = Tk()
   i.title("고래(Ver 1.2.1)")

   code_label = LabelFrame(i, text="코드 작성 부분")
   code_label.grid(column=0, row=0, padx=8, pady=4, sticky=N + S + E + W)
   Grid.rowconfigure(i, 0, weight=1)
   Grid.columnconfigure(i, 0, weight=1)
   scr = scrolledtext.ScrolledText(code_label, wrap=WORD)
   scr.grid(column=0, row=0, sticky=N + S + E + W)
   Grid.rowconfigure(code_label, 0, weight=1)
   Grid.columnconfigure(code_label, 0, weight=1)
   '''
   #버튼 관련 주석
   b_image = PhotoImage(file="button.png")
   b_1 = Button(i, image=b_image, bg="white", command=lambda: click())
   b_1.grid(column=0, row=1)
   '''
   if before:
       scr.insert(END, gui_txt)

   i.bind("<F5>", lambda x=1: click())

   i.lift()
   i.attributes('-topmost', True)
   i.after_idle(i.attributes, '-topmost', False)
   i.after(1, lambda: scr.focus_force())
   i.grab_set()
   i.grab_release()

   i.mainloop()



def kor_input():
    result = list()
    while True:
        text = input("> ")
        if text.replace(' ', '') == '':
            continue
        elif text == '작성시작':
            turn_on_gui()
            return gui_txt
        elif text == '기존코드':
            if gui_txt is None:
                print("기존에 작성된 코드가 없습니다.")
                continue
            turn_on_gui(before=True)
            return gui_txt
        elif text == '화면청소':
            import os
            return "import os \nos.system('cls')"
        elif text == '도움말':
            print("작성시작: 코드를 입력할 수 있는 새로운 창이 열립니다. 'F5'키를 누를 경우 실행됩니다.")
            print("기존코드: 가장 마지막으로 입력한 코드가 써져있는 창이 열립니다.")
            print("화면청소: 화면을 초기화합니다. 기존에 작성된 코드와 그 결과는 초기화되지 않습니다.")
            print("종료: 프로그램을 종료합니다.")
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
            raw_code = kor_input()
            if type(raw_code) == type(None):
                raw_code = ''
            exec(main(raw_code))
            
        except NameError as name:
            name_str = "".join([x for x in name.args])
            print("이름 오류: 변수, 함수명 '{0}'이/가 존재하지 않습니다.".format(name_str[6:name_str.find("'", 7)]))

        except TypeError as value:
            value_str = "".join([x for x in value.args])
            first = value_str.split()[0]
                
            # 함수 매개변수 오류
            if first not in ('unsupported', 'can', 'must', 'cannot'):
                if value_str.split()[1][0] == 'm':
                    if int(value_str[value_str.find('missing')+8:value_str.find('required')-1]) <= 2:
                        mis_args = value_str.split(':')[1][1:].replace(' and ', ', ')
                        print("자료형 오류: 함수 '{0}'에 필요한 매개변수 {1}개 - {2}이/가 없습니다.". \
                              format(value_str.split()[0], value_str[value_str.find('missing')+8:value_str.find('required')-1], mis_args))
                    else:
                        mis_args = value_str.split(':')[1][1:].replace(' and ', ' ')
                        print("자료형 오류: 함수 '{0}'에 필요한 매개변수 {1}개 - {2}이/가 없습니다.". \
                              format(value_str.split()[0], value_str[value_str.find('missing')+8:value_str.find('required')-1], mis_args))
                        
                elif value_str.split()[0][0] == "'":
                    if value_str == "'str' object does not support item assignment":
                        print("자료형 오류: 문자열 리터럴의 일부를 수정할 수 없습니다.")
                    else:
                        if value_str.split()[-1] == 'iterable':
                            typeKind = {"'int'": '정수', "'str'": '문자열', "'float'": '실수', "'list'": '배열', "'tuple'": '튜플', "'dict'": '사전', "'type'": '자료형', "'NoneType'": '없음', "'complex'": '복소수'}
                            value_spt = value_str.split()

                            for i in range(len(value_spt)):
                                if value_spt[i] in typeKind.keys():
                                    value_spt[i] = typeKind[value_spt[i]]

                            print("자료형 오류: '{0}'은/는 반복될 수 없는 자료형입니다.".format(value_spt[0]))
                else:
                    value_spt = value_str.split()
                    value_spt[0] = value_spt[0][:-2]
                    value_spt[-1] = value_spt[-1][1:-1]
                    typeKind = {'int': '정수', 'str': '문자열', 'float': '실수', 'list': '배열', 'tuple': '튜플', 'dict': '사전', 'type': '자료형', 'NoneType': '없음', 'complex': '복소수'}

                    for i in range(len(value_spt)):
                        if value_spt[i] in typeKind.keys():
                            value_spt[i] = typeKind[value_spt[i]]

                    print("자료형 오류: 함수 '{0}'의 매개변수의 자료형은 '{1}'이/가 들어가서는 안 됩니다.". \
                          format(value_spt[0]+"()", value_spt[-1]))
                    
            # 연산 타입 오류
            else:
                typeKind = {"'int'": '정수', "'str'": '문자열', "'float'": '실수', "'list'": '배열', "'tuple'": '튜플', "'dict'": '사전', "'type'": '자료형', "'NoneType'": '없음', "'complex'": '복소수'}
                value_spt = value_str.split()
                
                for i in range(len(value_spt)):
                    if value_spt[i] in typeKind.keys():
                        value_spt[i] = typeKind[value_spt[i]]

                if value_spt[0] == 'unsupported':
                    print("자료형 오류: '{0}', '{1}' 사이에 부적절한 연산자 '{2}'가 사용되었습니다.". \
                          format(value_spt[5], value_spt[7], value_spt[4][0]))
                    
                elif value_spt[0] == 'must':
                    typeKind = {'int': '정수', 'str': '문자열', 'float': '실수', 'list': '배열', 'tuple': '튜플', 'dict': '사전', 'type': '자료형', 'NoneType': '없음', 'complex': '복소수'}
                    value_spt[2] = value_spt[2][:-1]
                    
                    for i in range(len(value_spt)):
                        if value_spt[i] in typeKind.keys():
                            value_spt[i] = typeKind[value_spt[i]]
                            
                    print("자료형 오류: '{0}'이/가 사용되지 않고 '{1}'이/가 사용되어야 합니다.". \
                          format(value_spt[4], value_spt[2]))
                    
                elif value_spt[0] == 'can':
                    if value_str.split()[3] == 'list':
                        print("자료형 오류: 배열은 배열만을 더해서 연장할 수 있습니다.")
                    elif value_str.split()[3] == 'str':
                        print("자료형 오류: 문자열은 문자열만을 더해서 연장할 수 있습니다.")
                    elif value_str.split()[3] == 'tuple':
                        print("자료형 오류: 튜플은 튜플만을 더해서 연장할 수 있습니다.")
                    else:
                        print("자료형 오류: 연산이나 함수에 쓰인 자료형을 확인하십시오.")

                elif value_spt[0] == 'cannot':
                    typeKind = {'int': '정수', 'str': '문자열', 'float': '실수', 'list': '배열', 'tuple': '튜플', 'dict': '사전', 'type': '자료형', 'NoneType': '없음', 'complex': '복소수'}
                    for i in range(len(value_spt)):
                        if value_spt[i] in typeKind.keys():
                            value_spt[i] = typeKind[value_spt[i]]

                    print("자료형 오류: '{0}'은/는 반복될 수 없는 자료형입니다.".format(value_spt[3]))
        
                
        except RecursionError as recur:
            recur_str = "".join([x for x in recur.args])
            print("재귀 오류: 함수의 재귀가 무한정으로 일어납니다.")

        except ValueError as val:
            val_str = "".join([x for x in val.args])
            print("값 오류: 함수의 매개변수의 자료형이 일치하지 않습니다.")

        except SyntaxError as syn:
            print("입력 오류: 잘못된 코드를 입력하였습니다.")

        except EOFError as eof:
            print("문자열 오류: 문자열 리터럴을 닫지 않았습니다.")

        except TokenError as tok:
            print("입력 오류:", "".join([x for x in tok.args]))

        except IndexError as ind:
            print("인덱스 오류: 자료의 크기를 초과한 범위를 사용하였습니다.")

        except ZeroDivisionError as zero:
            print("나눗셈 오류: 0으로 나눌 수 없습니다.")

        except KeyboardInterrupt:
            print("Ctrl+C가 입력되어 중지되었습니다.")

        except Exception as e:
            exc_str = "".join([x for x in e.args])
            if exc_str == "'list' object has no attribute 'text'":
                print("입력 오류: 잘못된 코드를 입력하였습니다.")
            else:
                print('오류:', e.args)

        finally:
            scr = None
            i = None

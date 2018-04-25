class JongHoon(object):
    def __init__(self):
        self.name = "JongHoon"
        self.age = 18
    def print_jonghoon(self, message):
        print("Jonghoon said,", message)
    @classmethod
    def is_byeoungsin(cls):
        return True
    
jh = JongHoon()
jh.print_jonghoon("빼애애액")
if JongHoon.is_byeoungsin():
    jh.print_jonghoon("으아앙")
else:
    jh.print_jonghoon("뿌애앵")

##########################################
# 예상 출력 결과: #########################
# Jonghoon said, 빼애애액 #################
# Jonghoon said, 으아앙 ###################
##########################################

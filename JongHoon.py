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
#
##########################################
# 예상 출력 결과: #########################
# 빼애애액 ################################
##########################################
#####빼애애애액(현찬이)####################

from random import seed
from random import randint


class SecurityDevice:
    def __init__(self):
        self.input = ""

    def security(self, input1):
        self.input = input1
        state = 0
        code = ""
        for c in self.input:
            if state == 0 and c == "9":
                code += c
                state += 1
            elif state == 1 and c == "8":
                code += c
                state += 1
            elif state == 2 and c == "7":
                code += c
                state += 1
            elif state == 3 and c == "0":
                code += c
                state += 1
            elif state == 4 and c == "6":
                code += c
                state += 1
            elif state == 5 and c == "1":
                code = ""
                state = 0
                print("unlocked")
            elif state == 5 and c == "4":
                code = ""
                state = 0
                print("locked")
            else:
                code = ""
                state = 0


run = True
count = 0
input2 = ""
while run:
    input2 += str(randint(0, 9))
    print(input2)
    if input2 == "stop" or input2 == "Stop":
        run = False
    print(SecurityDevice.security(SecurityDevice, input2))
    if SecurityDevice.security(SecurityDevice, input2) == "unlocked":
        run = False
        print("Final count is :" + count)
    count += 1

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
while run:
    input2 = input("Enter a code or enter 'stop' to exit: ")
    if input2 == "stop" or input2 == "Stop":
        run = False
    SecurityDevice.security(SecurityDevice, input2)

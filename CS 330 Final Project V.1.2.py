

input = "9870610000000009870642222222223333333333398706133333322222222987"
#input = "9870651xxxxx98706xx1xxxxx98706xxxxxxx9887061"  #Should 98706x1 unlock the device assuming that x is an illegal character (so not 0-9)? If so, we only need to change the else case so that it only clears the code and state if the input was 0-9, not an illegal character


state = 0
# output = "locked"
#output = True
code = ""

#breakpoint()
for c in input:
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
        # output = "unlocked"
        #output = False
        print("unlocked")
    elif state == 5 and c == "4":
        code = ""
        state = 0
        # output = "locked"
        #output = True
        print("locked")
    else:
        code = ""
        state = 0

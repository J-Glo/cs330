**Security Device - CS 330 - Jonathan Gloria**

**Programs' Function:**

This program takes a string as an input and, depending on the characters of the string, will either print "unlocked", "locked", or will do nothing. 
The unlock code is 986071, the lock code is 987064. 
The user inputs either a single digit or multiple digits, and the security device checks to see if the digits entered matches the unlock or lock code. If the codes match, the program will either print "unlocked" or "locked" respectively. The program continualy prompts the user for a code until they enter "Stop" which will terminate the program. As long as any substring of the input matches the unlock/lock code, the security device will unlock/lock. For example, the unlock code is 986071, so an input of 986071 will unlock the device, or xxxx986071xxxxx will also unlock the code with "x" representing any integer. However, entering each digit seperatly, such as 9, then 8, then 6, etc. will not unlock the device. 

---

## How to build and run the executable:
I have already built the executables for your convenience, so you only need to run the exectuable

1. Open Git Bash
2. Clone the repository by entering "git clone https://github.com/J-Glo/cs330.git"
3. Go to the directory by entering "cd cs330.
4. Run the executable by entering "./cs330SecurityDevice.exe"


---

## Testing:

The python file "" includes my testing of the program using a random number gaenerator.

---


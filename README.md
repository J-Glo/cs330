**Security Device - CS 330 - Jonathan Gloria**

**Programs' Function:**

This program takes a string as an input and, depending on the characters of the string, will either print "unlocked", "locked", or will do nothing. 
The unlock code is 986071, the lock code is 987064. 
The security device starts in state 0 and will immediatly return to state 0 if an illegal character is entered (any character besides 0-9). 
Once the number 9 is inputted, the security device will switch to state 1. If an 8 is then entered, the device will go to state 2. Any other character besides 8 will result in the device to return to the inital state, state 0. 
Using the same logic, 7 must be entered next in order to reach state 3, 0 must be entered after 7 to reach state 4, and 6 must be entered after 0 to reach state 5.
Once in state 5, if a 1 is entered, the program will print "unlocked" and then return to state 0. If a 4 is entered, the program will print "locked" and then return to state 0.
---

## How to build and run the executable:
I have already built the executables for your convenience, so you only need to run the exectuable

1. Open Git Bash
2. Clone the repository by entering "git clone https://github.com/J-Glo/cs330.git"
3. Go to the directory by entering "cd cs330.
4. Run the executable byentering "./cs330SecurityDevice.exe"


---

## How to generate unit test coverage:

1. Click **Source** on the left side.
2. Click the README.md link from the list of files.
3. Click the **Edit** button.
4. Delete the following text: *Delete this line to make a change to the README from Bitbucket.*
5. After making your change, click **Commit** and then **Commit** again in the dialog. The commit page will open and you’ll see the change you just made.
6. Go back to the **Source** page.

---


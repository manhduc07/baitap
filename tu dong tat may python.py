import time
import os

while True:
    check=input("shut down your camputer (Yes/No)  ")
    if "Yes" == check or "yes" == check:
        break
    elif "No" == check or "no" == check:
        time.sleep(30)
    else:
        print("just Yes or No :)) pls")
        time.sleep(3)
    os.system('cls')
end=input("ENTER !") 
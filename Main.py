import keyboard
import time
txt = str(input("The text to spam: "))
delay = float(input("Delay between spam messages: "))
amount = int(input("Amount of spam messages: "))
print("Spaming in 4 seconds ...")
time.sleep(4)
for i in range(amount):
    i+=1
    keyboard.write(txt+" ")
    keyboard.press_and_release('enter')
    time.sleep(delay)

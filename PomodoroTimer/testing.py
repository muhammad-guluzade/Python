from time import sleep

number = 1000

def rec():
    global number
    if number > 0:
        number -= 1
        sleep(0.01)
        rec()
    else:
        print("Done")

rec()
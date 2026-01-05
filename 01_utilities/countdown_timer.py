import time
while True:
    try:
        seconds = int(input("Enter the number of seconds: "))
        if seconds < 1:
            print("Please enter a number greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input, please enter a whole number")
    
print("\n 🔔 Timer started..")
for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"⌛ Time Left: {time_format} ", end="\r")
    time.sleep(1)

print("\n Time's up! Take a break or move on to next task.")
# print("\a", end="\x07") # Beep sound

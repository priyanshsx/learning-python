import time 

# ask the user for the input time 
while True:
    try:
        input_time = input("Enter time for the timer (MM:SS): ").strip().split(":", 2)
        minutes = int(input_time[0])
        seconds = int(input_time[1])
        break 
    except (ValueError, IndexError):
        print(f"Please only enter numbers in the format (MM:SS). Example for 10 minutes and 0 seconds, enter: 10:00.\n")

# converting to seconds 

countdown = (minutes * 60) + seconds 

# looping until countdown == 0

while countdown > 0:
    mins, secs = divmod(countdown, 60)
    time.sleep(1)
    print(f"{mins:02d}:{secs:02d}", end="\r")
    countdown -= 1



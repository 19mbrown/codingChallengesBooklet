def timeToNum( time ):
    numList = time.split(":")
    hour = int(numList[0]) * 60
    minute = int(numList[1])
    return hour + minute

def isAlreadyEvent(startTime, endTime, times):
    for i in range(startTime, endTime):
        for j in times:
            if i in j:
                return True
    return False

def main():
    events = []
    times = []
    while True:
        name = input("What's the name of this event? ")
        startTime = timeToNum(input("What time does it start at? "))
        endTime = timeToNum(input("What time does it end at? "))
        isTaken = isAlreadyEvent(startTime, endTime, times)
        if not isTaken:
            times.append(range(startTime, endTime))
            events.append(name)
            print(name, "Added to events list.")
        else:
            print("This over laps with another event.")
        if input("Do you want to quit? ") == "y":
            break
        elif input("Do you want to print all events? ") == "y":
            print(", ".join(events))

if __name__ == "__main__":
    main()
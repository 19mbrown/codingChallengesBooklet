import datetime

diary = dict()
x = int()
while True:
    x += 1
    entry = input("Enter a diary entry:\n")
    diary[x] = [datetime.datetime.now().strftime("%H:%M:%S"), datetime.date.today().strftime("%B %d, %Y"), entry]
    for i in diary:
        print("\n".join(diary[i]), "\n")

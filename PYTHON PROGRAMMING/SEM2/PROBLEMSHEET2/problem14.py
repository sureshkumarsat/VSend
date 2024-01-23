seconds_user = int(input("ENTER NUMBER OF SECONDS : "))

days = seconds_user // (24 * 60 * 60)
seconds_user -= days * 24 * 60 * 60
hours = str(seconds_user // (60 * 60))
seconds_user -= int(hours) * 60 * 60
minutes = str(seconds_user // (60))
seconds = str(seconds_user % 60)
seconds_user -= int(minutes) * 60 - int(seconds)

if len(hours) == 1:
    hours = f"0{hours}"

if len(minutes) == 1:
    minutes = f"0{minutes}"

if len(seconds) == 1:
    seconds = f"0{seconds}"

string = f"{days} {hours}:{minutes}:{seconds}"
if seconds_user == 0:
    print(string)

frequency = float(input("ENTER FREQUENCY : "))

if frequency < 3 * 10 ** 9:
    freq_range = "RADIO WAVES"
elif 3 * 10 ** 9 <= frequency < 3 * 10 ** 12:
    freq_range = "MICROWAVES"
elif 3 * 10 ** 12 <= frequency < 4.3 * 10 ** 14:
    freq_range = "INFRARED LIGHT"
elif 4.3 * 10 ** 14 <= frequency < 7.5 * 10 ** 14:
    freq_range = "VISIBLE LIGHT"
elif 7.5 * 10 ** 14 <= frequency < 3 * 10 ** 17:
    freq_range = "ULTRAVIOLET LIGHT"
elif 3 * 10 ** 17 <= frequency < 3 * 10 ** 19:
    freq_range = "X - RAYS"
elif frequency > 3 * 10 ** 19:
    freq_range = "GAMMA RAYS"


print(f"{frequency} belongs to {freq_range}")

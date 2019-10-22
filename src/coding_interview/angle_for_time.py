from builtins import abs


def find_time(time_in: str):
    # time hour and min as an input
    # split 360/12 degree  = 30 deg
    # Angle for each min = 30/5 = 6 deg
    # find angle between 2 numbers
    # position of Hr hand
    # position of min hand
    # angle = position A - Position B
    hr, min = time_in.split(":")
    # print(hr, min)
    angle_for_hr_hand = 360 // 12
    angle_for_min_hand = angle_for_hr_hand // 5
    extra_angle_for_hr_hand = angle_for_min_hand / (5 * 5)

    # 4 * 30 = 120, 30 deg between 2 hrs, 6 deg between 2 mins
    position_a = angle_for_hr_hand * int(hr) + (int(min) * extra_angle_for_hr_hand)

    # 28 min = 5 * 30 + 4 * 6
    position_b = (int(min) // 5 * angle_for_hr_hand) + (int(min) % 5) * angle_for_min_hand

    return abs(position_a - position_b)


print(find_time('4:28'))
print(find_time('3:15'))
print(find_time('12:00'))
print('-------------')


def find_angle(time_in):
    hr, min = time_in.split(":")

    hr_hand_move_per_min = 360 / (12 * 60)
    min_hand_move_per_min = 360 / 60
    position_a = (int(hr) * 60 + int(min)) * hr_hand_move_per_min
    position_b = int(min) * min_hand_move_per_min
    return abs(position_a - position_b)


print(find_angle('4:28'))
print(find_angle('3:15'))
print(find_angle('12:00'))
print('-------------')


def clockangles(time_in):
    hour, minute = time_in.split(":")
    hour = int(hour)
    minute = int(minute)
    return abs((hour * 30 + minute * 0.5) - (minute * 6))


print(clockangles('4:28'))
print(clockangles('3:15'))
print(clockangles('12:00'))
print('-------------')

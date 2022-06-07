

def correlation(pashe_center, hand_center):
    x_abs = abs(pashe_center[0]-hand_center[0])
    y_abs = abs(pashe_center[1]-hand_center[1])
    avg = (x_abs + y_abs) / 2
    if avg < 25:
        return 1
    return 0

def escape(counter):
    # print(counter)
    if counter > 50:
        return 1
    return 0


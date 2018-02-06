def time_delta(t1, t2):
    delta = 0
    import re
    T1 = re.findall("\w+", t1)
    T2 = re.findall("\w+", t2)
    if int(T1[2]) == int(T2[2]):
        delta += 24 * 3600
    delta += (int(T1[3]) - int(T2[3])) * 3600
    delta += (int(T1[4]) - int(T2[4])) * 60
    delta += (int(T1[5]) - int(T2[5]))

    if t1[-5] != t2[-5]:
        delta += (int(T1[6]) + int(T2[6])) * 3600
    else:
        delta += (int(T1[6]) - int(T2[6])) * 3600

    return delta


if __name__ == "__main__":
    testCases = int(input())
    for i in range(testCases):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)

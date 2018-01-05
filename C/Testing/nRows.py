N = int(input())
for row in range(N, 0, -1):
    printeR = N
    S = ""
    for j in range(N, 0, -1):
        if j > row:
            # S += str(printeR)
            print(printeR, end="")
            printeR -= 1
        else:
            # S += str(printeR)
            print(printeR, end="")

    # print(S)
    print("")

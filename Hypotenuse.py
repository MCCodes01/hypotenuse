import math

def hypoto(s1, s2):
    if s1 != 0:
        return round((math.sqrt((s1**2) + (s2**2))),3)
    else:
            return -1

def main():
    s_1 = int(input("enter length of side 1 <or 0 to exit>"))
    s_2 = int(input("enter length of side 2 <or 0 to exit>"))
    s_3 = hypoto(s_1, s_2)
    if s_3 != -1:
        print(s_3)

main()
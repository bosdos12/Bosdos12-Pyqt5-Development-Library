# This library is just starting so there is nothing fancy here yet, i will start with actual updates soon.



def PercentageValue(p, s, a):
    width = a.primaryScreen().size().width()
    height = a.primaryScreen().size().height()
    if (p > 0) and p <= 100:
        if s == "h":
            return int((p/100)*height)
        elif s == "w":
            return int((p/100)*width)

        else:
            print(f"Invalid argument, please enter either 'v' or 'h' as the first parameter,\n{str(s)} is invalid;") 
    else:
        print(f"Please enter a percentage value between 0 and 100,\n{str(p)} is invalid;")

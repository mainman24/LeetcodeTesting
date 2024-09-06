
def intToRoman(num):
    num2 = num
    dict2 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    dict2 = dict(reversed(list(dict2.items())))
    length = len(str(num)) - 1
    rn_str = ''
    for i in range(len(str(num))):
        digit = num2 // (10 ** length)
        if len(str(num2)) > 1:
            if str(num2)[0] == "0":
                num2 = int(str(num2)[1:])
            print(num2)
        else:
            num2 = int(str(num2)[0:])

        number = digit * (10 ** length)
        length -= 1
        keys = list(dict2.keys())
        values = list(dict2.values())
        for j in range(0,len(keys)):
            if number >= values[j]:
                if str(number)[0] == '4' or str(number)[0] == '9': 
                    upper = values[j - 1]
                    x = j - 1
                    lower = values[j]
                    while ((upper - lower) != number):
                        try:
                            lower = values[j + 1]
                        except:
                            lower = values[0]
                    else:
                        rn_str += keys[values.index(lower)] + keys[values.index(upper)]
                    break
                number2 = number
                if number2 % values[j] != 0:
                    number2 -= values[j]
                    rn_str += keys[j]
                else:
                    times = number2 // values[j]
                    number2 -= times * values[j]
                    rn_str += times * keys[j]
                while number2 != 0:
                    if j+1 != len(keys):
                        x = j+1
                    else:
                        x = j
                    for k in range(x, len(keys)):
                        if number2 % values[k] == 0:
                            times = number2//values[k]
                            number2 -= values[k] * times
                            rn_str += keys[k] * times
                            break
                    break
                break
                        
                        
    return rn_str


x = intToRoman(1010)
print(x)


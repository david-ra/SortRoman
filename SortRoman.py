'''
Roman to Int Algorithm 
Looping for every character of the roman string
1. if the current character value is greather than or equal to the next symbol value, plus the value to result
2. if the current character value is smaller than the next symbol value, substract from the total.
'''
def roman2int(symbols):
    # mapping roman values from string to int 
    values = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "G":5000, "H":10000 }
    result = 0
    symbols = symbols.upper()
    length = len(symbols)

    for i in range(length):
        symbol = symbols[i]
        current_val = values[symbol]
        #print("current vs last:", current_val, last_val)
        if( i+1 < length ):
            _next = values[symbols[i+1]]
            if( current_val >= _next ):
                result+=current_val
            else:
                result-=current_val
        else:
            result+=current_val
    return result

def sortRoman(names):
    # split values into a pair list of [name, roman_number]
    names = [ name.split(" ") for name in names ]

    # sort by name and roman2int(int(roman_number))
    names.sort( key = lambda x: ( x[0], roman2int(x[1])))
    
    # return values sorted by name and roman string number
    return [ name[0]+" "+name[1] for name in names ]

def main():
    names = ["Louis XI", "Louis III", "Louis IX", "David IX", "David I", "Louis CXLIX"]
    names = sortRoman(names)
    print(names)


if __name__=="__main__":
    main()

# Generates VHDL case statement for use like a lookup table in BCD conversion to 7-segment display

## Constants / Settings ##
size_to_generate_to = 255
getter_signal = 'BCD_output'

# values: print, file
output_type = 'file'

# if output type is file
filename = 'test.txt'

## CODE ##
def generateCase(sizeTo, getter):
    maxSize = len(str(bin(sizeTo))[2:])
    for i in range(0,sizeTo+1):
        x = str(i)
        BCD_result = ''
        for j in range(0,len(x)):
            if x[j] == '0':
                BCD_result += "1111110"
            elif x[j] == '1':
                BCD_result += "0110000"
            elif x[j] == '2':
                BCD_result += "1101101"
            elif x[j] == '3':
                BCD_result += "1111001"
            elif x[j] == '4':
                BCD_result += "0110011"
            elif x[j] == '5':
                BCD_result += "1011011"
            elif x[j] == '6':
                BCD_result += "1011111"
            elif x[j] == '7':
                BCD_result += "1110000"
            elif x[j] == '8':
                BCD_result += "1111111"
            else:
                BCD_result += "1111011"
        
        BCD_result = enforceSize(BCD_result, (len(str(sizeTo))*7))
        output('\"' + BCD_result + '\" when input = \"' + enforceSize(str(bin(i))[2:],maxSize) + '\" else')

def enforceSize(x, maxSize):
    if(len(x) < maxSize):
        return ("0" * (maxSize - len(x))) + x
    return x

def output(string):
    if output_type == 'print':
        print string
    elif output_type == 'file':
        f.write(string)
        f.write('\n')
    else:
        raise Exception('incorrect output type')

if output_type == 'file':
    f = open(filename, 'w')

generateCase(size_to_generate_to, getter_signal)

if output_type == 'file':
    f.close()

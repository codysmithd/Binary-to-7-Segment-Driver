 Generates VHDL case statement for use like a lookup table in BCD conversion to 7-segment display

# Constants / Settings
size_to_generate_to = 999
getter_signal = "BCD_output"

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
        print 'case \"' + enforceSize(str(bin(i))[2:],maxSize) + '\" => ' + getter + ' <= \"' + BCD_result + '\";'

def enforceSize(x, maxSize):
    if(len(x) < maxSize):
        return ("0" * (maxSize - len(x))) + x
    return x

generateCase(size_to_generate_to, getter_signal)

from Crypto.Util.number import *

BASE10_STR = '11515195063862318899931685488813747395775516287289682636499965282714637259206269'

def main():
    n = long_to_bytes(int(BASE10_STR))
    str = n.decode()
    print(str)
    
if __name__ == '__main__':
    main()

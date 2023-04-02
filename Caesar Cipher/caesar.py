alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
    if direction=="encode":
        code=""
        if shift < 26:
            for i in text:
                if i in alphabet:
                    index=alphabet.index(i)
                    code_index=index+shift
                    j=index+1
                    k=len(alphabet)-j + shift
                    if code_index<=26:
                        code+=alphabet[code_index]
                    else :            
                        code+=alphabet[k-1]
                else:
                    code+=i
        elif shift >= 26:
            shift%=shift
            for i in text:
                if i in alphabet:
                    index=alphabet.index(i)
                    code_index=index+shift
                    j=index+1
                    k=len(alphabet)-j + shift
                    if code_index<=26:
                        code+=alphabet[code_index]
                    else :            
                        code+=alphabet[k-1]
                else:
                    code+=i
        print("Your encrypted code is %s" %code)
    elif direction=="decode":
        decode=""
        if shift < 26:
            for i in text:
                if i in alphabet:
                    index=alphabet.index(i)
                    code_index=index-shift
                    decode+=alphabet[code_index]
                else:
                    decode+=i
        elif shift >= 26:
            shift%=shift
            for i in text:
                if i in alphabet:
                    index=alphabet.index(i)
                    code_index=index-shift
                    decode+=alphabet[code_index]
                else:
                    decode+=i
        print("Your decrypted code is %s" %decode)
    else:
        print("Please enter correct direction, try next time!")
"""
Morse Code Encryption Tool
Created by John Fiore
01-29-2025
"""

MC_DICT = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

MC_REVERSE_DICT = {v: k for k, v in MC_DICT.items()}

C_WORDS = ['sos', 'attack', 'hello']

def encrypt(msg):
    cipher = ''
    for lttr in msg:
        if lttr != ' ':
            cipher += MC_DICT[lttr] + ' '
        else:
            cipher += ' '
    return cipher.strip()

def decrypt(msg):
    msg += ' '
    decipher = ''
    citxt = ''
    z = 0  # Initialize z

    for lttr in msg:
        if lttr != ' ':
            z = 0
            citxt += lttr
        else:
            z += 1
            if z == 2:
                decipher += ' '
            else:
                decipher += MC_REVERSE_DICT.get(citxt, '')  # Handle errors safely
                citxt = ''
    return decipher

def debug():
    testmsg = "HELLO I AM YES"
    result = encrypt(testmsg.upper())
    print(result)

    decrypted = decrypt(result)
    print(decrypted)

def cw_protocol(msg):
    if msg in C_WORDS:
            print(msg + " is a common word!")
    else:
        pass
        
def main():
    print("Welcome to the MCET.")
    print("a) Encrypt")
    print("a) Decrypt")
    ch1 = input("")
    
    if ch1 == "a":
        print("What to encrypt:")
        msg = input("")
        res = encrypt(msg.upper())
        print(res)
        cw_protocol(msg)
    elif ch1 == "b":
        print("What to decrypt:")
        msg = input("")
        res = decrypt(msg.upper())
        print(res)
        cw_protocol(res)

if __name__ == "__main__":
    main()

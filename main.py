MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def conversion(text):
    out_code = ''
    
    # Tackling words and sentences
    word_lst = text.split()
    
    for word in word_lst:
        for letter in word:
            
            try:
                out_code += MORSE_CODE_DICT[letter.upper()] + ' '
            except KeyError:
                # Handling Unsupported Characters
                print(f"Warning: Character '{letter}' cannot be converted. Skipping...")
        
        # Separate words with three spaces ( 7dits )
        out_code += '   '

                
    return out_code
    
    
    


if __name__=="__main__":
    text = input(f"Enter the text for Moorse code translation: ")
    
    moorse_code = conversion(text)
    
    print(f'Moorse code: {moorse_code}')
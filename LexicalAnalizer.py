from terminals import tokens 

class Lexical_Analizer:

    program = []
    tokens = []
    reserved_words = []
    symbols = []
    useless = []

    def __init__(self, program, reserved_words, symbols, useless):
        self.program = program
        self.reserved_words = reserved_words
        self.symbols = symbols
        self.useless = useless
    

    def token_separator(self):
        temp_tokens = []
        col = 0
        row = 0
        two_symbols = False
        for line in self.program:
            # print(line)
            row+=1
            col = 0
            line_character = ''
            for i in range (len(line)):
                col+=1
                if two_symbols: # pass by through the next i in for, 'cause the token had two symbols in it
                    two_symbols = False
                    continue
                if (line[i] == '#'): # ignore comments
                    break
                if (line[i] in self.useless or line[i] in self.symbols):
                    if (len(line_character) != 0): # for a single char symbol
                        temp_tokens.append([line_character, row, col-len(line_character)])
                    if (line[i] in self.symbols):
                        # look ahead for two symbols tokens
                        if line[i] in ['<', '>', '!', '=']:
                            if (line[i+1] == '='):
                                line_character = line[i] + line[i+1]
                                temp_tokens.append([line_character, row, col-len(line_character)])
                                two_symbols = True
                            else: # keep the possible single token (>,<,=)
                                temp_tokens.append([line[i], row, col-len(line_character)])
                        else: # others symbols
                            temp_tokens.append([line[i], row, col-len(line_character)])
                    # print('token', line_character, len(line_character))
                    line_character = ''
                else: # identifier and number tokens
                    line_character = line_character + line[i] 
        return temp_tokens

    def analyze(self):
        print('Lexical Analyzer...')
        temp_tokens = self.token_separator()
        success = True
        for tk in temp_tokens:
            # print(tk[0])
            word, row, col = tk[0], tk[1], tk[2]
            if word not in self.reserved_words and word not in self.symbols: # analyze words and numbers
                isInt = True
                if word[0].isalpha(): # ids must beggin with an alphabetic char
                    for i in word: # check the full word to match with the pattern
                        if not (i.isalpha() or i.isdigit()):
                            print('\x1b[1;31m' + '[%d,%d] !ERROR' % (row, col) + '\x1b[0m' + ' Wrong declaration of identificator!')
                            success = False
                            # panic mode - wash away the rest of the word from the wrong char
                            # print(word.index(i))
                            n_word = ''
                            for c in range (0, word.index(i)):
                                n_word = n_word + word[c]
                            # print(n_word)
                            word = n_word
                            break
                    # append the ID
                    self.tokens.append(["{ID}", word, row, col])

                elif word[0].isdigit(): #numbers must beggin with a digit
                    for i in range (len(word)):
                        if word[i] == '.' and not isInt: # check the full number to match with the float pattern
                            print('\x1b[1;31m' + '[%d,%d] !ERROR' % (row, col) + '\x1b[0m' + ' Wrong declaration of float type!')
                            success = False
                            # panic mode - wash away the rest of the word from the wrong char
                            n_word = ''
                            # print(word[i])
                            for c in range (0, i):
                                n_word = n_word + word[c]
                            # print(n_word)
                            word = n_word
                            break
                        elif word[i] == '.' :
                            isInt = False
                        
                        if not word[i].isdigit() and not word[i] == '.':
                            print('\x1b[1;31m' + '[%d,%d] !ERROR' % (row, col) + '\x1b[0m' + ' Wrong declaration of float type!')
                            success = False
                            n_word = ''
                            # print(word[i])
                            for c in range (0, i):
                                n_word = n_word + word[c]
                            # print(n_word)
                            word = n_word
                            break
                    if isInt:
                        self.tokens.append(["{INT_NUMBER}", word, row, col])
                    else:
                        self.tokens.append(["{FLOAT_NUMBER}", word, row, col])

                else:
                    print('\x1b[1;31m' + '[%d,%d] !ERROR' % (row, col) + '\x1b[0m' + ' Invalid character!')
                    success = False
                    # panic mode - wash away the rest of the word from the wrong char
                    n_word = ''
                    # print(word[i])
                    for c in range (0, i):
                        n_word = n_word + word[c]
                    # print(n_word)
                    self.tokens.append(["{ID}", n_word, row, col])

            else:
                # append the reserved word or symbol
                temp = tokens[word]
                self.tokens.append([temp, word, row, col])

        # print(self.tokens)
        if success:
            print('\x1b[1;32m' + 'Compiled Successfully' + '\x1b[0m')
        return(self.tokens)
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
                if two_symbols:
                    two_symbols = False
                    continue
                if (line[i] == '#'):
                    break
                if (line[i] in self.useless or line[i] in self.symbols):
                    if (len(line_character) != 0):
                        temp_tokens.append([line_character, row, col-len(line_character)])
                    if (line[i] in self.symbols):
                        # look ahead
                        if (line[i+1] in self.symbols):
                            line_character = line[i] + line[i+1]
                            temp_tokens.append([line_character, row, col-len(line_character)])
                            two_symbols = True
                        else:
                            temp_tokens.append([line[i], row, col-len(line_character)])
                    # print('token', line_character, len(line_character))
                    line_character = ''
                else:
                    line_character = line_character + line[i] 
        return temp_tokens

    def analyze(self):
        print('-> Analisador léxico')
        temp_tokens = self.token_separator()

        for tk in temp_tokens:
            # print(tk[0])
            word, row, col = tk[0], tk[1], tk[2]
            if word not in self.reserved_words and word not in self.symbols:
                isInt = True
                if word[0].isalpha():
                    for i in word:
                        if not (i.isalpha() or i.isdigit()):
                            # erro -> tem q ver se coloca o token anyway
                            print('id ta errado em [', row, ',', col, ']')
                            break
                    # append the ID
                    self.tokens.append(["{ID}", word, row, col])

                elif word[0].isdigit():
                    
                    for i in word:
                        if i == '.' and not isInt:
                            # erro float
                            print('float ta errado em [', row, ',', col, ']')
                            break
                        elif i == '.' :
                            isInt = False
                    if isInt:
                        self.tokens.append(["{INT_NUMBER}", word, row, col])
                    else:
                        self.tokens.append(["{FLOAT_NUMBER}", word, row, col])

                else:
                    print('algo de errado nao esta certo em [', row, ',', col, ']')
                    self.tokens.append(["{ID}", word, row, col])

            else:
                # append the reserved word or symbol
                temp = tokens[word]
                self.tokens.append([temp, word, row, col])

        # print(self.tokens)
        return(self.tokens)
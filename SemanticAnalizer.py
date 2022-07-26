from email import message
from terminals import tokens, reserved_words, symbols
from grammar import non_terminals


class Semantic_Analizer:

    program = []
    reserved_words = []
    reserved_words = reserved_words
    symbols = symbols
    stack = []
    sentence = []
    non_terminals = non_terminals
    tokens_localization = []

    symbol_table = []

    def __init__(self, program, reserved_words, symbols, useless, program_tokens):
        self.program = program
        self.reserved_words = reserved_words
        self.symbols = symbols
        self.useless = useless
        self.program_tokens = program_tokens
    
    def checkUnusedVars(self):
        for var in self.symbol_table:
            if not var[2]:
                print('\033[93m' + '!!WARNING' + '\x1b[0m ' + var[0], 'is declared but never used')
    
    def var_declaration(self, token, next_token):
        # lexema, tipo, isUsed
        symbol = [next_token[1], token[1], False]
        self.symbol_table.append(symbol)
        # print('adiciona na tabela de simbolos', self.symbol_table)
    
    def getTypeOfVar(self, lex):
        for var in self.symbol_table:
            if var[0] == lex:
                return var[1]
    
    def changeToUsedVar(self, lex):
        for var in self.symbol_table:
            if var[0] == lex:
                var[2] = True
    
    def varIsDeclared(self, token):
        # print('procura se ta na tabela de simbolos')
        lex = token[1]
        for symbol in self.symbol_table:
            if symbol[0] == lex:
                return True
        return False
    
    def matchTypes(self, types):
        message = ''
        # se todos são iguais
        # INT COM INT
        # FLOAT COM FLOAT
        # BOOL COM BOOL
        # CHAR COM CHAR
        result = all(t == types[0] for t in types)
        # INT COM FLOAT
        # if not result:
        #     for t in types:
        #         if t not in ['int', 'float']:
        #             print(t)
        #             result = False
        #             return result, 'Variable types doesnt match'
        #     result = True
        if not result:
            message = 'Variable types doesnt match'
        return result, message
    
    def analyzeMultipleVars(self, tokens):
        types = []

        for token in tokens:
            if token[0] == "{INT_NUMBER}":
                types.append('int')
                # analyze = True
            elif token[0] == "{FLOAT_NUMBER}":
                types.append('float')
                # analyze = True
            elif self.varIsDeclared(token):
                types.append(self.getTypeOfVar(token[1]))
                self.changeToUsedVar(token[1])
                # analyze = True
            else:
                # print('unvalid', token)
                message = token[1] + ' is not declared'
                return False, message

        # print(types)
        result, message = self.matchTypes(types)
        if not result:
            # print(message)
            return result, message
        return True, ''

    
    def analyze(self):
        print('Semantic Analyzer...')
        i = 0
        success = True
        while i < len(self.program_tokens):
            # print(self.program_tokens[i])
            #print(self.program_tokens[i])
    
            # DECLARAÇÃO DE VARIÁVEIS
            if self.program_tokens[i][0] in ["{CHAR}","{FLOAT}","{INT}","{BOOLEAN}"]:
                self.var_declaration(self.program_tokens[i], self.program_tokens[i+1])
                i+=1
            
            # USO DE VARIÁVEIS
            elif self.program_tokens[i][0] == "{ID}":
                
                # ATRIB, RELACIONAL, ARITMÉTICO, LOGICO
                k = 0
                tokens_to_analize_together = []
                tokens_to_analize_together.append(self.program_tokens[i])
                while self.program_tokens[i+1+k][0] not in ["{;}", "{)}", "{AND}", "{OR}"]:
                    # print(self.program_tokens[i+1+k])
                    if self.program_tokens[i+1+k][0] in ["{ID}", "{INT_NUMBER}", "{FLOAT_NUMBER}"]:
                        tokens_to_analize_together.append(self.program_tokens[i+1+k])
                        k+=1
                    else:
                        k+=1
                    
                print('tokens juntos', tokens_to_analize_together)
                result, message = self.analyzeMultipleVars(tokens_to_analize_together)
                if not result:
                    print('\x1b[1;31m' + '!!ERROR' + '\x1b[0m ' + message, 'in line', self.program_tokens[i][2], 'column', self.program_tokens[i][3])
                    success = False
                    break
                i+=k

            
            i+=1
        self.checkUnusedVars()
        if success:
            print('\x1b[1;32m' + 'Compiled Successfully' + '\x1b[0m')


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
                print("!WARNING!", var[0], 'is declared but never used')
    
    def var_declaration(self, token, next_token):
        # lexema, tipo, isUsed
        symbol = [next_token[1], token[1], False]
        self.symbol_table.append(symbol)
        print('adiciona na tabela de simbolos', self.symbol_table)
    
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
        
        print(lex, 'is not declared!')
        return False
    
    def matchTypes(self, types):
        # INT COM INT
        # INT COM FLOAT
        # FLOAT COM FLOAT
        # BOOL COM BOOL
        # CHAR COM CHAR
        return False
    
    def analyzeMultipleVars(self, tokens):
        types = []

        for token in tokens:
            if token[0] == "{INT_NUMBER}":
                types.append('int')
                analyze = True
            elif token[0] == "{FLOAT_NUMBER}":
                types.append('float')
                analyze = True
            elif self.varIsDeclared(token):
                types.append(self.getTypeOfVar(token[1]))
                self.changeToUsedVar(token[1])
                analyze = True
            else:
                print('Unvalid token')
                return
        print(types)

        self.matchTypes(types)
        return analyze

    
    def analyze(self):
        print('Semantic Analyzer...')
        i = 0
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
                print(self.analyzeMultipleVars(tokens_to_analize_together))
                i+=k

            
            i+=1
        self.checkUnusedVars()


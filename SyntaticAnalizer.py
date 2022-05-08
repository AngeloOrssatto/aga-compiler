from terminals import tokens, reserved_words, symbols
from grammar import non_terminals
class Syntatic_Analizer:

    program = []
    tokens = tokens
    program_tokens = []
    reserved_words = []
    reserved_words = reserved_words
    symbols = symbols
    stack = []
    sentence = []
    non_terminals = non_terminals

    def __init__(self, program, reserved_words, symbols, useless, program_tokens):
        self.program = program
        self.reserved_words = reserved_words
        self.symbols = symbols
        self.useless = useless
        self.program_tokens = program_tokens
    
    def define_sentence(self):
        for item in self.program_tokens:
            # print(item)
            self.sentence.append(item[1])
        self.sentence.append('$')
        # print(self.sentence)
        

    def analyze(self):
        print('Sintatic Analyzer...')
        self.define_sentence()
        
        self.stack.append("Q")
        self.stack.append("int")
        self.stack.append("S")
        self.stack.append("$")
        #print(self.stack)

        i = 0
        X = self.stack[0]
        while X != '$': 
            X = self.stack[0]
            a = self.sentence[i]
        # for i in range (0, len(self.sentence)-1):
            # Se for terminal
            print('topo pilha:', X)
            print('pilha:', self.stack)
            if X not in self.non_terminals:
                # print('terminal', self.stack[i])
                if X == a:
                    print('desempilha', X, 'avança na sentença')
                    self.stack.pop(0)
                    i += 1
                else:
                    print('\x1b[1;31m' + '!ERROR')

            # Se não for terminal
            else:
                print('nao terminal', X)
                self.stack.pop(0)


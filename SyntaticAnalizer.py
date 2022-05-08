import pandas as pd

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

        parsing_table = pd.read_excel('TABELA PREDITIVA-v3.xlsx', index_col='PRODUCTION')
        
        self.stack.append("PROC")
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
            print('leitura sentença:', a)
            print('pilha:', self.stack)
            print('sentença:', self.sentence)

            if X not in self.non_terminals:
                # print('terminal', self.stack[i])
                if X == a:
                    # desempilha X
                    self.stack.pop(0)
                    # avança na sentença
                    i += 1
                else:
                    print('\x1b[1;31m' + '!ERROR' + '\x1b[0m' + ' - Primeiro caso')

            # Se não for terminal
            else:
                if type(parsing_table.loc[X, a]) is str:
                    # desempilha X
                    self.stack.pop(0)
                    print(self.stack)
                    # empilha produção ao contrario
                    res = parsing_table.loc[X, a]
                    res = res.split()
                    del(res[0:2])
                    res = [el for el in reversed(res)]
                    for el in res:
                        self.stack.insert(0, el)
                    
                else:
                    print('\x1b[1;31m' + '!ERROR' + '\x1b[0m' + ' - Segundo caso')

                

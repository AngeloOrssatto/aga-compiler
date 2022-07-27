
class ThreeAddressCode:

    symbol_table = []
    tokens = []
    intermediate_program = []
    aux_var_count = 1
    label_count = 1

    def __init__(self, symbol_table, tokens):
        self.symbol_table = symbol_table
        self.tokens = tokens
    
    def generateFile(self):
        with open(r'output.txt', 'w') as fp:
            for line in self.intermediate_program:
                fp.write("%s\n" % line)
        
    
    def getIntermediateProgram(self):
        return self.intermediate_program

    def analyze(self):
        print('gerar codigo 3 endereços')
        for i, token in enumerate(self.tokens):
            if i != len(self.tokens)-1:
                next_token = self.tokens[i+1]

            if token[0] in ["{INT}", "{FLOAT}", "{BOOLEAN}", "{CHAR}"]:
                self.variableDeclaration(token, next_token)
            
            if token[0] in ["{READ}", "{WRITE}"]:
                self.inputOutputDeclaration(token, self.tokens[i+2])

            if token[0] == "{ATRIB}":
                # print(token, next_token, self.tokens[i+2])
                if next_token[0] in ["{INT_NUMBER}", "{FLOAT_NUMBER}"]:
                    self.singleAtribution(self.tokens[i-1], next_token)
                elif next_token[0] == "{ID}" and self.tokens[i+2][0] == "{;}":
                    self.singleAtribution(self.tokens[i-1], next_token)
                else:
                    k = 0
                    expression = []
                    while self.tokens[i+k][0] != "{;}":
                        # print(k, self.tokens[i+k])
                        expression.append(self.tokens[i+k])
                        k+=1
                    self.expressionStatement(self.tokens[i-1], expression)
            
            if token[0] == "{IF}":
                k = 1
                condition = []
                while self.tokens[i+k+1][0] != "{)}":
                    condition.append(self.tokens[i+k+1][1])
                    k+=1
                self.ifStatement(condition)

            
            if token[0] == "{FOR}":
                k = 1
                condition = []
                condition.append(self.tokens[i+1][1])
                while self.tokens[i+k+4][0] != "{)}":
                    print(self.tokens[i+k+4])
                    condition.append(self.tokens[i+k+4][1])
                    k+=1
                self.forStatement(condition)
            # if token[0] == "{ELSE}":

            
        self.generateFile()


    def ifStatement(self, condition):
        print(condition)
        c_code = ''
        code = ''
        if len(condition) == 3:
            for i in condition:
                c_code += i + ' '
            code = 'if ' + c_code + ' goto l' + str(self.label_count)
            self.label_count += 1
            self.intermediate_program.append(code)
            print(code)
    
    def forStatement(self, condition):
        print('condiçao', condition)
        c_code = ''
        code = ''
        condition.pop(1)
        if len(condition) == 3:
            for i in condition:
                if i == ',':
                    i = '>'
                c_code += i + ' '
            label_begin = self.label_count
            self.label_count+=1
            label_exit_for = self.label_count
            self.label_count+=1
            code = 'l' + str(label_begin)
            self.intermediate_program.append(code)
            code = 'if ' + c_code + ' goto l' + str(label_exit_for)
            self.label_count += 1
            self.intermediate_program.append(code)
            # bloco de instruções
            # no fim, goto label começo 'label_begin'
            # novo label pra sair do for
            print(code)
        

    def variableDeclaration(self, token, next_token):
        code = token[1] + ' ' + next_token[1]
        # print(code)
        self.intermediate_program.append(code)
    
    def inputOutputDeclaration(self, token, next_token):
        code = token[1] + ' ' + next_token[1]
        # print(code)
        self.intermediate_program.append(code)
    
    def singleAtribution(self, prev_token, next_token):
        code = prev_token[1] + ' = ' + next_token[1]
        # print(code)
        self.intermediate_program.append(code)

    def expressionStatement(self, var, expression):
        # print(len(expression))
        c_code = ''
        code = ''
        if len(expression) == 4:
            for i in expression:
                c_code += i[1] + ' '
            code = var[1] + ' ' + c_code
        else:
            print('aqui é treta')
            aux = []
            for i in expression:
                aux.append(i[1])
            aux.pop(0)
            
            while len(aux) > 3:
                temp_var = 't'+ str(self.aux_var_count)
                code = temp_var + ' = ' + aux.pop(0) + aux.pop(0) + aux.pop(0)
                self.aux_var_count += 1
                aux.insert(0, temp_var)
                self.intermediate_program.append(code)
            code = var[1] + ' = ' + aux[0] + aux[1] + aux[2]

        #print('aqui', var, expression)
        #print(code)
        self.intermediate_program.append(code)
    

        
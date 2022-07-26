from lib2to3.pgen2 import token
from LexicalAnalizer import Lexical_Analizer
from SyntaticAnalizer import Syntatic_Analizer
from SemanticAnalizer import Semantic_Analizer
from terminals import reserved_words, symbols, useless

def main():
    file = open('./teste.txt', 'r')
    program = file.readlines()
    
    lexical = Lexical_Analizer(program, reserved_words, symbols, useless)
    tokens = lexical.analyze()
    # print(tokens)

    sintatic = Syntatic_Analizer(program, reserved_words, symbols, useless, tokens)
    sintatic.analyze()

    semantic = Semantic_Analizer(program, reserved_words, symbols, useless, tokens)
    semantic.analyze()

    return


if __name__ == "__main__":
    print("\n\tAGA - H Compiler")
    print("--------------------------------")
    main()

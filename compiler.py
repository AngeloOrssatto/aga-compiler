from LexicalAnalizer import Lexical_Analizer
from SyntaticAnalizer import Syntatic_Analizer
from terminals import reserved_words, symbols, useless

def main():
    file = open('./program1.txt', 'r')
    program = file.readlines()
    # for line in program:
    #     print(line)
    # print("--------------------------------")
    lexical = Lexical_Analizer(program, reserved_words, symbols, useless)
    tokens = lexical.analyze()
    # print("--------------------------------")
    # print('Tokens:')
    # print(tokens)

    sintatic = Syntatic_Analizer(program, reserved_words, symbols, useless, tokens)
    sintatic.analyze()

    return


if __name__ == "__main__":
    print("\n\tAGA - H Compiler")
    print("--------------------------------")
    main()

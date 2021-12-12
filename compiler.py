from LexicalAnalizer import Lexical_Analizer
from terminals import reserved_words, symbols, useless

def main():
    file = open('./program.txt', 'r')
    program = file.readlines()
    lexical = Lexical_Analizer(program, reserved_words, symbols, useless)
    tokens = lexical.analyze()
    return


if __name__ == "__main__":
    print("Compilador AGA - H")
    main()

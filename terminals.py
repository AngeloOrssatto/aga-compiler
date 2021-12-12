tokens = {
    "char": "{CHAR}",
    "int": "{INT}",
    "float": "{FLOAT}",
    "boolean": "{BOOLEAN}",

    "true": "{TRUE}",
    "false": "{FALSE}",

    "+": "{+}",
    "-": "{-}",
    "*": "{*}",
    "/": "{/}",

    "not": "{NOT}",
    "and": "{AND}",
    "or": "{OR}",

    "=": "{ATRIB}",
    "==": "{EQUAL}",
    "<": "{LESS}",
    "<=": "{LESS_EQUAL}",
    ">": "{MORE}",
    ">=": "{MORE_EQUAL}",
    "!=": "{DIFF}",

    ";": "{;}",
    "{": "{{}",
    "}": "{}}",
    "(": "{(}",
    ")": "{)}",
    "'": "{'}",

    "if": "{IF}",
    "else": "{ELSE}",
    "do": "{DO}",
    "while": "{WHILE}",
    "for": "{FOR}",
    "in": "{IN}",
    "range": "{RANGE}",
    "read": "{READ}",
    "write": "{WRITE}",
}

reserved_words = [
    'int', 
    'float', 
    'boolean', 
    'char', 
    'read', 
    'write', 
    'and', 
    'or', 
    'not',
    'if',
    'else',
    'do',
    'while',
    'for',
    'in',
    'range',
]

symbols = [
    '+',
    '-',
    '*',
    '/',
    '=',
    '<',
    '<=',
    '>',
    '>=',
    '!=',
    '==',
    '(',
    ')',
    "'",
    ';',
    '{',
    '}',
]

useless = [
    ' ',
    '\n',
    '\t',
]
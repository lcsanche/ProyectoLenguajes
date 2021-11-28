import ply.lex as lex


# Inicio-> Luis Carlos Sanchez Plaza
reserved = {
    #Condicionales
    'if' : 'IF',
    'else' : 'ELSE',
    'end':'END',
    
    #Bucles
    'for':'FOR',
    'in': "IN",
    'do': 'DO',
    'while' : 'WHILE',

    #Boolean
    'true': 'TRUE',
    'false': 'FALSE',

    #Imprimir y Leer
    'puts': 'PUTS',
    'gets': 'GETS',

    #Funciones
    'def': "DEF",
    'return' : "RETURN",

    # Funciones para Array
    'insert': "INSERT",
    'delete_at': "DELETE_AT",
    
    #Metodos para hash
    'delete': "DELETE",

    #metodos para stacks
    'search': "SEARCH",
    'push': "PUSH",

}

tokens = [
    'VARIABLE',

    #Datos Primitivos
    'NUMBER',
    'FLOAT',
    'STRING',

    #Operadores
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EXPONENTIATION',

    #Comparadores
    'GREATER',
    'GREATER_OR_EQUAL',
    'MINOR',
    'MINOR_OR_EQUAL',

    #Simbolos
    'RPAR',
    'LPAR',
    'RCOR',
    'LCOR',
    'RKEY',
    'LKEY',
    'OR',
    'AND',
    'NOT',
    'ASIGN',
    'COMMA',
    'POINT',
    'D_POINT',
    'QUESTION'
]+list(reserved.values())

# Fin-> Luis Carlos Sanchez Plaza

#Comentario Prueba

# Inicio -> Tommy Joel Villagómez Borja

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.'

# Regular expression rules for simple tokens
t_NUMBER = r'\d+'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*' 
t_DIVIDE = r'/'
t_EXPONENTIATION = r'\*\*'

t_GREATER = r'>'
t_GREATER_OR_EQUAL = r'>='
t_MINOR = r'<' 
t_MINOR_OR_EQUAL = r'<='

t_LPAR = r'\('
t_RPAR = r'\)'
t_LCOR = r'\['
t_RCOR = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_OR = r'\|\|'
t_AND = r'\&\&'
t_NOT = r'\!'
t_ASIGN = r'\='
t_COMMA = r'\,'
t_POINT = r'\.'
t_D_POINT = r'\:'
t_QUESTION = r'\?'

def t_VARIABLE(t):
    r'([a-z_$@] | @@)[A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t

# Inicio -> Paúl del Pezo
def t_STRING(t):
    r'(\"|\').*?(\"|\')'
    t.value = t.value[1:-1]
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
# Define a rule so we can track line numbers
def t_newline(t):
 r'\n+'
 t.lexer.lineno += len(t.value)

 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Fin -> Tommy Joel Villagómez Borja

# Build the lexer
lexer = lex.lex()
toks=[]
def analyze(data):
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        toks.append(str(tok))
def readAlgoritm(archivo):
    lines=archivo.split('\n')
    for line in lines:
        analyze(line)
        if len(line) == 0:
            break
    return toks

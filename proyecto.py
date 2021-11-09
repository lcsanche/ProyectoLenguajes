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
    
    #Operadores logicos
    'and':'AND',
    'or':'OR',

    #Boolean
    'true': 'TRUE',
    'false': 'FALSE',

    #Imprimir y Leer
    'puts': 'PUTS',
    'gets': 'GETS',

    #Funciones
    'def': "DEF",

    # Funciones para Array
    'insert': "INSERT",
    'delete_at': "DELETE_AT",
    
    #Metodos para hash
    'delete': "DELETE",

    #metodos para stacks
    'search': "SEARCH",
    'push': "PUSH",

    #Otros
    'include': 'INCLUDE',
    'alias': "ALIAS",
    'ensure': "ENSURE",
    'self': "SELF"
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
    'PIPE',
    'S_OR',
    'S_AND',
    'S_NOT',
    'ASIGN',
    'COMMA',
    'POINT',
    'QUESTION'
]+list(reserved.values())

# Fin-> Luis Carlos Sanchez Plaza

#Comentario Prueba

# Inicio -> Tommy Joel Villagómez Borja

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
t_ignore_COMMENT = r'#.'

# Regular expression rules for simple tokens
t_NUMBER = r'\d+'

t_PLUS = r'+'
t_MINUS = r'-'
t_TIMES = r'*' 
t_DIVIDE = r'/'
t_EXPONENTIATION = r'**'

t_GREATER = r'>'
t_GREATER_OR_EQUAL = r'>='
t_MINOR = r'<' 
t_MINOR_OR_EQUAL = r'<='

t_LPAR = r'('
t_RPAR = r')'
t_LCOR = r'['
t_RCOR = r']'
t_LKEY = r'{'
t_RKEY = r'}'
t_PIPE = r'|'
t_S_OR = r'||'
t_S_AND = r'&&'
t_S_NOT = r'!'
t_ASIGN = r'='
t_COMMA = r','
t_POINT = r'.'
t_QUESTION = r'?'

def tVARIABLE(t):
    r'[a-zA-Z$@][A-Za-z_0-9]'
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
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
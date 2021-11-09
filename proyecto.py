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
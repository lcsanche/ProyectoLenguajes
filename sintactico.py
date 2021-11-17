import ply.yacc as yacc
from lexico import tokens

# Inicio -> Luis Carlos Sanchez Plaza
def p_instrucciones(p):
    '''instrucciones : asignacion
                    | expression
                    | funciones
                    | comparacion
                    | condicional
                    | impresion
                    | input
                    | callFuncion
                    | addValueHash
                    | modValueHash
                    | deleteValueHash
    '''

def p_body(p):
    ''' cuerpo : asignacion
                | expression
                | comparacion
                | condicional
                | impresion
                | input
                | callFuncion
                | addValueHash
                | modValueHash
                | deleteValueHash
    '''
# ----------------------------------Asignacion----------------------------------
def p_asignacion(p):
    '''asignacion : VARIABLE ASIGN expression
                | VARIABLE ASIGN comparacion
                | VARIABLE ASIGN callFuncion
                | VARIABLE ASIGN diccionario
                | VARIABLE ASIGN getValueHash
    '''

# ----------------------------------Expresiones----------------------------------
def p_expression_term(p):
    '''expression : term 
                    | boleano
    '''

def p_term_factor(p):
    'term : factor'

def p_factor_num(p):
    '''factor : NUMBER
                | STRING
                | FLOAT
    '''

def p_factor_expr(p):
    'factor : LPAR expression RPAR'

# ----------------------------------Operaciones matematicas----------------------------------
def p_expression_plus(p):
    'expression : expression PLUS term'

def p_expression_minus(p):
    'expression : expression MINUS term'

def p_term_times(p):
    'term : term TIMES factor'

def p_term_div(p):
    'term : term DIVIDE factor'

def p_term_exp(p):
    'term : term EXPONENTIATION factor'

# ----------------------------------Comparador----------------------------------
def p_comparacion(p):
    '''comparacion : expression comparador expression
                    | expression comparador expression AND comparacion
                    | expression comparador expression OR comparacion
    '''

def p_comparador(p):
    '''comparador : GREATER 
                | GREATER_OR_EQUAL
                | MINOR
                | MINOR_OR_EQUAL
                | ASIGN ASIGN
                | NOT ASIGN
    '''

# ----------------------------------Condicional----------------------------------
def p_cond_if(p):
    '''condicional : IF comparacion D_POINT cuerpo END
                    | IF comparacion D_POINT cuerpo END cond_else
    '''

def p_cond_else(p):
    'cond_else : ELSE D_POINT cuerpo END'

# ----------------------------------Input e Impresion----------------------------------
def p_puts(p):
    'impresion : PUTS STRING'

def p_gets(p):
    'input : VARIABLE ASIGN GETS'

# ----------------------------------Funciones----------------------------------
def p_par_function(p):
    ''' parametros : VARIABLE
                    | VARIABLE COMMA parametros
    '''

def p_header_function(p):
    '''encabezado : DEF VARIABLE LPAR RPAR
                    | DEF VARIABLE LPAR parametros RPAR
    '''

def p_function(p):
    '''funciones : encabezado cuerpo END
                | encabezado RETURN expression END
                | encabezado cuerpo RETURN expression END
    '''

def p_call_function(p):
    '''callFuncion : VARIABLE LPAR RPAR
                | VARIABLE LPAR parametros RPAR
    '''
# ----------------------------------Booleanos----------------------------------
def p_boolean(p):
    '''boleano : TRUE 
                | FALSE
    '''

# ----------------------------------Hashes----------------------------------
def p_hash(p):
    'diccionario : LKEY cuerpoHash RKEY'

def p_body_hash(p):
    '''cuerpoHash : expression ASIGN GREATER expression
                    | expression ASIGN GREATER expression COMMA cuerpoHash
    '''

def p_get_hash(p):
    'getValueHash : VARIABLE LCOR expression RCOR'

def p_add_hash(p):
    'addValueHash : VARIABLE LCOR expression RCOR ASIGN expression'

def p_mod_hash(p):
    'modValueHash : VARIABLE LCOR expression RCOR ASIGN expression'

def p_del_hash(p):
    'deleteValueHash : VARIABLE POINT DELETE LPAR expression RPAR'

# Fin -> Luis Carlos Sanchez Plaza











# ----------------------------------Manejando Errores----------------------------------
def p_error(p):
    print("Error Sintactico!")

# Construyendo el parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
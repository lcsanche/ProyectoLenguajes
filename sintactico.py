import ply.yacc as yacc
from lexico import tokens

# Inicio -> Luis Carlos Sanchez Plaza
def p_instrucciones(p):
    '''instrucciones : asignacion
                    | expression
                    | funciones
                    | comparacion
                    | condicional
                    | while
                    | for
                    | impresion
                    | input
                    | callFuncion
                    | addValueHash
                    | modValueHash
                    | deleteValueHash
                    | insertArray
                    | deleteArray
                    | searchStack
                    | pushStack    
                    | metodoBoleano    
    '''

def p_body(p):
    ''' cuerpo : asignacion
                | expression
                | comparacion
                | condicional
                | impresion
                | for
                | while
                | input
                | callFuncion
                | addValueHash
                | modValueHash
                | deleteValueHash
                | insertArray
                | deleteArray
                | pushStack
                | searchStack
    '''
# ----------------------------------Asignacion----------------------------------
def p_asignacion(p):
    '''asignacion : VARIABLE ASIGN expression
                | VARIABLE ASIGN comparacion
                | VARIABLE ASIGN callFuncion
                | VARIABLE ASIGN diccionario
                | VARIABLE ASIGN getValueHash
                | VARIABLE ASIGN array
                | VARIABLE ASIGN stack
                | VARIABLE tipo_asignacion factor
                | VARIABLE ASIGN opMatematicas
    '''
def p_tipo_asignacion(p):
    '''tipo_asignacion : PLUS ASIGN
                        | MINUS ASIGN 
                        | TIMES ASIGN 
                        | DIVIDE ASIGN 
                        | EXPONENTIATION ASIGN 
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
                | VARIABLE
    '''

def p_factor_expr(p):
    'factor : LPAR expression RPAR'

# ----------------------------------Comparador----------------------------------
def p_comparacion(p):
    '''comparacion : expression comparador expression
                    | expression comparador expression AND comparacion
                    | expression comparador expression OR comparacion
                    | expression AND expression
                    | expression OR expression
    
    '''

def p_comparador(p):
    '''comparador : GREATER 
                | GREATER_OR_EQUAL
                | MINOR
                | MINOR_OR_EQUAL
                | ASIGN ASIGN
                | NOT ASIGN
    '''


# ----------------------------------Input e Impresion----------------------------------
def p_puts(p):
    'impresion : PUTS factor'

def p_gets(p):
    'input : VARIABLE ASIGN GETS'

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

#-----------------------------------Metodos booleanos----------------------------------
def p_boolean_method(p):
    '''metodoBoleano : VARIABLE POINT VARIABLE QUESTION LPAR expression RPAR
                    | VARIABLE POINT VARIABLE QUESTION LPAR RPAR
    '''

# Fin -> Luis Carlos Sanchez Plaza

# Inicio -> Tommy Joel Villag??mez Borja
#-----------------------------------while----------------------------------
def p_while(p):
    '''while : WHILE LPAR comparacion RPAR repCuerpo END
            | WHILE LPAR comparacion RPAR repCuerpo END while
    '''
def p_repCuerpo(p):
    '''repCuerpo : cuerpo 
                | cuerpo repCuerpo
    '''

#------------------------------------array-----------------------------------
def p_parA_function(p):
    ''' parametrosA : factor
                    | factor COMMA parametrosA
    '''
def p_array(p):
    '''array : LCOR parametrosA RCOR
             | LCOR RCOR
    '''

def p_argumentos_array(p):
    '''argumentosA : NUMBER COMMA factor
    '''
#------------------------------------sintacticoArray-------------------------
def p_insert_array(p):
    '''insertArray : VARIABLE POINT INSERT LPAR argumentosA RPAR
    '''

def p_delete_array(p):
    '''deleteArray : VARIABLE POINT DELETE_AT LPAR NUMBER RPAR
    '''

# Fin -> Tommy Joel Villag??mez Borja

# Inicio -> Paul Daniel del Pezo Navarrete
#------------------------------------for-----------------------------------
def p_for(p):
    '''for : FOR VARIABLE IN NUMBER POINT POINT NUMBER  DO repCuerpo END
            | FOR VARIABLE IN NUMBER POINT POINT NUMBER  DO repCuerpo END for
    '''
#------------------------------------stack-----------------------------------
def p_vacio(p):
    'vacio : '''
def p_stack(p):
    '''stack : STACK LPAR parametrosA RPAR
            | STACK LPAR vacio RPAR
    '''
def p_search_stack(p):
    '''searchStack : VARIABLE POINT SEARCH LPAR factor RPAR
    '''
def p_push_stack(p):
    '''pushStack : VARIABLE POINT PUSH LPAR factor RPAR
    '''

# Fin -> Paul Daniel del Pezo Navarrete



#----------------------------------------------------------Reglas Semanticas---------------------------------------------------------



# Inicio -> Luis Carlos Sanchez Plaza
# ----------------------------------Operaciones matematicas----------------------------------

def p_opMatematicas(p):
    ''' opMatematicas : suma
                    | resta
                    | multiplicacion
                    | division
                    | exponenciacion
    '''

def p_suma(p):
    '''suma : VARIABLE PLUS NUMBER
            | operadores PLUS operadores
            | operadores PLUS opMatematicas
            | operadores PLUS LPAR operadores RPAR
            | operadores PLUS LPAR opMatematicas RPAR
    '''

def p_resta(p):
    '''resta : VARIABLE MINUS NUMBER 
            | operadores MINUS operadores
            | operadores MINUS opMatematicas
            | operadores MINUS LPAR operadores RPAR
            | operadores MINUS LPAR opMatematicas RPAR
    '''

def p_multiplicacion (p):
    ''' multiplicacion : operadores TIMES operadores
                    | operadores TIMES LPAR operadores RPAR
                    | operadores TIMES LPAR opMatematicas RPAR
    '''

def p_divicion (p):
    ''' division : operadores DIVIDE operadores
                | operadores DIVIDE LPAR operadores RPAR
                | operadores DIVIDE LPAR opMatematicas RPAR
    '''

def p_exponenciacion (p):
    ''' exponenciacion : operadores EXPONENTIATION operadores
                    | LPAR operadores RPAR EXPONENTIATION operadores
                    | LPAR opMatematicas RPAR EXPONENTIATION operadores
    '''

def p_operadores(p):
    ''' operadores : enteros
                | FLOAT  
    '''
    
def p_enteros(p):
    ''' enteros : NUMBER
                | MINUS NUMBER
    '''

# Fin -> Luis Carlos Sanchez Plaza

# Inicio -> Tommy Joel Villagomez Borja
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
    '''funciones : encabezado repCuerpo END
                | encabezado RETURN expression END
                | encabezado repCuerpo RETURN expression END
    '''

def p_call_function(p):
    '''callFuncion : VARIABLE LPAR RPAR
                | VARIABLE LPAR parametros RPAR
    '''
# Fin -> Tommy Joel Villagomez Borja

# Inicio -> Paul del Pezo
# ----------------------------------Condicional----------------------------------
def p_cond_if(p):
    '''condicional : IF comparacion repCuerpo END
                    | IF comparacion repCuerpo cond_else
    '''

def p_cond_else(p):
    'cond_else : ELSE repCuerpo END'
# Fin -> Paul del Pezo

resultGUI = []


# ----------------------------------Manejando Errores----------------------------------
def p_error(p):
    resultGUI.append("-----------------------------------------------------------------")
    resultGUI.append("Error de sintaxis o sem??ntico!")
    resultGUI.append("El siguiente bloque de codigo es incorrecto: %s" % p.lexer.lexdata)
    resultGUI.append("-----------------------------------------------------------------")

# Build the parser
parser = yacc.yacc()
def readAlgoritmSint(file_name):
    resultGUI.clear()
    archivo = open(file_name, "r")
    for line in archivo:
        if line != "\n":
            if line[:3] == "for" or line[:3] == "def" or line[:5] == "while" or line[:2] == "if":
                nLine = line.replace("\n", "")
                for Eline in archivo:
                    nLine += " " + Eline.replace("\n", "").replace("\t", "")
                    if Eline[:3] == "end":
                        break
                line = nLine
            resultGUI.append(line)
            parser.parse(line)
    return resultGUI


    

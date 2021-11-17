
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ASIGN COMMA DEF DELETE DELETE_AT DIVIDE DO D_POINT EACH ELSE END ENSURE EXPONENTIATION FALSE FLOAT GETS GREATER GREATER_OR_EQUAL IF IN INCLUDE INSERT LCOR LKEY LPAR MINOR MINOR_OR_EQUAL MINUS NOT NUMBER OR PLUS POINT PUSH PUTS QUESTION RCOR RETURN RKEY RPAR SEARCH SELF STRING TIMES TRUE VARIABLE WHILEinstrucciones : asignacion\n                    | expression\n                    | funciones\n                    | comparacion\n                    | condicional\n                    | impresion\n                    | input\n                    | callFuncion\n                    | addValueHash\n                    | modValueHash\n                    | deleteValueHash\n     cuerpo : asignacion\n                | expression\n                | comparacion\n                | condicional\n                | impresion\n                | input\n                | callFuncion\n                | addValueHash\n                | modValueHash\n                | deleteValueHash\n    asignacion : VARIABLE ASIGN expression\n                | VARIABLE ASIGN comparacion\n                | VARIABLE ASIGN callFuncion\n                | VARIABLE ASIGN diccionario\n                | VARIABLE ASIGN getValueHash\n    expression : term \n                    | boleano\n    term : factorfactor : NUMBER\n                | STRING\n                | FLOAT\n    factor : LPAR expression RPARexpression : expression PLUS termexpression : expression MINUS termterm : term TIMES factorterm : term DIVIDE factorterm : term EXPONENTIATION factorcomparacion : expression comparador expression\n                    | expression comparador expression AND comparacion\n                    | expression comparador expression OR comparacion\n    comparador : GREATER \n                | GREATER_OR_EQUAL\n                | MINOR\n                | MINOR_OR_EQUAL\n                | ASIGN ASIGN\n                | NOT ASIGN\n    condicional : IF comparacion D_POINT cuerpo END\n                    | IF comparacion D_POINT cuerpo END cond_else\n    cond_else : ELSE D_POINT cuerpo ENDimpresion : PUTS STRINGinput : VARIABLE ASIGN GETS parametros : VARIABLE\n                    | VARIABLE COMMA parametros\n    encabezado : DEF VARIABLE LPAR RPAR\n                    | DEF VARIABLE LPAR parametros RPAR\n    funciones : encabezado cuerpo END\n                | encabezado RETURN expression END\n                | encabezado cuerpo RETURN expression END\n    callFuncion : VARIABLE LPAR RPAR\n                | VARIABLE LPAR parametros RPAR\n    boleano : TRUE \n                | FALSE\n    diccionario : LKEY cuerpoHash RKEYcuerpoHash : expression ASIGN GREATER expression\n                    | expression ASIGN GREATER expression COMMA cuerpoHash\n    getValueHash : VARIABLE LCOR expression RCORaddValueHash : VARIABLE LCOR expression RCOR ASIGN expressionmodValueHash : VARIABLE LCOR expression RCOR ASIGN expressiondeleteValueHash : VARIABLE POINT DELETE LPAR expression RPAR'
    
_lr_action_items = {'VARIABLE':([0,16,24,36,37,84,86,92,99,111,119,],[13,13,59,65,73,13,73,73,-55,-56,13,]),'IF':([0,16,84,99,111,119,],[17,17,17,-55,-56,17,]),'PUTS':([0,16,84,99,111,119,],[18,18,18,-55,-56,18,]),'TRUE':([0,16,17,20,29,30,31,32,33,36,38,44,63,64,72,82,84,87,88,89,95,99,107,111,113,119,120,],[22,22,22,22,22,-42,-43,-44,-45,22,22,22,-46,-47,22,22,22,22,22,22,22,-55,22,-56,22,22,22,]),'FALSE':([0,16,17,20,29,30,31,32,33,36,38,44,63,64,72,82,84,87,88,89,95,99,107,111,113,119,120,],[23,23,23,23,23,-42,-43,-44,-45,23,23,23,-46,-47,23,23,23,23,23,23,23,-55,23,-56,23,23,23,]),'DEF':([0,],[24,]),'NUMBER':([0,16,17,20,27,28,29,30,31,32,33,36,38,40,41,42,44,63,64,72,82,84,87,88,89,95,99,107,111,113,119,120,],[25,25,25,25,25,25,25,-42,-43,-44,-45,25,25,25,25,25,25,-46,-47,25,25,25,25,25,25,25,-55,25,-56,25,25,25,]),'STRING':([0,16,17,18,20,27,28,29,30,31,32,33,36,38,40,41,42,44,63,64,72,82,84,87,88,89,95,99,107,111,113,119,120,],[19,19,19,57,19,19,19,19,-42,-43,-44,-45,19,19,19,19,19,19,-46,-47,19,19,19,19,19,19,19,-55,19,-56,19,19,19,]),'FLOAT':([0,16,17,20,27,28,29,30,31,32,33,36,38,40,41,42,44,63,64,72,82,84,87,88,89,95,99,107,111,113,119,120,],[26,26,26,26,26,26,26,-42,-43,-44,-45,26,26,26,26,26,26,-46,-47,26,26,26,26,26,26,26,-55,26,-56,26,26,26,]),'LPAR':([0,13,16,17,20,27,28,29,30,31,32,33,36,38,40,41,42,44,59,63,64,65,72,77,82,84,87,88,89,95,99,107,111,113,119,120,],[20,37,20,20,20,20,20,20,-42,-43,-44,-45,20,20,20,20,20,20,86,-46,-47,37,20,95,20,20,20,20,20,20,-55,20,-56,20,20,20,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,14,15,19,21,22,23,25,26,57,60,61,62,66,67,68,69,70,71,74,78,79,80,81,85,93,97,101,102,104,109,110,112,114,115,116,123,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-27,-28,-31,-29,-62,-63,-30,-32,-51,-34,-35,-39,-22,-23,-24,-25,-26,-52,-60,-36,-37,-38,-57,-33,-61,-58,-40,-41,-64,-59,-48,-67,-68,-70,-49,-50,]),'PLUS':([3,14,15,19,21,22,23,25,26,45,56,58,60,61,62,66,76,78,79,80,83,85,91,96,103,108,114,118,],[27,-27,-28,-31,-29,-62,-63,-30,-32,27,27,27,-34,-35,27,27,27,-36,-37,-38,27,-33,27,27,27,27,27,27,]),'MINUS':([3,14,15,19,21,22,23,25,26,45,56,58,60,61,62,66,76,78,79,80,83,85,91,96,103,108,114,118,],[28,-27,-28,-31,-29,-62,-63,-30,-32,28,28,28,-34,-35,28,28,28,-36,-37,-38,28,-33,28,28,28,28,28,28,]),'GREATER':([3,14,15,19,21,22,23,25,26,45,56,60,61,66,78,79,80,85,105,],[30,-27,-28,-31,-29,-62,-63,-30,-32,30,30,-34,-35,30,-36,-37,-38,-33,113,]),'GREATER_OR_EQUAL':([3,14,15,19,21,22,23,25,26,45,56,60,61,66,78,79,80,85,],[31,-27,-28,-31,-29,-62,-63,-30,-32,31,31,-34,-35,31,-36,-37,-38,-33,]),'MINOR':([3,14,15,19,21,22,23,25,26,45,56,60,61,66,78,79,80,85,],[32,-27,-28,-31,-29,-62,-63,-30,-32,32,32,-34,-35,32,-36,-37,-38,-33,]),'MINOR_OR_EQUAL':([3,14,15,19,21,22,23,25,26,45,56,60,61,66,78,79,80,85,],[33,-27,-28,-31,-29,-62,-63,-30,-32,33,33,-34,-35,33,-36,-37,-38,-33,]),'ASIGN':([3,13,14,15,19,21,22,23,25,26,34,35,45,56,60,61,66,78,79,80,85,91,94,],[34,36,-27,-28,-31,-29,-62,-63,-30,-32,63,64,34,34,-34,-35,34,-36,-37,-38,-33,105,107,]),'NOT':([3,14,15,19,21,22,23,25,26,45,56,60,61,66,78,79,80,85,],[35,-27,-28,-31,-29,-62,-63,-30,-32,35,35,-34,-35,35,-36,-37,-38,-33,]),'LCOR':([13,65,],[38,89,]),'POINT':([13,],[39,]),'END':([14,15,19,21,22,23,25,26,43,45,46,47,48,49,50,51,52,53,54,57,60,61,62,66,67,68,69,70,71,74,78,79,80,83,85,93,96,98,101,102,104,110,112,114,115,116,121,123,],[-27,-28,-31,-29,-62,-63,-30,-32,81,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-51,-34,-35,-39,-22,-23,-24,-25,-26,-52,-60,-36,-37,-38,97,-33,-61,109,110,-40,-41,-64,-48,-67,-68,-70,-49,123,-50,]),'RETURN':([14,15,16,19,21,22,23,25,26,43,45,46,47,48,49,50,51,52,53,54,57,60,61,62,66,67,68,69,70,71,74,78,79,80,85,93,99,101,102,104,110,111,112,114,115,116,123,],[-27,-28,44,-31,-29,-62,-63,-30,-32,82,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-51,-34,-35,-39,-22,-23,-24,-25,-26,-52,-60,-36,-37,-38,-33,-61,-55,-40,-41,-64,-48,-56,-67,-68,-70,-49,-50,]),'RPAR':([14,15,19,21,22,23,25,26,37,58,60,61,73,75,78,79,80,85,86,100,106,108,],[-27,-28,-31,-29,-62,-63,-30,-32,74,85,-34,-35,-53,93,-36,-37,-38,-33,99,111,-54,115,]),'AND':([14,15,19,21,22,23,25,26,60,61,62,78,79,80,85,],[-27,-28,-31,-29,-62,-63,-30,-32,-34,-35,87,-36,-37,-38,-33,]),'OR':([14,15,19,21,22,23,25,26,60,61,62,78,79,80,85,],[-27,-28,-31,-29,-62,-63,-30,-32,-34,-35,88,-36,-37,-38,-33,]),'D_POINT':([14,15,19,21,22,23,25,26,55,60,61,62,78,79,80,85,101,102,117,],[-27,-28,-31,-29,-62,-63,-30,-32,84,-34,-35,-39,-36,-37,-38,-33,-40,-41,119,]),'RCOR':([14,15,19,21,22,23,25,26,60,61,76,78,79,80,85,103,],[-27,-28,-31,-29,-62,-63,-30,-32,-34,-35,94,-36,-37,-38,-33,112,]),'COMMA':([14,15,19,21,22,23,25,26,60,61,73,78,79,80,85,118,],[-27,-28,-31,-29,-62,-63,-30,-32,-34,-35,92,-36,-37,-38,-33,120,]),'RKEY':([14,15,19,21,22,23,25,26,60,61,78,79,80,85,90,118,122,],[-27,-28,-31,-29,-62,-63,-30,-32,-34,-35,-36,-37,-38,-33,104,-65,-66,]),'TIMES':([14,19,21,25,26,60,61,78,79,80,85,],[40,-31,-29,-30,-32,40,40,-36,-37,-38,-33,]),'DIVIDE':([14,19,21,25,26,60,61,78,79,80,85,],[41,-31,-29,-30,-32,41,41,-36,-37,-38,-33,]),'EXPONENTIATION':([14,19,21,25,26,60,61,78,79,80,85,],[42,-31,-29,-30,-32,42,42,-36,-37,-38,-33,]),'GETS':([36,],[71,]),'LKEY':([36,],[72,]),'DELETE':([39,],[77,]),'ELSE':([110,],[117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),'asignacion':([0,16,84,119,],[2,46,46,46,]),'expression':([0,16,17,20,29,36,38,44,72,82,84,87,88,89,95,107,113,119,120,],[3,45,56,58,62,66,76,83,91,96,45,56,56,103,108,114,118,45,91,]),'funciones':([0,],[4,]),'comparacion':([0,16,17,36,84,87,88,119,],[5,47,55,67,47,101,102,47,]),'condicional':([0,16,84,119,],[6,48,48,48,]),'impresion':([0,16,84,119,],[7,49,49,49,]),'input':([0,16,84,119,],[8,50,50,50,]),'callFuncion':([0,16,36,84,119,],[9,51,68,51,51,]),'addValueHash':([0,16,84,119,],[10,52,52,52,]),'modValueHash':([0,16,84,119,],[11,53,53,53,]),'deleteValueHash':([0,16,84,119,],[12,54,54,54,]),'term':([0,16,17,20,27,28,29,36,38,44,72,82,84,87,88,89,95,107,113,119,120,],[14,14,14,14,60,61,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'boleano':([0,16,17,20,29,36,38,44,72,82,84,87,88,89,95,107,113,119,120,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'encabezado':([0,],[16,]),'factor':([0,16,17,20,27,28,29,36,38,40,41,42,44,72,82,84,87,88,89,95,107,113,119,120,],[21,21,21,21,21,21,21,21,21,78,79,80,21,21,21,21,21,21,21,21,21,21,21,21,]),'comparador':([3,45,56,66,],[29,29,29,29,]),'cuerpo':([16,84,119,],[43,98,121,]),'diccionario':([36,],[69,]),'getValueHash':([36,],[70,]),'parametros':([37,86,92,],[75,100,106,]),'cuerpoHash':([72,120,],[90,122,]),'cond_else':([110,],[116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> asignacion','instrucciones',1,'p_instrucciones','sintactico.py',6),
  ('instrucciones -> expression','instrucciones',1,'p_instrucciones','sintactico.py',7),
  ('instrucciones -> funciones','instrucciones',1,'p_instrucciones','sintactico.py',8),
  ('instrucciones -> comparacion','instrucciones',1,'p_instrucciones','sintactico.py',9),
  ('instrucciones -> condicional','instrucciones',1,'p_instrucciones','sintactico.py',10),
  ('instrucciones -> impresion','instrucciones',1,'p_instrucciones','sintactico.py',11),
  ('instrucciones -> input','instrucciones',1,'p_instrucciones','sintactico.py',12),
  ('instrucciones -> callFuncion','instrucciones',1,'p_instrucciones','sintactico.py',13),
  ('instrucciones -> addValueHash','instrucciones',1,'p_instrucciones','sintactico.py',14),
  ('instrucciones -> modValueHash','instrucciones',1,'p_instrucciones','sintactico.py',15),
  ('instrucciones -> deleteValueHash','instrucciones',1,'p_instrucciones','sintactico.py',16),
  ('cuerpo -> asignacion','cuerpo',1,'p_body','sintactico.py',20),
  ('cuerpo -> expression','cuerpo',1,'p_body','sintactico.py',21),
  ('cuerpo -> comparacion','cuerpo',1,'p_body','sintactico.py',22),
  ('cuerpo -> condicional','cuerpo',1,'p_body','sintactico.py',23),
  ('cuerpo -> impresion','cuerpo',1,'p_body','sintactico.py',24),
  ('cuerpo -> input','cuerpo',1,'p_body','sintactico.py',25),
  ('cuerpo -> callFuncion','cuerpo',1,'p_body','sintactico.py',26),
  ('cuerpo -> addValueHash','cuerpo',1,'p_body','sintactico.py',27),
  ('cuerpo -> modValueHash','cuerpo',1,'p_body','sintactico.py',28),
  ('cuerpo -> deleteValueHash','cuerpo',1,'p_body','sintactico.py',29),
  ('asignacion -> VARIABLE ASIGN expression','asignacion',3,'p_asignacion','sintactico.py',33),
  ('asignacion -> VARIABLE ASIGN comparacion','asignacion',3,'p_asignacion','sintactico.py',34),
  ('asignacion -> VARIABLE ASIGN callFuncion','asignacion',3,'p_asignacion','sintactico.py',35),
  ('asignacion -> VARIABLE ASIGN diccionario','asignacion',3,'p_asignacion','sintactico.py',36),
  ('asignacion -> VARIABLE ASIGN getValueHash','asignacion',3,'p_asignacion','sintactico.py',37),
  ('expression -> term','expression',1,'p_expression_term','sintactico.py',42),
  ('expression -> boleano','expression',1,'p_expression_term','sintactico.py',43),
  ('term -> factor','term',1,'p_term_factor','sintactico.py',47),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactico.py',50),
  ('factor -> STRING','factor',1,'p_factor_num','sintactico.py',51),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintactico.py',52),
  ('factor -> LPAR expression RPAR','factor',3,'p_factor_expr','sintactico.py',56),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','sintactico.py',60),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','sintactico.py',63),
  ('term -> term TIMES factor','term',3,'p_term_times','sintactico.py',66),
  ('term -> term DIVIDE factor','term',3,'p_term_div','sintactico.py',69),
  ('term -> term EXPONENTIATION factor','term',3,'p_term_exp','sintactico.py',72),
  ('comparacion -> expression comparador expression','comparacion',3,'p_comparacion','sintactico.py',76),
  ('comparacion -> expression comparador expression AND comparacion','comparacion',5,'p_comparacion','sintactico.py',77),
  ('comparacion -> expression comparador expression OR comparacion','comparacion',5,'p_comparacion','sintactico.py',78),
  ('comparador -> GREATER','comparador',1,'p_comparador','sintactico.py',82),
  ('comparador -> GREATER_OR_EQUAL','comparador',1,'p_comparador','sintactico.py',83),
  ('comparador -> MINOR','comparador',1,'p_comparador','sintactico.py',84),
  ('comparador -> MINOR_OR_EQUAL','comparador',1,'p_comparador','sintactico.py',85),
  ('comparador -> ASIGN ASIGN','comparador',2,'p_comparador','sintactico.py',86),
  ('comparador -> NOT ASIGN','comparador',2,'p_comparador','sintactico.py',87),
  ('condicional -> IF comparacion D_POINT cuerpo END','condicional',5,'p_cond_if','sintactico.py',92),
  ('condicional -> IF comparacion D_POINT cuerpo END cond_else','condicional',6,'p_cond_if','sintactico.py',93),
  ('cond_else -> ELSE D_POINT cuerpo END','cond_else',4,'p_cond_else','sintactico.py',97),
  ('impresion -> PUTS STRING','impresion',2,'p_puts','sintactico.py',101),
  ('input -> VARIABLE ASIGN GETS','input',3,'p_gets','sintactico.py',104),
  ('parametros -> VARIABLE','parametros',1,'p_par_function','sintactico.py',108),
  ('parametros -> VARIABLE COMMA parametros','parametros',3,'p_par_function','sintactico.py',109),
  ('encabezado -> DEF VARIABLE LPAR RPAR','encabezado',4,'p_header_function','sintactico.py',113),
  ('encabezado -> DEF VARIABLE LPAR parametros RPAR','encabezado',5,'p_header_function','sintactico.py',114),
  ('funciones -> encabezado cuerpo END','funciones',3,'p_function','sintactico.py',118),
  ('funciones -> encabezado RETURN expression END','funciones',4,'p_function','sintactico.py',119),
  ('funciones -> encabezado cuerpo RETURN expression END','funciones',5,'p_function','sintactico.py',120),
  ('callFuncion -> VARIABLE LPAR RPAR','callFuncion',3,'p_call_function','sintactico.py',124),
  ('callFuncion -> VARIABLE LPAR parametros RPAR','callFuncion',4,'p_call_function','sintactico.py',125),
  ('boleano -> TRUE','boleano',1,'p_boolean','sintactico.py',129),
  ('boleano -> FALSE','boleano',1,'p_boolean','sintactico.py',130),
  ('diccionario -> LKEY cuerpoHash RKEY','diccionario',3,'p_hash','sintactico.py',135),
  ('cuerpoHash -> expression ASIGN GREATER expression','cuerpoHash',4,'p_body_hash','sintactico.py',138),
  ('cuerpoHash -> expression ASIGN GREATER expression COMMA cuerpoHash','cuerpoHash',6,'p_body_hash','sintactico.py',139),
  ('getValueHash -> VARIABLE LCOR expression RCOR','getValueHash',4,'p_get_hash','sintactico.py',143),
  ('addValueHash -> VARIABLE LCOR expression RCOR ASIGN expression','addValueHash',6,'p_add_hash','sintactico.py',146),
  ('modValueHash -> VARIABLE LCOR expression RCOR ASIGN expression','modValueHash',6,'p_mod_hash','sintactico.py',149),
  ('deleteValueHash -> VARIABLE POINT DELETE LPAR expression RPAR','deleteValueHash',6,'p_del_hash','sintactico.py',152),
]

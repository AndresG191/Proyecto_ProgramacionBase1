grammar Ensamblador;

OPERACION_ARITMETICA : (SUMAR | RESTAR | MULTIPLICAR | DIVIDIR) ;
fragment SUMAR       : [Ss][Uu][Mm][Aa][Rr] ;
fragment RESTAR      : [Rr][Ee][Ss][Tt][Aa][Rr] ;
fragment MULTIPLICAR : [Mm][Uu][Ll][Tt][Ii][Pp][Ll][Ii][Cc][Aa][Rr] ;
fragment DIVIDIR     : [Dd][Ii][Vv][Ii][Dd][Ii][Rr] ;

MOVER     : [Mm][Oo][Vv][Ee][Rr] ;
GUARDAR   : [Gg][Uu][Aa][Rr][Dd][Aa][Rr] ;
COMPARAR  : [Cc][Oo][Mm][Pp][Aa][Rr][Aa][Rr] ;
SI        : [Ss][Ii] ;
IR_A      : [Ii][Rr]('_'[Aa])? ;
EN        : [Ee][Nn] ;
CON       : [Cc][Oo][Nn] ;
Y         : [Yy] ;
A         : [Aa] ;

OPERADOR : [+\-*/] ;
COMPARADOR : '<=' | '>=' | '==' | '!=' | '<' | '>' ;

NUMERO : '-'? [0-9]+ ('.' [0-9]+)? ;
REGISTRO : [Rr][A-Za-z0-9]+ ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

DOS_PUNTOS : ':' ;
NEWLINE    : ('\r'? '\n')+ ;
WS         : [ \t]+ -> skip ;
COMENTARIO : '//' ~[\r\n]* -> skip ;

programa : linea* ultima_linea? EOF ;

linea
    : etiqueta? instruccion? NEWLINE
    | NEWLINE
    ;

ultima_linea
    : etiqueta? instruccion?
    ;

etiqueta : ID DOS_PUNTOS ;

instruccion
    : operacionAritmetica
    | mover
    | comparar
    | condicional
    | salto
    | guardar_inst
    ;

operacionAritmetica : OPERACION_ARITMETICA NUMERO OPERADOR NUMERO Y GUARDAR EN REGISTRO ;
mover               : MOVER NUMERO A REGISTRO ;
comparar            : COMPARAR REGISTRO CON NUMERO ;
condicional         : SI REGISTRO COMPARADOR NUMERO IR_A ID ;
salto               : IR_A ID ;
guardar_inst        : GUARDAR NUMERO EN REGISTRO ;
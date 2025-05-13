grammar Ensamblador;

OPERACION_ARITMETICA : SUMAR | RESTAR | MULTIPLICAR | DIVIDIR ;
SUMAR : [Ss] 'umar' ;
RESTAR : [Rr] 'estar' ;
MULTIPLICAR : [Mm] 'ultiplicar' ;
DIVIDIR : [Dd] 'ividir' ;

MOVER : [Mm] 'over' ;
GUARDAR : [Gg] 'uardar' ;
COMPARAR : [Cc] 'omparar' ;
SI : [Ss] 'i' ;
IR_A : [Ii] 'r_a' ;
EN : [Ee] 'n' ;
CON : [Cc] 'on' ;
DE : [Dd] 'e' ;
Y : [Yy] ;
A : [Aa] ;

OPERADOR : '+' | '-' | '*' | '/' ;
COMPARADOR : '<=' | '>=' | '==' | '!=' | '<' | '>' ;

NUMERO : '-'? [0-9]+ ('.' [0-9]+)? ;
REGISTRO : [Rr] [A-Za-z0-9]* ;
ID : [a-zA-Z_][a-zA-Z_0-9]* ;
ETIQUETA : ID ':' ;

COMA : ',' ;
NEWLINE : ('\r'? '\n')+ ;
WS : [ \t]+ -> skip ;
COMENTARIO : '//' ~[\r\n]* -> skip ;

programa : instruccion+ ;

instruccion
    : operacionAritmetica
    | mover
    | comparar
    | condicional
    | salto
    ;

operacionAritmetica
    : OPERACION_ARITMETICA NUMERO OPERADOR NUMERO Y GUARDAR EN REGISTRO
    ;

mover
    : MOVER NUMERO A REGISTRO
    ;

comparar
    : COMPARAR REGISTRO CON NUMERO
    ;

condicional
    : SI REGISTRO COMPARADOR NUMERO IR_A ID
    ;

salto
    : IR_A ID
    ;

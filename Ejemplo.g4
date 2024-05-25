grammar Ejemplo;

programa: sentencia*;

sentencia: expresion ';' | asignacion ';' | impresion ';' ;

expresion: expresion '+' expresion
         | expresion '*' expresion
         | NUMERO
         | ID
         | '(' expresion ')' 
         | '[' expresion ']' ;

asignacion: ID '=' expresion;

impresion: 'print' '(' (STRING | ID) ')' ;

NUMERO: [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
//CADENA: '"'[A-Za-z0-9_ ]+'"'
STRING: '"' .*? '"'; 
ESPACIOS: [ \n\t\r]+ -> skip;

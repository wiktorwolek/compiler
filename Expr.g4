grammar Expr;

prog: ( stat? NEWLINE )*;

stat:	write | ID '=' expr | read;

write: WRITE ID;

read: READ ID;

expr: value ADD expr | value;

value: ID | INT;	

WRITE: 'write';

READ:	'read';
   
ID:  ('a'..'z'|'A'..'Z')+;

INT: '0'..'9'+;

ADD: '+';

NEWLINE:	'\r'? '\n';

WS:   (' '|'\t')+ { skip(); };
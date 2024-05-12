grammar Expr;

prog: ( stat? NEWLINE )* '<EOF>';

stat:	write | assign | read;

assign: ID '=' expr;

write: WRITE ID;

read: READ ID;

expr:  add | value;

add: value ADD expr;

value: ID | INT;	

WRITE: 'write';

READ:	'read';
   
ID:  ('a'..'z'|'A'..'Z')+;

INT: '0'..'9'+;

ADD: '+';

NEWLINE:	'\r'? '\n';

WS:   (' '|'\t')+ -> skip;
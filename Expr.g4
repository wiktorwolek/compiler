grammar Expr;

prog: ( stat? NEWLINE)* '<EOF>';

stat: write | assign | read;

assign: ID '=' expression;

expression: expression1 | add;

expression1: expression2 | multiply;

write: WRITE ID;

read: READ ID;

add: expression1 ADD expression1;

multiply: expression2 MUL expression2;

expression2: ID | INT | '(' expression ')';

WRITE: 'write';

READ: 'read';

ID: ('a' ..'z' | 'A' ..'Z')+;

INT: '0' ..'9'+;

ADD: '+';

MUL: '*';

NEWLINE: '\r'? '\n';

WS: (' ' | '\t')+ -> skip;
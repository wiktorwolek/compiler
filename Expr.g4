grammar Expr;

prog: ( statement? NEWLINE)* '<EOF>';

statement: write | assign | read;

assign: ID '=' expression;

write: WRITE ID;

read: READ ID;

expression: expression1 | add;

expression1: expression2 | multiply;

expression2:
	INT						# int
	| REAL					# real
	| TOINT expression2		# toint
	| TOREAL expression2	# toreal
	| '(' expression ')'	# par
	| ID					# id;

add: expression1 ADDOP expression;

multiply: expression2 MULOP expression2;

divide: expression2 DIVOP expression2;

value: ID | INT;

WRITE: 'write';

READ: 'read';

TOINT: '(int)';

TOREAL: '(real)';

ID: ('a' ..'z' | 'A' ..'Z')+;

INT: '0' ..'9'+;

REAL: '0' ..'9'+ '.' '0' ..'9'+;

ADDOP: '+';

MULOP: '*';

DIVOP: '/';

NEWLINE: '\r'? '\n';

WS: (' ' | '\t')+ -> skip;
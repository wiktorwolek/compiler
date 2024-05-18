grammar Expr;

prog: ( (statement|function)? NEWLINE)* '<EOF>';

statement: write #write1| assign #assign1| read #read1| assigntable #assigntable1;

assign: ID '=' expression;

assigntable: ID '=' newtable;

newtable: '[' (tablerow';')* ']';

tablerow: (tableitem',')*;

tableitem: expression;

write: WRITE ID;

read: READ ID;

expression: expression1 | add;

expression1: expression2 | multiply | divide;

expression2:
	INT						# int
	| REAL					# real
	| TOINT expression2		# toint
	| TOREAL expression2	# toreal
	| '(' expression ')'	# par
	| id					# ids
	| CALL ID '(' ')' #call;

id: ID
	| table;
	
table: ID '[' indexes ']' | ID '[' indexes ',' indexes ']';

indexes: expression;

add: expression1 ADDOP expression;

multiply: expression2 MULOP expression2;

divide: expression2 DIVOP expression2;

function: FUNCTION fparam fblock ENDFUNCTION
;
fparam: ID
;

fblock: ( statement? NEWLINE )* 
; 

CALL: 'call'
;

FUNCTION: 'function'
;

ENDFUNCTION:	'endfunction'
;


WRITE: 'write';

READ: 'read';

TOINT: '(int)';

TOREAL: '(real)';

ID: ('a' ..'z' | 'A' ..'Z')+;

INT: '0' ..'9'+;

REAL: '0' ..'9'+ '.' '0' ..'9'+;

DIVOP: '/';

MULOP: '*';

ADDOP: '+';

NEWLINE: '\r'? '\n';

WS: (' ' | '\t')+ -> skip;
grammar Expr;

prog: block;

block: ((statement | function | struct | declStruct)? NEWLINE)*;

statement:
	write									# write1
	| assign								# assign1
	| read									# read1
	| assigntable							# assigntable1
	| IF equal THEN blockif ENDIF			# if
	| REPEAT repetitions blockrep ENDREPEAT	# loop;

equal: ID '==' expression;

blockif: block;

blockrep: block;

repetitions: expression;

assign: assignableID '=' expression;

assignableID: id | table | structref;

id: ID;

idToken: ID | table | structref;

structref: ID '.' ID;

assigntable: ID '=' newtable;

newtable: '{' (tablerow ';')* tablerow '}';

tablerow: (tableitem ',')* tableitem;

tableitem: expression;

write: WRITE expression;

read: readInt | readDouble;

readInt: READ 'int'? ID;

readDouble: READ 'real' ID;

expression: expression1 | add | substract;

expression1: expression2 | multiply | divide;

expression2:
	INT						# int
	| REAL					# real
	| STRING				# string
	| TOINT expression2		# toint
	| TOREAL expression2	# toreal
	| '(' expression ')'	# par
	| idToken				# ids
	| CALL ID '(' ')'		# call;

table: ID '[' indexes ']' | ID '[' indexes ',' indexes ']';

indexes: expression;

add: expression1 ADDOP expression;

substract: expression1 SUBOP expression1;

multiply: expression2 MULOP expression2;

divide: expression2 DIVOP expression2;

function: FUNCTION fparam fblock ENDFUNCTION;

fparam: ID;

fblock: ( statement? NEWLINE)*;

struct: STRUCT sname sblock ENDSTRUCT;

sname: ID;

sblock: ( declaration? NEWLINE)*;

declaration: declInt | declReal;

declInt: 'int' ID;

declReal: 'real' ID;

declStruct: sname ID;

// declString: 'string' INT assignableID;

REPEAT: 'repeat';

ENDREPEAT: 'endrepeat';

IF: 'if';

THEN: 'then';

ENDIF: 'endif';

CALL: 'call';

FUNCTION: 'function';

ENDFUNCTION: 'endfunction';

STRUCT: 'struct';

ENDSTRUCT: 'endstruct';

WRITE: 'write';

READ: 'read';

TOINT: '(int)';

TOREAL: '(real)';

ID: ('a' ..'z' | 'A' ..'Z')+;

INT: '0' ..'9'+;

REAL: '0' ..'9'+ '.' '0' ..'9'+;

STRING: '"' [a-zA-Z0-9 !@#$%^&*-+]* '"';

DIVOP: '/';

MULOP: '*';

ADDOP: '+';

SUBOP: '-';

NEWLINE: '\r'? '\n';

WS: (' ' | '\t')+ -> skip;
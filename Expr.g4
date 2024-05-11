grammar Expr;

prog: ( stat? NEWLINE )* 
    ;

stat:	WRITE ID		
	| ID '=' expr		
	| READ ID   		
   ;

expr: value ADD expr		
	| value			
   ;

value: ID
       | INT
   ;	

WRITE:	'write' 
   ;

READ:	'read' 
   ;
   
ID:   ('a'..'z'|'A'..'Z')+
   ;

INT:   '0'..'9'+
    ;

ADD: '+'
    ;

NEWLINE:	'\r'? '\n'
    ;

WS:   (' '|'\t')+ { skip(); }
    ;
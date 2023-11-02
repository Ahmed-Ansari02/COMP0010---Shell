grammar Expr;

command: pipe | command ';' command | call;
pipe: call '|' call | pipe '|' call;
//call: ( NONKEYWORD | quoted)*;
call:
    WHITESPACE?
    (redirection WHITESPACE)*
    argument
    (WHITESPACE atom)*
    WHITESPACE?;
WHITESPACE: [ \t]+;
//NONKEYWORD: ~[\r\n'"`;|]*;
atom: redirection | argument;
argument: (quoted | UNQUOTED)+;
UNQUOTED: ~[\t\r\n'"`|;<>]+;
redirection:
	'<' WHITESPACE? argument
	| '>' WHITESPACE? argument;
quoted: SINGLE_QUOTED | DOUBLEQUOTED | BACKQUOTED;
SINGLE_QUOTED: '\'' ~[\n']* '\'';
DOUBLEQUOTED: '"' ( BACKQUOTED | ~[\n"`]+ )* '"';
BACKQUOTED: '`' ~[\n']* '`';
WS: [ \t\r\n]+ -> skip;
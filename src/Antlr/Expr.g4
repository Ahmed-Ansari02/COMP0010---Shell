grammar Expr;

//command: 'hello';
redirection:
	'<' WHITESPACE? argument
	| '>' WHITESPACE? argument;
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
atom: redirection | argument;
argument: (quoted | UNQUOTED)*;
UNQUOTED: ~[ \t\r\n'"`|;<>]+;
quoted: SINGLE_QUOTED | DOUBLE_QUOTED | BACK_QUOTED;
SINGLE_QUOTED: '\'' ~[\n']* '\'';
DOUBLE_QUOTED: '"' ( BACK_QUOTED | ~[\n"`]+ )* '"';
BACK_QUOTED: '`' ~[\n`]* '`';
WS: [ \t\r\n]+ -> skip;
grammar ShellGrammar;

s : command EOF ;
command: pipe | command ';' command | call;
redirection:
	'<' WHITESPACE? argument
	| '>' WHITESPACE? argument;
pipe: call '|' call | pipe '|' call;
call:
	WHITESPACE? (redirection WHITESPACE)*
	argument
	(WHITESPACE (redirection | argument))* WHITESPACE?;
WHITESPACE: [ \t]+;
APPLICATION: 'echo' | 'ls' | 'grep' | 'cat';
argument: (APPLICATION | UNQUOTED | quoted)+;
UNQUOTED: ~[ \t\r\n'"`|;<>]+;
quoted: SINGLE_QUOTED | BACK_QUOTED | DOUBLE_QUOTED;
SINGLE_QUOTED: '\'' ( SINGLE_QUOTED | ~[\n']+ )* '\'';
//DOUBLE_QUOTED_BACK_QUOTES: '"' ( BACK_QUOTED | (~[\n"`]+) )* '"';
DOUBLE_QUOTED: '"' ( DOUBLE_QUOTED | (~[\n"]+) )* '"';
BACK_QUOTED: '`' ~[\n`]* '`';
//SINGLE_QUOTED: '\'' ~[\n']* '\'';

//quoted: single_quoted | back_quoted | double_quoted;
//single_quoted: SINGLE_QUOTED;
//double_quoted: DOUBLE_QUOTED_BACK_QUOTES | DOUBLE_QUOTED;
//back_quoted: BACK_QUOTED;


WS: [ \t\r\n]+ -> skip;



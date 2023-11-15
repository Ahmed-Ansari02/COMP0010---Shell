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
//quoted: SINGLE_QUOTED | BACK_QUOTED | DOUBLE_QUOTED;
SINGLE_QUOTED: '\'' (NOT_SINGLE_QUOTED)* '\'';
fragment NOT_SINGLE_QUOTED: ~[\n']+;
fragment NOT_DOUBLE_QUOTED: ~[\n"]+;
fragment NOT_BACK_QUOTED: ~[\n`]*;
fragment NOT_DOUBLE_BACK_QUOTED: ~[\n"`]+;
DOUBLE_QUOTED: '"' (NOT_DOUBLE_QUOTED)* '"' | '"' ( BACK_QUOTED | NOT_DOUBLE_BACK_QUOTED )* '"';
BACK_QUOTED: '`' NOT_BACK_QUOTED '`';

quoted: single_quoted | back_quoted | double_quoted;
single_quoted: SINGLE_QUOTED;
double_quoted: '"' (DOUBLE_QUOTED | UNQUOTED)+ '"' | DOUBLE_QUOTED;
back_quoted: BACK_QUOTED;


WS: [ \t\r\n]+ -> skip;



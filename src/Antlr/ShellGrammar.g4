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
SINGLE_QUOTED: '\'' ~[\n']* '\'';
DOUBLE_QUOTED: '"' ( BACK_QUOTED | (~[\n"`]+) )* '"';
BACK_QUOTED: '`' ~[\n`]* '`';
WS: [ \t\r\n]+ -> skip;
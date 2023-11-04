grammar ShellGrammar;

redirection:
	'<' WHITESPACE? argument
	| '>' WHITESPACE? argument;
command: pipe | command ';' command | call;
pipe: call '|' call | pipe '|' call;
call:
	WHITESPACE? (redirection WHITESPACE)* argument (
		WHITESPACE atom
	)* WHITESPACE?;
WHITESPACE: [ \t]+;
atom: redirection | argument;
APPLICATION: 'echo' | 'ls' | 'grep' | 'cat';
argument: (quoted | UNQUOTED | APPLICATION)+;
UNQUOTED: ~[ \t\r\n'"`|;<>]+;
quoted: SINGLE_QUOTED | DOUBLE_QUOTED | BACK_QUOTED;
SINGLE_QUOTED: '\'' ~[\n']* '\'';
DOUBLE_QUOTED: '"' ( BACK_QUOTED | ~[\n"`]+)* '"';
BACK_QUOTED: '`' ~[\n`]* '`';
WS: [ \t\r\n]+ -> skip;
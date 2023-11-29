grammar ShellGrammar;

s: command EOF;
command: pipe | command ';' command | call;
redirection:
	'<' WHITESPACE? argument
	| '>' WHITESPACE? argument;
pipe: call '|' call | pipe '|' call;
call:
	WHITESPACE? (redirection WHITESPACE)* argument (
		WHITESPACE (redirection | argument)
	)* WHITESPACE?;
WHITESPACE: [ \t]+;
// APPLICATION: 'echo' | 'ls' | 'grep' | 'cat';
argument: (UNQUOTED | quoted)+;
UNQUOTED: ~[ \t\r\n'"`|;<>]+;
fragment NOT_QUOTED: ~[\n"'`]+;
fragment NOT_SINGLE_QUOTED: ~[\n']+;
fragment NOT_DOUBLE_QUOTED: ~[\n"]+;
fragment NOT_BACK_QUOTED: ~[\n`]+;
fragment NOT_DOUBLE_BACK_QUOTED: ~[\n"`]+;
fragment QUOTED: SINGLE_QUOTED | DOUBLE_QUOTED | BACK_QUOTED;
quoted: SINGLE_QUOTED | BACK_QUOTED | DOUBLE_QUOTED;
SINGLE_QUOTED: '\'' (SINGLE_QUOTED | NOT_SINGLE_QUOTED)* '\'';
DOUBLE_QUOTED: '"' (DOUBLE_QUOTED | NOT_DOUBLE_QUOTED)* '"';
//DOUBLE_BACK_QUOTED: '"' (BACK_QUOTED | NOT_DOUBLE_BACK_QUOTED)* '"';
BACK_QUOTED: '`' (BACK_QUOTED | NOT_BACK_QUOTED)* '`';
//
// quoted: single_quoted | back_quoted | double_quoted; single_quoted: '\'' (NOT_QUOTED | WHITESPACE
// | quoted)* '\''; double_quoted: '"' (NOT_QUOTED | WHITESPACE | quoted)* '"'; back_quoted: '`'
// (NOT_QUOTED | WHITESPACE | quoted)* '`';

WS: [ \t\r\n]+ -> skip;
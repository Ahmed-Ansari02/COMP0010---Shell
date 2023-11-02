grammar Expr;
program: command*;
command: pipe | command ';' command | call;
pipe: call '|' call | pipe '|' call;
call:
	whitespace? (redirection whitespace)* argument (
		whitespace atom
	)* whitespace?;
whitespace: 'a';
atom: redirection | argument;
argument: (quoted | unquoted)+;
redirection:
	'<' whitespace? argument
	| '>' whitespace? argument;
quoted: singlequoted | doublequoted | backquoted;
singlequoted: '\'' ~('\n' | '\'')* '\'';
doublequoted: '"' ( backquoted | doublequotecontent)* '"';
doublequotecontent: ~('\n' | '"' | '`');
backquoted: '`' ~('\n' | '\'')* '`';
// nonkeyword: ~[\r\n'"`|;]+;

unquoted:
	~(
		'\t'
		| '\r'
		| '\n'
		| '\''
		| '"'
		| '`'
		| ';'
		| '|'
		| '<'
		| '>'
	)+;
application: 'echo' | 'ls' | 'grep' | 'cat';
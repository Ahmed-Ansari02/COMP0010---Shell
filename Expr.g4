grammar Expr;		

program: command*;

command: simpleCommand
       | simpleCommand OPERATOR command;

simpleCommand: CMD+ (arg)*;

arg: STRING | UNQUOTED_STRING;

OPERATOR : '>'|'|'|';';

CMD: 'echo'|'ls'|'grep'|'cat';

UNQUOTED_STRING: [a-zA-Z0-9_]+;

STRING: '"' ~["]* '"';

WS: [ \t\r\n]+ -> skip;

grammar Expr;		

program: command*;

command: simpleCommand
       | simpleCommand OPERATOR command;

simpleCommand: CMD+ (arg)*;

arg: STRING | UNQUOTED_STRING|FIlE;

OPERATOR : '>'|'|'|';';

CMD: 'echo'|'ls'|'grep'|'cat'|'cd';

UNQUOTED_STRING: [a-zA-Z0-9_]+;

FIlE: ([a-zA-Z0-9_]+'.'[a-zA-Z0-9_]+);

STRING: '"' ~["]* '"';

WS: [ \t\r\n]+ -> skip;

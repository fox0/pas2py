grammar Pascal;

program:
    variableDeclarationPart block DOT;

variableDeclarationPart:
    'var' variableDeclaration (SEMI variableDeclaration)* SEMI;

variableDeclaration:
    identifierList COLON varType;

identifierList:
    ID (COMMA ID)*;

varType:
    ('integer' | 'int64');

block:
    'begin' statements SEMI 'end';

statements:
    statement (SEMI statement)*;

statement:
      writelnReadln
    | block
    //| callFunction
    | assignmentStatement
    | ifStatement
    ;

writelnReadln:
    'writeln' LPAREN CONST_STR RPAREN SEMI
    'readln' LPAREN ID RPAREN;

assignmentStatement:
    ID ASSIGN expression;

expression:
    (LPAREN expression RPAREN | CONST_INT | ID) (operators expression)*;

operators:
    EQUAL | NOT_EQUAL | LT | LE | GE | GT | DIV | PLUS | MINUS | STAR | SLASH;

ifStatement:
    'if' expression 'then' statement ('else' statement)*;


ID: [a-zA-Z][a-zA-Z0-9_]*;
CONST_INT: [0-9]+;
CONST_STR: '\'' ('\'\'' | ~ ('\''))* '\'';

WS: [ \t\r\n]+ -> skip;
COMMENT1: '(*' .*? '*)' -> skip;
COMMENT2: '{' .*? '}' -> skip;

SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
ASSIGN: ':=';

EQUAL: '=';
NOT_EQUAL: '<>';
LT: '<';
LE: '<=';
GE: '>=';
GT: '>';

DIV: '//';
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';

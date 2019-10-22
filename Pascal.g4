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
    'begin'
    callFunction SEMI //todo
    'end'
    ;

callFunction:
    ID LPAREN parameterList RPAREN;

parameterList:
    ID (COMMA ID)*;


ID: [a-zA-Z][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;

SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';

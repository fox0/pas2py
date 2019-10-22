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
    block | callFunction | assignmentStatement | if_;

callFunction:
    ID LPAREN parameterList RPAREN;

parameterList:
    ID (COMMA ID)*;

assignmentStatement:
    ID ASSIGN expression;

expression:
    factor (operator expression)?;

factor:
    ID | CONST_INT | LPAREN expression RPAREN;

operator:
    PLUS | MINUS | STAR | SLASH | 'div' | 'mod';  //todo + <=

if_:
    'if' expression statement 'else' statement SEMI;


ID: [a-zA-Z][a-zA-Z0-9_]*;
CONST_INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;

SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
ASSIGN: ':=';

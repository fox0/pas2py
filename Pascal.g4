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
    'begin' statements SEMI? 'end';

statements:
    statement (SEMI statement)*;

statement:
    writelnReadln
    | readln
    | writeln
    | block
    | assignmentStatement
    | ifStatement
    | whileStatement
    ;

writelnReadln:
    'writeln' LPAREN CONST_STR RPAREN SEMI
    'readln' LPAREN ID RPAREN;

readln:
    'readln' LPAREN identifierList RPAREN;

writeln:
    'writeln' LPAREN expressions RPAREN;

assignmentStatement:
    ID ASSIGN expression;

expressions:
    expression (COMMA expression)*;

expression:
    (LPAREN expression RPAREN | CONST_INT | CONST_STR | ID) (operators expression)*;

operators:
    EQUAL | NOT_EQUAL | LT | LE | GE | GT | OR | AND | DIV | MOD | PLUS | MINUS | STAR | SLASH;

ifStatement:
    'if' expression 'then' (block|blockBody) elseStatement?;

elseStatement:
    'else' (block|blockBody);

whileStatement:
    'while' expression 'do' (block|blockBody);

blockBody:
    statement;

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
OR: 'or';
AND: 'and';

PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';

DIV: '//';
MOD: '%';

ID: [a-zA-Z][a-zA-Z0-9_]*;
CONST_INT: [0-9]+;
CONST_STR: '\'' ('\'\'' | ~ ('\''))* '\'';
WS: [ \t\r\n]+ -> skip;
COMMENT1: '(*' .*? '*)' -> skip;
COMMENT2: '{' .*? '}' -> skip;

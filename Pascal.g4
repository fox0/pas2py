grammar Pascal;

program:
    ('program' ID SEMI)? variableDeclarationPart blockStatement DOT;

variableDeclarationPart:
    'var' variableDeclaration (SEMI variableDeclaration)* SEMI;

variableDeclaration:
    identifierList COLON varType;

identifierList:
    ID (COMMA ID)*;

varType:
    ('byte' | 'longint' | 'integer' | 'int64' | 'real' | 'string' | 'boolean');

blockStatement:
    'begin' statements SEMI? 'end';

// нужно для правильных отступов в питоне
fakeblockStatement:
    statement;

statements:
    statement (SEMI statement)*;

statement:
    blockStatement
    | assignmentStatement
    | ifStatement
    | whileStatement
    | forStatement
    | breakStatement
    | writelnReadln
    | readln
    | writeln
    | write
    ;

writelnReadln:
    'writeln' LPAREN CONST_STR RPAREN SEMI
    'readln' LPAREN ID RPAREN;

readln:
    'readln' LPAREN identifierList RPAREN;

writeln:
    'writeln' LPAREN expressions RPAREN;

write:
    'write' LPAREN expressions RPAREN;

assignmentStatement:
    ID ASSIGN expression;

expressions:
    expression (COMMA expression)*;

expression:
    ( LPAREN expression RPAREN
    | CONST_INT
    | CONST_STR
    | ID
    | ID LPAREND expression RPAREND
    ) (operators expression)*;

operators:
    EQUAL | NOT_EQUAL | LT | LE | GE | GT | OR | AND | DIV | MOD | PLUS | MINUS | STAR | SLASH;

ifStatement:
    'if' expression 'then' (blockStatement | fakeblockStatement) elseStatement?;

elseStatement:
    'else' (blockStatement | fakeblockStatement);

whileStatement:
    'while' expression 'do' (blockStatement | fakeblockStatement);

forStatement:
    'for' ID ASSIGN expression 'to' expression 'do' (blockStatement | fakeblockStatement);

breakStatement:
    'break';

SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
LPAREND: '[';
RPAREND: ']';

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

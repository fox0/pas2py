grammar Pascal;

program:
    variableDeclarationPart;

variableDeclarationPart:
    'var' variableDeclaration (SEMI variableDeclaration)* SEMI;

variableDeclaration:
    identifierList COLON ('integer' | 'int64');

identifierList:
    ID (COMMA ID)*;


ID: [a-zA-Z][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;

SEMI: ';';
COLON: ':';
COMMA: ',';

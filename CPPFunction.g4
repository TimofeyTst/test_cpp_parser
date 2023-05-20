grammar CPPFunction;

// Parser rules
function: type_specifier identifier '(' parameter_list ')' compound_statement;

type_specifier: 'int' | 'char' | 'float' | 'double';

identifier: ID;

parameter_list: parameter (',' parameter)*;

parameter: type_specifier identifier;

compound_statement: '{' (declaration | statement)* '}';

declaration: type_specifier identifier_list ';';

identifier_list: identifier (',' identifier)*;

statement: assignment_statement ';';

assignment_statement: identifier '=' expression;

expression: identifier | INT_CONST;

// Lexer rules
ID: [a-zA-Z_][a-zA-Z_0-9]*;

INT_CONST: [0-9]+;

WS: [ \t\r\n]+ -> skip;

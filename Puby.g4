grammar Puby;

// --- Entrada ---
programa
    : comando* EOF
    ;

// --- Comandos ---
comando
    : escrita
    | leitura
    | atribuicao
    | condicional
    | enquanto
    | laco_para
    | incremento
    ;

// --- Saída: puts expr[, expr]* ---
escrita
    : PUTS (expressao (',' expressao)*)?
    ;

// --- Entrada: x = gets ---
leitura
    : ID '=' GETS
    ;

// --- Atribuição: x = expr ---
atribuicao
    : ID '=' expressao
    ;

// --- if / elsif / else / end ---
condicional
    : IF condicao corpo_if (ELSIF condicao corpo_if)* (ELSE corpo_if)? END
    ;

corpo_if
    : comando*
    ;

// --- while (do opcional) ... end ---
enquanto
    : WHILE condicao (DO)? comando* END
    ;

// --- for/in (do opcional) ... end ---
laco_para
    : FOR ID IN intervalo (DO)? comando* END
    ;

intervalo
    : expressao RANGE expressao
    ;

// --- Pós-incremento/decremento ---
incremento
    : ID (OP_INC | OP_DEC)
    ;

// --- Condição é expressão ---
condicao
    : expressao
    ;

// --- Expressões (LL(1), fatoradas) ---
expressao
    : logico_baixo
    ;

// logico_baixo  =>  not_baixo ( (and|or) not_baixo )*
logico_baixo
    : not_baixo logico_baixo_suf
    ;

logico_baixo_suf
    : AND_WORD not_baixo logico_baixo_suf
    | OR_WORD  not_baixo logico_baixo_suf
    | /* vazio */
    ;

// not_baixo  =>  NOT not_baixo | logico_alto
not_baixo
    : NOT not_baixo
    | logico_alto
    ;

// logico_alto  =>  rel ( (&&| ||) rel )*
logico_alto
    : rel logico_alto_suf
    ;

logico_alto_suf
    : AND_SYM rel logico_alto_suf
    | OR_SYM  rel logico_alto_suf
    | /* vazio */
    ;

// rel  =>  soma ( OP_REL soma )*
rel
    : soma (OP_REL soma)*
    ;

// soma  =>  mult ( (+|-) mult )*
soma
    : mult (OP_ADD mult)*
    ;

// mult  =>  unario ( (*|/) unario )*
mult
    : unario (OP_MUL unario)*
    ;

// unario  =>  !unario | (+|-)unario | primario
unario
    : OP_NOT unario
    | OP_ADD unario
    | primario
    ;

// primario  =>  NUM | STRING | ID | (expressao)
primario
    : NUM
    | STRING
    | ID
    | '(' expressao ')'
    ;

// --- Palavras-chave ---
IF          : 'if';
ELSIF       : 'elsif';
ELSE        : 'else';
END         : 'end';
WHILE       : 'while';
FOR         : 'for';
IN          : 'in';
DO          : 'do';
PUTS        : 'puts';
GETS        : 'gets';
NOT         : 'not';
AND_WORD    : 'and';
OR_WORD     : 'or';
AND_SYM     : '&&';
OR_SYM      : '||';

// --- Operadores ---
OP_INC      : '++';
OP_DEC      : '--';
OP_ADD      : '+' | '-' ;
OP_MUL      : '*' | '/' ;
OP_REL      : '>=' | '<=' | '==' | '!=' | '>' | '<' ;
OP_NOT      : '!';
RANGE       : '..' | '...';

// --- Identificadores e literais ---
ID          : [a-zA-Z_] [a-zA-Z0-9_]* ;
NUM         : [0-9]+ ('.' [0-9]+)? ;
STRING      : '"' ( ~["\\\r\n] | '\\' . )* '"' ;

// --- Espaços em branco ---
WS          : [ \t\r\n]+ -> skip ;

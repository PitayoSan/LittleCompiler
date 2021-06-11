import plylex
import ply.yacc as yacc

from tree import Node
from plylex import literals, tokens


def p_block(p):
    '''
    block : stmt ';' block
        | stmt ';'
    '''
    if len(p) == 4:
        p[0] = Node('block', children=[p[1], p[3]])
    else:
        p[0] = p[1]


def p_block_ctrl(p):
    '''
    block : loop block
        | cond block
        | loop
        | cond
    '''
    if len(p) == 3:
        p[0] = Node('block', children=[p[1], p[2]])
    else:
        p[0] = p[1]


def p_stmt(p):
    '''
    stmt : ID '=' expr
        | expr
        | decl
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('ass', children=[Node(p[1]), p[3]])


def p_expr(p):
    '''
    expr : strexpr
        | numexpr
        | boolexpr
    '''
    p[0] = p[1]


def p_strexpr(p):
    '''
    strexpr : strexpr '+' strexpr
    '''
    p[0] = Node(p[2], children=[p[1], p[3]])


def p_strexpr_const(p):
    '''
    strexpr : SCONST
        | ID
    '''
    p[0] = Node(p[1])


def p_numexpr(p):
    '''
    numexpr : number
        | numexpr '+' numexpr
        | numexpr '-' numexpr
        | numexpr '*' numexpr
        | numexpr '/' numexpr
        | numexpr '^' numexpr
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node(p[2], children=[p[1], p[3]])


def p_number(p):
    '''
    number : ICONST
        | FCONST
        | ID
    '''
    p[0] = Node(p[1])


def p_boolexpr(p):
    '''
    boolexpr : boolval
        | boolcomp
        | boolexpr AND boolexpr
        | boolexpr OR boolexpr
        | '(' boolexpr AND boolexpr ')'
        | '(' boolexpr OR boolexpr ')'
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = Node(p[2], children=[p[1], p[3]])
    else:
        p[0] = Node(p[3], children=[p[2], p[4]])


def p_boolval(p):
    '''
    boolval : ID
        | TRUE
        | FALSE
    '''
    p[0] = Node(p[1])


def p_boolcomp(p):
    '''
    boolcomp : number EQUAL number
        | number NEQUAL number
        | number '>' number
        | number '<' number
        | number LEQT number
        | number MEQT number
        | strexpr EQUAL strexpr
        | strexpr NEQUAL strexpr
    '''
    p[0] = Node(p[2], children=[p[1], p[3]])


def p_decl(p):
    '''
    decl : numdecl
        | strdecl
        | booldecl
    '''
    p[0] = p[1]


def p_numdecl(p):
    '''
    numdecl : INT ID
        | FLOAT ID
        | INT ID '=' numexpr
        | FLOAT ID '=' numexpr
    '''
    if len(p) == 3:
        p[0] = Node('decl', children=[Node(p[1]), Node(p[2])])
    else:
        ass = Node('ass', children=[Node(p[2]), p[4]])
        p[0] = Node('decl', children=[Node(p[1]), ass])


def p_strdecl(p):
    '''
    strdecl : STRING ID
        | STRING ID '=' strexpr
    '''
    if len(p) == 3:
        p[0] = Node('decl', children=[Node(p[1]), Node(p[2])])
    else:
        ass = Node('ass', children=[Node(p[2]), p[4]])
        p[0] = Node('decl', children=[Node(p[1]), ass])


def p_booldecl(p):
    '''
    booldecl : BOOLEAN ID
        | BOOLEAN ID '=' boolexpr
    '''
    if len(p) == 3:
        p[0] = Node('decl', children=[Node(p[1]), Node(p[2])])
    else:
        ass = Node('ass', children=[Node(p[2]), p[4]])
        p[0] = Node('decl', children=[Node(p[1]), ass])


def p_cond(p):
    '''
    cond : IF boolblock braceb
        | IF boolblock braceb ELSE braceb
        | IF boolblock braceb condelif ELSE braceb
    '''
    if len(p) == 4:
        p[0] = Node('if', children=[p[2], p[3]])
    elif len(p) == 6:
        p[0] = Node('if', children=[p[2], p[3], p[5]])
    else:
        p[0] = Node('if', children=[p[2], p[3], p[4], p[6]])


def p_condelif(p):
    '''
    condelif : ELIF boolblock braceb
        | ELIF boolblock braceb condelif
    '''
    if len(p) == 4:
        p[0] = Node('elif', children=[p[2], p[3]])
    else:
        p[0] = Node('elif', children=[p[2], p[3], p[4]])


def p_boolblock(p):
    '''
    boolblock : '(' boolexpr ')'
    '''
    p[0] = p[2]


def p_braceb(p):
    '''
    braceb : '{' block '}'
    '''
    p[0] = p[2]


def p_loop(p):
    '''
    loop : forctrl
        | whilectrl
        | dowhilectrl
    '''
    p[0] = p[1]


def p_forctrl(p):
    '''
    forctrl : FOR forcond braceb
    '''
    p[0] = Node('for', children=[p[2], p[3]])


def p_forcond(p):
    '''
    forcond : '(' stmt ';' stmt ';' stmt ')'
    '''
    p[0] = Node('forcond', children=[p[2], p[4], p[6]])


def p_whilectrl(p):
    '''
    whilectrl : WHILE boolblock braceb
    '''
    p[0] = Node('while', children=[p[2], p[3]])


def p_dowhilectrl(p):
    '''
    dowhilectrl : DO braceb WHILE boolblock ';'
    '''
    p[0] = Node('dowhile', children=[p[4], p[2]])


def p_error(p):
    if hasattr(p, 'value'):
	    print(f'Syntax error at {p.value!r}')
    else:
        print('Syntax error')


parser = yacc.yacc()
output = parser.parse(lexer=plylex.lexer, input=open("input.txt").read())
print(output)

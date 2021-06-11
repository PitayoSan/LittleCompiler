import ply.lex as lex


# Tokens
reserved = (
	'IF', 'ELSE', 'ELIF', 'WHILE', 'DO', 'FOR',
	'INT', 'FLOAT', 'STRING', 'BOOLEAN',
	'AND', 'OR', 'TRUE', 'FALSE'
)

tokens = reserved + (
	'ID', 'ICONST', 'FCONST', 'SCONST',
	'EQUAL', 'NEQUAL', 'LEQT', 'MEQT'
)

literals = [
	'+',
	'-',
	'*',
	'/',
	'^',
	'=',
	'<',
	'>',
	'(',
	')',
	'{',
	'}',
	';',
	'"'
]

t_ignore = ' \t\x0c'
t_EQUAL 		= r'=='
t_NEQUAL 		= r'!='
t_LEQT 		= r'<='
t_MEQT 		= r'>='


reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r


def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


def t_error(t):
	print('Illegal character "%s"' % t.value[0])
	t.lexer.skip(1)


t_ICONST = r'-?\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
t_FCONST = r'-?((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'


lexer = lex.lex()

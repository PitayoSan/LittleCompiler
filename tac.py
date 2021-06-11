from tree import Node


def make_tac(node):
	stack = []
	lines = []
	counter = 0
	lines = traverse_tree(node, counter, stack, lines)


	with open('tac.txt', 'w') as tac_file:
		headers = ' Identifiers    | Op             | Arg1           | Arg2           \n'
		tac_file.write(headers)
		for raw_line in lines:
			line = '{:>15} | {:>15} | {:>15} | {:>15}\n'.format(line[:])
			tac_file.write(line + '\n')


def traverse_tree(node, counter, stack, lines):
	if len(node.children) > 0:
		for child in node.children:
			lines, counter = traverse_tree(child, counter, stack, lines)
	lines, counter = make_new_line(node, counter, lines)
	return lines, counter


def make_new_line(node, counter, lines):
	value = node.value
	parent = node.parent
	if value == 'block':
		new_line = []
	elif value == 'ass':
		new_line = ['=', f't{counter - 1}', f't{counter - 2}']
	elif value == 'decl':
		new_line = ['=', f't{counter - 1}', f't{counter - 2}']
	elif value == 'if':
		new_line = []
	elif value == 'elif':
		new_line = []
	elif value == 'else':
		new_line = []
	elif value == 'for':
		new_line = []
	elif value == 'forcond':
		new_line = []
	elif value == 'while':
		new_line = []
	elif value == 'dowhile':
		new_line = []
	elif value.isnumeric() or value.isfloat() or isinstance(value, str):
		lines.append(['=', f't{counter}', value])
		counter += 1
	else:
		new_line = []
	return lines, counter

def isfloat(n):
	try:
		float(n)
		return True
	except ValueError:
		return False

import re
nf = open('cprogComments.c', 'w')
f = open("cprog.c", 'r')

for line in f:
	line_parts = line.split('\n')

	if not line.strip():
		print 'Handling newlines or blank lines'
		pass
	elif re.search(r'(//|/\*|\*/|\*)', line):
		print 'Handling comments'
		pass
	elif re.search(r'#define', line):
		print 'Handling define'
		line_parts[1] = "// Define the constant"
	elif re.search(r'(int|float|bool|double).*=', line):
		print 'Handling declare + init'
		line_parts[1] = "// Define and declare a variable"
	elif re.search(r'=', line):
		print 'Handling assignment'
		line_parts[1] = '// Set the variable to a new value'
	elif re.search(r'^\s*(int|float|bool|double|void).*\(.*\)', line):
		print 'Handling function block comment'
		line_parts = ['/*\n', '*Create a new function to do a useful task\n', '*/\n'] + line_parts
	elif re.search(r'printf', line):
		print 'Handling print'
		line_parts[1] = '// Output the expression to the console'
	elif re.search(r'return', line):
		print 'Handling return'
		line_parts[1] = '// Return the value'
	else:
		pass

	print line_parts
	nf.write(' '.join(line_parts) + '\n')
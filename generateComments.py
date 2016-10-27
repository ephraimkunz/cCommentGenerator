import re
import sys
import os

allowed_file_extensions = ['.c', '.h']
output_change = '_commented'

def add_comments(in_filename, out_filename):
	of = open(in_filename, 'r')
	nf = open(out_filename, 'w')

	for line in of:
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

		#print line_parts
		nf.write(' '.join(line_parts) + '\n')

def main():
	files_to_process = []
	output_files = []
	num_args = len(sys.argv)

	if num_args == 1: # Generate comments for all files in directory with correct .c and .h extension
		files_to_process = [f for f in os.listdir('.') if os.path.isfile(f) and os.path.splitext(f)[-1] in allowed_file_extensions]
		output_files = [os.path.splitext(f)[0] + output_change + os.path.splitext(f)[-1] for f in files_to_process]
	elif num_args == 2: #Generate comments for given file
		files_to_process = [sys.argv[1]]
		if os.path.splitext(files_to_process[0])[-1] in allowed_file_extensions:
			output_files = [os.path.splitext(files_to_process[0])[0] + output_change + os.path.splitext(files_to_process[0])[-1]]
	elif num_args == 3: #Generate comments for first file, storing results in file name of second file
		files_to_process = [sys.argv[1]]
		output_files = [sys.argv[2]]

	#Now start the real work
	print files_to_process, output_files
	for i in range(len(files_to_process)):
		add_comments(files_to_process[i], output_files[i])


main()
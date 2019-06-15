# cli.py
# Import the argparse library
import argparse
import os 
import sys


# create the parser
my_parser = argparse.ArgumentParser(
	description='List the content of a folder',
	epilog='Enjoy the program! :)',
	prefix_chars='/')
# Add the arguments
my_parser.add_argument('Path',
						metavar='path',
						type=str,
						help='the path to list')
# Execut the parse_arg() method
args = my_parser.parse_args()

input_path = args.Path



if not os.path.isdir(input_path):
	print('The path specified does not exist')
	sys.exit()

print('\n'.join(os.listdir(input_path)))
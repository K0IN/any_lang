#!/usr/bin/env python3
import ast
import compiler
import argparse

parser = argparse.ArgumentParser(
    prog='AnyCompiler',
    description='Compiles a set of files into a python ast')

parser.add_argument('input_files', type=argparse.FileType('r'), nargs='+')
parser.add_argument('-o', '--out')

args = parser.parse_args()
print(args)

results = [compiler.compile_file(file) for file in args.input_files]


if len(results) > 1:
    result = "\n".join(results)
else:
    result = results[0]

if args.out:
    with open(args.out, 'w') as f:
        f.write(result)
else:
    print(results)

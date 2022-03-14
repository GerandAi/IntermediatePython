'''
This is just like python_ex2.py, except now we print a specific argument from
the sys.argv list.

Note that this will result in an error if you try to access a position in the
list that does not exit (if you try to access the argument at index 1, but
there is noe argument at index 1.)

Try running the script with:
python python_ex3.py 'hello' 'world'

To see the error that will occur if not enough arguments are passed, try:
python python_ex3.py 'hello' 'world'
'''
import sys

print(__doc__)

print(sys.argv[1])

print(sys.argv[2])

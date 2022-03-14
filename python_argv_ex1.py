'''
This is a simple script that helps us understand how we can use sys package to
access command line arguments.
Later we will learn about the argparse package.

First we import sys, then we use sys.argv to acess the commandl line arguments.

Also, we learn that this string - the one you are reading right now - is
called a docstring. It is defined between the triple quotes and is at the top
of the script.  It is automatically stored in the "__doc__" variable when the
script is run.  We can access it by printing the __doc__ variable like we do
below.
'''
import sys

print(__doc__)

print(sys.argv)

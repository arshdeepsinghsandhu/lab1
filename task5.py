def do_twice(f, x):
	f(x)
	f(x)

def print_twice(x):
	print (x)

def do_four(*p):
	do_twice(*p)
	do_twice(*p)

do_twice(print_twice, "Arsh")
do_four(print_twice, "Sandhu")

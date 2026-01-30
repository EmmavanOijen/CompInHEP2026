.cc.o:
	g++ -c $<

all: output

output: hello_world.o
	g++ hello_world.o -o output

# Remove all files except source files and the Makefile.
FILETYPES = *.o *.txt

clean:
	rm -f $(FILETYPES)

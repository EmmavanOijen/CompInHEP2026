all: library test

library: libMET.so

libMET.so: METclass.o
	g++ -shared -o libMET.so METclass.o

METclass.o: METclass.cc METclass.h
	g++ -fPIC -c METclass.cc

test:
	g++ test.cc -L. -lMET -o output
	LD_LIBRARY_PATH=. ./output

clean:
	rm -f *.o output

cleanAll: clean
	rm -f libMET.so

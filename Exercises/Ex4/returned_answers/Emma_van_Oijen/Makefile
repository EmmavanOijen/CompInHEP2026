all: library test

library: libtrack.so libidentity.so

libtrack.so: trackclass.o
	g++ -shared -o libtrack.so trackclass.o

trackclass.o: trackclass.cpp trackclass.h
	g++ -fPIC -c trackclass.cpp

libidentity.so: identityclass.o libtrack.so
	g++ -shared -o libidentity.so identityclass.o -L. -ltrack

identityclass.o: identityclass.cpp identityclass.h
	g++ -fPIC -c identityclass.cpp

test:
	g++ test.cpp -L. -lidentity -ltrack -o output
	LD_LIBRARY_PATH=. ./output

clean:
	rm -f *.o output

cleanAll: clean
	rm -f *.so

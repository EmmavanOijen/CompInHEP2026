#Note: use "make" to create executables of the two .cpp files,
#use "make createPlot" to create the plot using the two executables and
#use "make PyROOT" to create the plot using the Python files.

files = $(wildcard *.cpp)
OBJS = $(addsuffix .o,$(basename $(files)))

OPT = -O -Wall -fPIC

ROOTINC := $(shell root-config --cflags)
ROOTLIBS := $(shell root-config --glibs)
INC = -I. $(ROOTINC)

.cpp.o:
	$(CXX) $(OPT) $(INC) -c $*.cpp

all: compile executable

compile: $(OBJS)

executable: tree.o plot.o
	 $(CXX) -O tree.o -o tree $(ROOTLIBS)
	 $(CXX) -O plot.o -o plot $(ROOTLIBS)

createPlot:
	./tree
	./plot

PyROOT:
	python3 tree.py
	python3 plot.py

clean:
	rm -f *.o *.~

cleanAll: clean
	rm -f *.png tree plot *.root

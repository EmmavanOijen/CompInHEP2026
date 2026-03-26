PYTHIA8_URL = https://pythia.org/download/pythia83/pythia8317.tgz
PYTHIA8_TGZ = $(notdir $(PYTHIA8_URL))
PYTHIA8_DIR = $(basename $(PYTHIA8_TGZ))

OPT = -O2 -std=c++11 -pedantic -W -Wall -Wshadow -fPIC
INC = -I$(PYTHIA8_DIR)/include
LIBS = -L$(PYTHIA8_DIR)/lib -lpythia8 -ldl

SRC = $(wildcard *.cpp)
OBJS = $(addsuffix .o,$(basename $(SRC)))

.cpp.o:
	$(CXX) $(OPT) $(INC) -c -o $@ $<

$(PYTHIA8_DIR):
	wget $(PYTHIA8_URL)
	tar xfvz $(PYTHIA8_TGZ)
	cd $(PYTHIA8_DIR) && ./configure && make -j 8

all:
	$(MAKE) $(PYTHIA8_DIR)

compile: $(OBJS)

datageneration: $(OBJS) $(PYTHIA8_DIR)
	$(CXX) $(OPT) $(INC) $(OBJS) $(LIBS) -o datageneration

job:
	echo '#!'`which bash` > test.job
	echo 'export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH):$(PYTHIA8_DIR)/lib' >> test.job
	echo 'export PYTHIA8DATA=$(PWD)/pythia8317/share/Pythia8/xmldoc' >> test.job
	echo './datageneration' >> test.job
	chmod +x test.job

clean:
	rm -f *.o *.~ datageneration test.job

cleanAll: clean
	rm -rf *.png *.pdf *.C pythia* *.txt

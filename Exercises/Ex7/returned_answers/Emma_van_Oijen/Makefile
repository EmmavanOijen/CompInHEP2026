PYTHIA8_URL = https://pythia.org/download/pythia83/pythia8317.tgz
PYTHIA8_TGZ = $(notdir $(PYTHIA8_URL))
PYTHIA8_DIR = $(basename $(PYTHIA8_TGZ))

LHAPDF_URL = http://www.hepforge.org/archive/lhapdf/LHAPDF-6.5.6.tar.gz
LHAPDF_TGZ = $(notdir $(LHAPDF_URL))
LHAPDF_DIR = $(basename $(basename $(LHAPDF_TGZ)))

GARBAGE = $(wildcard *~ *.o *.a *.so pythia_simulation pythia8* *.job)

PDFDIR = $(PWD)/LHAPDF
PDFSET = cteq6l1.tar.gz

OPT = -O2 -std=c++11 -pedantic -W -Wall -Wshadow -fPIC
INC = -I$(PYTHIA8_DIR)/include
LIBS = -L$(PYTHIA8_DIR)/lib -lpythia8 -ldl

OBJ = $(addsuffix .o,$(basename $(wildcard *.cpp)))

all:
	$(MAKE) LHAPDFget
	$(MAKE) p8get
	$(MAKE) compile
	$(MAKE) pythia_simulation
	$(MAKE) job

p8get:
	wget $(PYTHIA8_URL) && tar xfvz $(PYTHIA8_TGZ) && cd $(PYTHIA8_DIR) && ./configure && make

LHAPDFget:
	wget $(LHAPDF_URL)
	tar xfvz $(LHAPDF_TGZ)
	cd $(LHAPDF_DIR) && ./configure --prefix=$(PDFDIR) && make && make install
.cpp.o:
	$(CXX) $(OPT) $(INC) -c $^ -o $@



compile: $(OBJ)

pythia_simulation:	$(OBJ)
	$(CXX) $(OPT) $(INC) $@.o $(LIBS) -o pythia_simulation

job:
	echo '#!'`which bash` > test.job 
	echo 'export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH):$(PYTHIA8_DIR)/lib' >> test.job
	echo 'export LD_LIBRARY_PATH=$(LHAPDF_DIR)/lib:$$LD_LIBRARY_PATH' >> test.job
	echo 'export PYTHIA8DATA=$(PWD)/pythia8317/share/Pythia8/xmldoc' >> test.job
	echo './pythia_simulation' >> test.job
	chmod +x test.job

clean:
	rm -rf $(GARBAGE)

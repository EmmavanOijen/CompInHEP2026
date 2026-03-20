#include "Pythia8/Pythia.h"

#include <iostream>
using namespace Pythia8;

int main() {

  Pythia pythia;
  pythia.readString("HiggsSM:all = on");
  pythia.readString("PDF:pSet=LHAPDF6:cteq6l1");

  pythia.init();
  for (int iEvent = 0; iEvent < 1000; ++iEvent) {
    if (!pythia.next()) continue;
  }
  pythia.stat();
  std::cout << "n=1000" << std::endl;
  std::cout << "xsec= " << pythia.info.sigmaGen() << std::endl; 
  std::cout << "err = " << pythia.info.sigmaErr() << " (" << std::fixed << std::setprecision(2) << 100*pythia.info.sigmaErr()/pythia.info.sigmaGen() <<"%)" << std::endl;

  for (int iEvent = 0; iEvent < 10000; ++iEvent) {
    if (!pythia.next()) continue;
  }
  pythia.stat();
  std::cout << "n=10000" << std::endl;
  std::cout << "xsec= " << pythia.info.sigmaGen() << std::endl;
  std::cout << "err = " << pythia.info.sigmaErr() << " (" << std::fixed << std::setprecision(2) << 100*pythia.info.sigmaErr()/pythia.info.sigmaGen() <<"%)" << std::endl;
}

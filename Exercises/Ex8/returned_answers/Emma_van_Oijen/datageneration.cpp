#include "Pythia8/Pythia.h"

#include <iostream>
using namespace std;
using namespace Pythia8;

int main() {
  Pythia pythia;

  pythia.readString("SoftQCD:nonDiffractive = on");
  pythia.readString("Beams:eCM = 13600");

  pythia.init();

  ofstream fPT;
  fPT.open ("pT.txt");

  ofstream fETA;
  fETA.open ("eta.txt");

  for (int iEvent = 0; iEvent < 10000; ++iEvent) {
    if (!pythia.next()) continue;

    for (int i = 0; i < pythia.event.size(); ++i) {
      int Eventid = pythia.event[i].id();
      if (Eventid == 13 || Eventid == -13) {
        fPT << pythia.event[i].pT() << endl;
        fETA << pythia.event[i].eta() << endl;
      }
    }
  }

  fPT.close();
  fETA.close();

  return 0;
}

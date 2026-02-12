#include <iostream>
#include <vector>
#include "identityclass.h"
#include <iomanip>
using namespace std;

int main() {
  identity id;
  id.SetValue(-1.0,3.5,4.0,6.8); //Input your test values here.
  id.SetParticleID("electron");
  id.SetParentParticleID("pion");

  auto retvec = id.return_value(); //Unpack the returned 4-momentum.
  cout << setprecision(3);

  cout << "The returned 4-momentum is (" << retvec[0] << ", " \
<< retvec[1] << ", " << retvec[2] << ", " << retvec[3] << ").\n";
  cout << "The transverse momentum is " << id.pT() << ".\n";
  cout << "The pseudorapidity is " << id.pseudorapidity() << ".\n";
  cout << "The particle ID is the " << id.return_particleID() << ".\n";
  cout << "The parent particle ID is the " << id.return_parent_ParticleID() << ".\n";

  return 0;
}

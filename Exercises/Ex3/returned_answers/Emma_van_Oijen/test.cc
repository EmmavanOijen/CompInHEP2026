#include <iostream>
#include <array>
#include "METclass.h"
#include <iomanip>
using namespace std;

int main() {
  MET_class c;
  c.SetValue(-2.0,3.0); //Input your test values here.

  auto retMET = c.return_value();
  cout << setprecision(3);

  cout << "The returned MET is (" << retMET[0] << ", " << retMET[1] << ").\n";
  cout << "x = " << c.x() << "\n";
  cout << "y = " << c.y() << "\n";
  cout << "The amplitude of MET is " << c.amplitude() << ".\n";
  cout << "phi = " << c.phi() << " radians\n";

  return 0;
}

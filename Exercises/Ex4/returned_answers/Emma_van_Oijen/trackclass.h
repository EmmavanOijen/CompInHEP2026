#ifndef TRACKCLASS_H
#define TRACKCLASS_H

#include <vector>
using namespace std;

class track {
  public:
    track();    // Constructor
    ~track();    // Destructor

    void SetValue(double t, double x, double y, double z);

    vector<double> return_value();
    double pT();
    double pseudorapidity();

  protected:
    vector<double> four_momentum;
    double mom_magnitude;
    double theta;
};
#endif

#ifndef METCLASS_H
#define METCLASS_H

#include <array>
using namespace std;

class MET_class {
  public:
    MET_class();    // Constructor
    ~MET_class();    // Destructor

    void SetValue(double x, double y);

    array<double, 2> return_value();
    double x();
    double y();
    double amplitude();
    double phi();

  private:
    double MET_vec[2];
};
#endif

#include <iostream>
#include <cmath>
#include <math.h>
#include <array>
#include "METclass.h"

using namespace std;

MET_class::MET_class(){
  MET_vec[0] = 0;
  MET_vec[1] = 0;
}

MET_class::~MET_class(){}

array<double, 2> MET_class::return_value(){
  return {MET_vec[0], MET_vec[1]};
}

void MET_class::SetValue(double x, double y) {
  MET_vec[0] = x;
  MET_vec[1] = y;
}

double MET_class::x(){
  return MET_vec[0];
}

double MET_class::y(){
  return MET_vec[1];
}

double MET_class::amplitude(){
  return sqrt(x()*x()+y()*y());
}

double MET_class::phi(){
  return (x() >= 0) ? abs(atan(y()/x())) : M_PI - abs(atan(y()/x()));
}

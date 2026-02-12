#include <iostream>
#include <cmath>
#include <vector>
#include "trackclass.h"

using namespace std;

track::track(){}
track::~track(){}

void track::SetValue(double t, double x, double y, double z){
  four_momentum.push_back(t);
  four_momentum.push_back(x);
  four_momentum.push_back(y);
  four_momentum.push_back(z);
}

vector<double> track::return_value(){
  return four_momentum;
}

double track::pT(){
  return sqrt(pow(four_momentum[1],2) + pow(four_momentum[2],2));
}

double track::pseudorapidity(){
  mom_magnitude = sqrt(pow(four_momentum[1],2) + pow(four_momentum[2],2) + pow(four_momentum[3],2));
  theta = acos(four_momentum[3]/mom_magnitude);
  return -log(tan(theta/2));
}

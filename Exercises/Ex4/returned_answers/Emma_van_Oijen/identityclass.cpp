#include <iostream>
#include "identityclass.h"
#include <string>

using namespace std;

identity::identity(){}
identity::~identity(){}

void identity::SetParticleID(string par_ID){
  particleID = par_ID;
}

void identity::SetParentParticleID(string par_par_ID){
  parent_particleID = par_par_ID;
}

string identity::return_particleID(){
  return particleID;
}

string identity::return_parent_ParticleID(){
  return parent_particleID;
}

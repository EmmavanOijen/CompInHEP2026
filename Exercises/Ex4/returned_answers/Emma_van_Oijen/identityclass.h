#ifndef IDENTITYCLASS_H
#define IDENTITYCLASS_H

#include <string>
#include "trackclass.h"
using namespace std;

class identity: public track {
  public:
    identity();    // Constructor
    ~identity();    // Destructor

    void SetParticleID(string par_ID);
    void SetParentParticleID(string par_par_ID);
    string return_particleID();
    string return_parent_ParticleID();

  private:
    string particleID;
    string parent_particleID;
};
#endif

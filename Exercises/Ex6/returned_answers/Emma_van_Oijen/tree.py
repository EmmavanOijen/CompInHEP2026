#!/usr/bin/env python

import ROOT
from array import array

def main():
  datafile = ROOT.TFile("random_data_py.root","RECREATE")
  mytree = ROOT.TTree("mytree","Gaussian random numbers")
  random_number = array('d', [0.0])
  mytree.Branch("random_number",random_number,"random_number/D")

  N = 1000;
  rand = ROOT.TRandom3(123456789);

  for i in range(0,N):
    random_number[0] = rand.Gaus(0, 1)
    mytree.Fill()

  mytree.Write()
  datafile.Close()

main()

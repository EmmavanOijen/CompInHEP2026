#!/usr/bin/env python

import ROOT
from array import array

def main():
  fnumbers = ROOT.TFile.Open("random_data_py.root")
  readtree = fnumbers.Get("mytree")
  number = array('d', [0.0])
  readtree.SetBranchAddress("random_number",number)

  cGauss = ROOT.TCanvas("cGauss", "Gaussian", 700, 500)
  histo = ROOT.TH1D("Gaussian","Gaussian",50,-4,4)

  for i in range(0,readtree.GetEntries()):
    readtree.GetEntry(i)
    histo.Fill(number[0])

  cGauss.SetFillColor(0)
  histo.SetFillColor(5)
  histo.SetLineWidth(4)
  histo.SetLineColor(1)
  histo.GetXaxis().SetTitle("x values")
  histo.GetYaxis().SetTitle("y = count")

  gaussFit = ROOT.TF1("gaussFit","gaus")
  histo.Fit(gaussFit)

  cGauss.Print("plot_py.png")

main()

#!/usr/bin/env python

import re
import ROOT

def main():
  canvas_pt = ROOT.TCanvas("cPT", "Muon minimum bias events pT", 750, 500)
  histo_pt = ROOT.TH1D("pT","pT",50,0,10)

  with open("pT.txt") as file1:
    pt = []
    for line in file1:
      pt.append(float(line))
      histo_pt.Fill(float(line))

  histo_pt.GetXaxis().SetTitle("pT")
  histo_pt.GetYaxis().SetTitle("nr. of events")
  histo_pt.SetTitle("Muon minimum bias events pT")

  histo_pt.Draw()
  canvas_pt.Update()

  canvas_pt.Print("pt.png")
  canvas_pt.Print("pt.pdf")
  canvas_pt.Print("pt.C")


  canvas_eta = ROOT.TCanvas("cETA", "Muon minimum bias events eta", 750, 500)
  histo_eta = ROOT.TH1D("eta","eta",50,-10,10)

  with open("eta.txt") as file2:
    eta = []
    for line in file2:
      eta.append(float(line))
      histo_eta.Fill(float(line))

  histo_eta.GetXaxis().SetTitle("eta")
  histo_eta.GetYaxis().SetTitle("nr. of events")
  histo_pt.SetTitle("Muon minimum bias events eta")

  histo_eta.Draw()
  canvas_eta.Update()

  canvas_eta.Print("eta.png")
  canvas_eta.Print("eta.pdf")
  canvas_eta.Print("eta.C")

  nr_detected = 0
  for i in range(len(pt)):
    if pt[i] > 5 and abs(eta[i])<2.5:
      nr_detected += 1

  print(f"The probability of muon detection from a minimum bias event is {nr_detected/len(pt) *100:.2f}%.")


if __name__ == '__main__':
  main()

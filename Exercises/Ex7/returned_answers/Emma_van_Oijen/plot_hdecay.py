#!/usr/bin/env python

import re
import ROOT
from array import array

def main():
  pattern = re.compile(r"\s*(?P<mass>\d+\.\d+).*?(?P<width>\d+\.\d+E[+-]?\d+)\s*$")

  mytree = ROOT.TTree("mytree","Higgs Decay Output")
  mass = array('d', [0.0])
  mytree.Branch("mass",mass,"mass/D")
  width = array('d', [0.0])
  mytree.Branch("width",width,"width/D")
  
  with open("br.sm2") as file:
    for i,line in enumerate(file):
      match = re.search(pattern, line)
      if match:
        mass[0] = float(match.group('mass'))
        width[0] = float(match.group('width'))
        mytree.Fill()
        if mass[0] == 125.000:
          print(f"The width at m_H = 125 GeV is {width[0]}.")

  cHiggs = ROOT.TCanvas("cHiggs", "Higgs Decay", 750, 500)
  Graph = ROOT.TGraph(mytree.GetEntries())
  for i in range(mytree.GetEntries()):
    mytree.GetEntry(i)
    Graph.SetPoint(i, mass[0], width[0])

  cHiggs.SetFillColor(0)
  Graph.SetTitle("Higgs Decay")
  Graph.SetLineWidth(2)
  Graph.SetLineColor(1)
  Graph.GetXaxis().SetTitle("Higgs mass (GeV)")
  Graph.GetYaxis().SetTitle("Width (GeV)")

  Graph.Draw()
  cHiggs.Update()
  cHiggs.Print("plot_hdecay.png")
  cHiggs.Print("plot_hdecay.pdf")

main()

#!/usr/bin/env python
import ROOT

ROOT.ROOT.EnableImplicitMT()

def main():
    df = ROOT.RDataFrame("Events", "DYJetsToLL.root")

    df = df.Filter("HLT_IsoMu24", "Events which pass the IsoMu24 higher level trigger")

    histo = df.Histo1D(("pileup", ";x-axis;y-axis", 40, 0, 40), "PV_npvs")

    # Plotting the data
    c = ROOT.TCanvas("pileup", "pileup", 750, 500)

    histo.GetXaxis().SetTitle("nr primary vertices")
    histo.GetYaxis().SetTitle("nr of events")
    histo.SetTitle("pileup")

    histo.Draw()
    c.Update()

    c.Print("RDataFrame_pileup.png")
    c.Print("RDataFrame_pileup.pdf")
    c.Print("RDataFrame_pileup.C")


if __name__ == "__main__":
    main()

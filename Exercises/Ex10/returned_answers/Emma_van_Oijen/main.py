#!/usr/bin/env python

import ROOT

def main():

    ROOT.gSystem.Load("libMyAnalysis.so")

    tchain = ROOT.TChain("Events")
    tchain.Add("DYJetsToLL.root")

    tselector = ROOT.MyAnalysis()

    tchain.Process(tselector)


if __name__ == '__main__':
    main()

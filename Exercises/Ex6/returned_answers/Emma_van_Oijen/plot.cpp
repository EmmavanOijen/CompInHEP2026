#include <TFile.h>
#include <TTree.h>
#include <TCanvas.h>
#include <TH1D.h>
#include <TF1.h>

void plot(){
  TFile* fnumbers = TFile::Open("random_data.root");
  TTree* readtree = (TTree*)fnumbers->Get("mytree");
  Double_t number;
  readtree->SetBranchAddress("random_number",&number);

  TCanvas *cGauss = new TCanvas("cGauss", "Gaussian", 700, 500);
  TH1D* histo = new TH1D("Gaussian","Gaussian",50,-4,4);

  for(Long64_t i = 0; i < readtree->GetEntries(); ++i){
    readtree->GetEntry(i);
    histo->Fill(number);
  }

  cGauss->SetFillColor(0);
  histo->SetFillColor(5);
  histo->SetLineWidth(4);
  histo->SetLineColor(1);
  histo->GetXaxis()->SetTitle("x values");
  histo->GetYaxis()->SetTitle("y = count");

  TF1* gaussFit = new TF1("gaussFit","gaus");
  histo->Fit(gaussFit);

  cGauss->Print("plot.png");
}

int main() {
    plot();
    return 0;
}

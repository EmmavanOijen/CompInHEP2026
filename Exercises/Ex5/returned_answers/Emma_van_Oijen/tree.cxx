void tree(){

  TFile * datafile = TFile::Open("random_data.root","RECREATE");
  TTree* mytree = new TTree("mytree","Gaussian random numbers");
  Double_t random_number;
  mytree->Branch("random_number",&random_number);

  int N = 1000;
  TRandom3 rand(0);

  for(int i = 0; i < N; ++i){
    random_number = rand.Gaus(0, 1);
    mytree->Fill();
  }

  mytree->Write();
  datafile->Close();
}

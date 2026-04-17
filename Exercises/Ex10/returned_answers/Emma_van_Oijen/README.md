Note that I did not upload the root file due to its size but that I assume it's in the same folder.

Steps for running everything:
Don't redo these steps since they'll overwrite what I changed:
1. Use python3 makeSelector.py DYJetsToLL.root to create MyAnalysis.h and MyAnalysis.C.
2. Use mv MyAnalysis.C MyAnalysis.cc to change the filetype as mentioned in the example.

You can safely redo these steps:
3. Use make to create the library.
4. Use python3 main.py to create the plots.

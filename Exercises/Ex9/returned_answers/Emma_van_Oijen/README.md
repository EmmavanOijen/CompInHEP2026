The following detector is being used:
The default "material" is vacuum.
The absorber material is lead (G4_Pb) before changing it to water (G4_WATER) in the exercise and rebuilding the example.
The gap material is liquid argon.
The detector consists of a calorimeter with 10 layers.
Each layer contains a 10mm absorber and a 5mm gap.
The calorimeter is thus 10*(10+5)mm = 150mm =15cm thick.
The every layer has a size of 10cm*10cm.
The world is the size of the calorimeter multiplied by 1.2 (so 12cm*12cm*18cm)

To change to water I added:
nistManager->FindOrBuildMaterial("G4_WATER");

and changed "auto absorberMaterial = G4Material::GetMaterial("G4_Pb");" into:
auto absorberMaterial = G4Material::GetMaterial("G4_WATER");

in the file DetectorConstruction.cc before building.

The different particles can be chosen inside the vis.mac file as indicated.
After building I only changed the vis.mac to run the different particles inside the built folder.

Unfortunately, I did not have time to create pictures and I was also unsure of what to create a picture.
(Which output data to use, Energy of absorber or gap or Track Length absorber or gap or whether it needs to be a picture of the detector.)
You can still see all the data using "root" then "new TBrowser" and finally clicking on the branch you wish to see.

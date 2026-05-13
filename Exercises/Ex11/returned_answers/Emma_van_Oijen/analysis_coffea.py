#!/usr/bin/env python
import awkward as ak
import hist
from coffea.nanoevents import NanoEventsFactory, NanoAODSchema
from coffea.nanoevents.methods import candidate
import matplotlib.pyplot as plt

# Remove cross reference index warnings about variables that aren't used.
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

def main():
    filename = "file://DYJetsToLL.root"

    # Creating events
    events = NanoEventsFactory.from_root(
        {filename: "Events"},
        metadata={"dataset": "Pileup"},
        schemaclass=NanoAODSchema,
    ).events()

    # Building PV and trigger objects
    PVs = ak.zip(
        {
	    "npvs": events.PV.npvs,
	    "HLT_IsoMu24": events.HLT.IsoMu24,
        },
        with_name="npvsCandidate",
        behavior=candidate.behavior,
    )

    # Select the number of primary vertices for the events that pass the selection.
    nPVs = PVs.npvs[PVs.HLT_IsoMu24 == True]

    # Flatten table for filling histogram
    nPVs_flat = ak.flatten(nPVs, axis=None)

    # Creating and filling histogram
    h_npvs = hist.Hist.new.Reg(40, 0, 40, name="x", label="nPVs").Double()
    h_npvs.fill(x=nPVs_flat)

    # Plotting the data
    fig, ax = plt.subplots()
    h_npvs.plot(ax=ax)

    ax.set_title("pileup")
    ax.set_xlabel("nr primary vertices")
    ax.set_ylabel("nr of events")
    ax.set_xlim(0,40)
    # Use scientific notation on y-axis (note the le5 denoting 10^5 on top of the axis).
    ax.ticklabel_format(axis="y", style="sci", scilimits=[-3,3])

    plt.savefig("COFFEA_pileup.pdf")
    plt.savefig("COFFEA_pileup.png")


if __name__ == "__main__":
    main()

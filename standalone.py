

processList = {
    

    "mgp8_pp_bb_Q_30000_84000_5f_84TeV":    {"fraction":0.001},

}
outputDir   = "./outputs/treemakerel/"
# outputDirEos = "/eos/users/r/rjafaris" #helps the output to be visible in CERNbox (does not work!)

# Define the input dir (optional)
#inputDir    = "./localSamples/"
inputDir    = "/eos/experiment/fcc/hh/generation/DelphesEvents/fcc_v07/II/"

nCPUS       = -1

from jetClusteringHelper import InclusiveJetClusteringHelper

jetFlavourHelper = None
jetClusteringHelper = None

# Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis:
    # __________________________________________________________
    # Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        global jetClusteringHelper

        njets = 2
        ptcut = 100
        coneRadius = 0.4

## name of collections in EDM root files
        collections = {
    "GenParticles": "Particle",
    "PFParticles": "ReconstructedParticles",
    "PFTracks": "EFlowTrack",
    "PFPhotons": "EFlowPhoton",
    "PFNeutralHadrons": "EFlowNeutralHadron",
    "TrackState": "_EFlowTrack_trackStates",
    "TrackerHits": "TrackerHits",
    "CalorimeterHits": "CalorimeterHits",
    #"dNdx": "EFlowTrack_2",
    "PathLength": "EFlowTrack_L",
    "Bz": "magFieldBz",
        }

        ## define jet clustering parameters
        jetClusteringHelper = InclusiveJetClusteringHelper(collections["PFParticles"], coneRadius, ptcut)

        ## run jet clustering
        df = jetClusteringHelper.define(df)
        return df

    # __________________________________________________________
    # Mandatory: output function, please make sure you return the branchlist as a python list
    def output():

       # branches_jet = list(variables_jet.keys())
        branchList = ["jet_mass"]

        return branchList


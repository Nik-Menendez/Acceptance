import os, sys
from ROOT import TH1F,TH2F,TFile,TTree,TCanvas, TProfile, TNtuple, gErrorIgnoreLevel, kInfo, kWarning
from tqdm import tqdm
tqdm_disable = False

File = TFile("/cmsuf/data/store/user/t2/users/nikmenendez/2018_MC_bkg/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8.root")

tree = File.Get("Ana/passedEvents")
nEvents = tree.GetEntries()

event_total = 0.0
event_pass = 0.0

for i in tqdm(range(0, nEvents),disable=tqdm_disable):
	tree.GetEntry(i)

	event_total+=1
	lep_pass=0

	for j in range(len(tree.GENlep_id)):
		if (abs(tree.GENlep_id.at(j)) == 13 and abs(tree.GENlep_eta.at(j)) < 2.4 and tree.GENlep_pt.at(j) > 5):
			#print "We got a passing muon!"
			lep_pass+=1
		elif (abs(tree.GENlep_id.at(j)) == 11 and abs(tree.GENlep_eta.at(j)) < 2.5 and tree.GENlep_pt.at(j) > 7):
			#print "We got a passing electron!"
			lep_pass+=1

	if (lep_pass >= 3):
		event_pass+=1

print (event_pass/event_total)*100, "% of events were in acceptance"

	

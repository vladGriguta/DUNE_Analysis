

from __future__ import print_function
import ROOT
from ROOT import TCanvas, TGraph
from ROOT import gROOT
from math import sin
from array import array
from ROOT import TH1F, kBlue, kRed

# define dynamically a python class containing root Leaves objects
class PyListOfLeaves(dict) :
    pass


locationResults = '../finalCSVfiles/'

locationRootFiles = '../'
nameOfSNFile = 'SN_tw1.root' #input('Give name of the ROOT file containing SN-like energy depositions:\n')
nameOfArFile = 'Ar39_tw1.root' #input('Give name of the ROOT file containing Ar39-like energy depositions:\n')

# Open the ROOT files
SNfile = ROOT.TFile(str(locationRootFiles+nameOfSNFile))
arfile = ROOT.TFile(str(locationRootFiles+nameOfArFile))


##############################################################################

SNtree_vuv = SNfile.Get("data_tree_vuv");
SNtree_vis = SNfile.Get("data_tree_vis");
SNevent_tree = SNfile.Get("event_tree");

leaves_vuv = SNtree_vuv.GetListOfLeaves()

# create an istance
pyl_vuv = PyListOfLeaves()

for i in range(0,leaves_vuv.GetEntries() ) :
    leaf = leaves_vuv.At(i)
    name = leaf.GetName()
    # add dynamically attribute to my class 
    pyl_vuv.__setattr__(name,leaf)


nev = SNtree_vuv.GetEntries()
timeSN_vuv = []
pmt_vuv = []
x_vuv = []
y_vuv = []
z_vuv = []
event_vuv = []

for iev in range(0,nev):
    SNtree_vuv.GetEntry(iev)
    # get values from the tree using Python class pyl which contains leaves
    # objects 
    timeSN_vuv.append(pyl_vuv.data_time_vuv.GetValue())
    pmt_vuv.append(pyl_vuv.data_pmt_vuv.GetValue())
    x_vuv.append(pyl_vuv.data_x_pos_vuv.GetValue())
    y_vuv.append(pyl_vuv.data_y_pos_vuv.GetValue())
    z_vuv.append(pyl_vuv.data_z_pos_vuv.GetValue())
    event_vuv.append(pyl_vuv.data_event_vuv.GetValue())
    #print(timeSN[iev])

with open(locationResults+'time_SN_vuv.csv', 'w') as f:
    f.write("time,pmt,x,y,z,event\n")
    for i in range(0,nev):
        f.write(str(timeSN_vuv[i]) + ', ' + str(pmt_vuv[i]) + ', ' + str(x_vuv[i]) \
        + ', ' + str(y_vuv[i]) + ', ' + str(z_vuv[i]) + ', ' + str(event_vuv[i]) + '\n')
f.close()

###############################################################################

leaves_vis = SNtree_vis.GetListOfLeaves()

# create an istance
pyl_vis = PyListOfLeaves()

for i in range(0,leaves_vis.GetEntries() ) :
    leaf = leaves_vis.At(i)
    name = leaf.GetName()
    # add dynamically attribute to my class 
    pyl_vis.__setattr__(name,leaf)


nev = SNtree_vis.GetEntries()
timeSN_vis = []
pmt_vis = []
x_vis = []
y_vis = []
z_vis = []
event_vis = []

for iev in range(0,nev):
    SNtree_vis.GetEntry(iev)
    # get values from the tree using Python class pyl which contains leaves
    # objects 
    timeSN_vis.append(pyl_vis.data_time_vis.GetValue())
    pmt_vis.append(pyl_vis.data_pmt_vis.GetValue())
    x_vis.append(pyl_vis.data_x_pos_vis.GetValue())
    y_vis.append(pyl_vis.data_y_pos_vis.GetValue())
    z_vis.append(pyl_vis.data_z_pos_vis.GetValue())
    event_vis.append(pyl_vis.data_event_vis.GetValue())
    #print(timeSN[iev])

with open(locationResults+'time_SN_vis.csv', 'w') as f:
    f.write("time,pmt,x,y,z,event\n")
    for i in range(0,nev):
        f.write(str(timeSN_vis[i]) + ', ' + str(pmt_vis[i]) + ', ' + str(x_vis[i]) \
        + ', ' + str(y_vis[i]) + ', ' + str(z_vis[i]) + ', ' + str(event_vis[i]) + '\n')
f.close()

###############################################################################
# Probably won't need anything from the event_tree from now on

"""

leaves_event = SNevent_tree.GetListOfLeaves()

# create an istance
pylEvent = PyListOfLeaves()

for i in range(0,leaves_event.GetEntries() ) :
    leaf = leaves_event.At(i)
    name = leaf.GetName()
    # add dynamically attribute to my class 
    pylEvent.__setattr__(name,leaf)


nev = SNevent_tree.GetEntries()
# print(nev)
energySN = []
xposSN = []
decayTime = []
for iev in range(0,nev):
    SNevent_tree.GetEntry(iev)
    # get values from the tree using Python class pyl which contains leaves
    # objects 
    energySN.append(pylEvent.event_E.GetValue())
    xposSN.append(pylEvent.event_x_pos.GetValue())
    decayTime.append(pylEvent.event_decay_time.GetValue())

with open('events_SN.txt', 'w') as f:
    f.write("energy,x,decayTime\n")
    for i in range(0,nev):
    	print(energySN[i])
        f.write(str(energySN[i]) + ', ' + str(xposSN[i]) + ', ' + str(decayTime[i]) + '\n')
f.close()

"""



###############################################################################

artree_vuv = arfile.Get("data_tree_vuv");


arleaves_vuv = artree_vuv.GetListOfLeaves()

# create an istance
pylAr_vuv = PyListOfLeaves()

for i in range(0,arleaves_vuv.GetEntries() ) :
    leaf = arleaves_vuv.At(i)
    name = leaf.GetName()
    # add dynamically attribute to my class 
    pylAr_vuv.__setattr__(name,leaf)
    print(name)


nev = artree_vuv.GetEntries()
print('Total number of vuv photons is  '+str(nev))
artime_vuv = []
arpmt_vuv = []
arx_vuv = []
ary_vuv = []
arz_vuv = []
arevent_vuv = []

k = 0;
for iev in range(0,nev):
    artree_vuv.GetEntry(iev)
    # get values from the tree using Python class pyl which contains leaves
    # objects
    artime_vuv.append(pylAr_vuv.data_time_vuv.GetValue())
    arpmt_vuv.append(pylAr_vuv.data_pmt_vuv.GetValue())
    arx_vuv.append(pylAr_vuv.data_x_pos_vuv.GetValue())
    ary_vuv.append(pylAr_vuv.data_y_pos_vuv.GetValue())
    arz_vuv.append(pylAr_vuv.data_z_pos_vuv.GetValue())
    arevent_vuv.append(pylAr_vuv.data_event_vuv.GetValue())
    if ( iev % (nev/10) == 0 ):
    	print(str(k) + "% Completed...\n" );
    	k = k + 10;
    

with open(locationResults+'time_Ar_vuv.csv', 'w') as f:
    f.write("time,pmt,x,y,z,event\n")
    for i in range(0,nev):
        f.write(str(artime_vuv[i]) + ', ' + str(arpmt_vuv[i]) + ', ' + str(arx_vuv[i]) \
        + ', ' + str(ary_vuv[i]) + ', ' + str(arz_vuv[i]) + ', ' + str(arevent_vuv[i]) + '\n')
f.close()

###############################################################################
artree_vis = arfile.Get("data_tree_vis");

arleaves_vis = artree_vis.GetListOfLeaves()

# create an istance
pylAr_vis = PyListOfLeaves()

for i in range(0,arleaves_vis.GetEntries() ) :
    leaf = arleaves_vis.At(i)
    name = leaf.GetName()
    # add dynamically attribute to my class 
    pylAr_vis.__setattr__(name,leaf)
    print(name)


nev = artree_vis.GetEntries()
print('Total number of visual photons is  '+str(nev))
artime_vis = []
arpmt_vis = []
arx_vis = []
ary_vis = []
arz_vis = []
arevent_vis = []

k = 0;
for iev in range(0,nev):
    artree_vis.GetEntry(iev)
    # get values from the tree using Python class pyl which contains leaves
    # objects
    artime_vis.append(pylAr_vis.data_time_vis.GetValue())
    arpmt_vis.append(pylAr_vis.data_pmt_vis.GetValue())
    arx_vis.append(pylAr_vis.data_x_pos_vis.GetValue())
    ary_vis.append(pylAr_vis.data_y_pos_vis.GetValue())
    arz_vis.append(pylAr_vis.data_z_pos_vis.GetValue())
    arevent_vis.append(pylAr_vis.data_event_vis.GetValue())
    #if ( iev % (nev/10) == 0 ):
    #	print(str(k) + "% Completed...\n" );
    #	k = k + 10;
    

with open(locationResults+'time_Ar_vis.csv', 'w') as f:
    f.write("time,pmt,x,y,z,event\n")
    for i in range(0,nev):
        f.write(str(artime_vis[i]) + ', ' + str(arpmt_vis[i]) + ', ' + str(arx_vis[i]) \
        + ', ' + str(ary_vis[i]) + ', ' + str(arz_vis[i]) + ', ' + str(arevent_vis[i]) + '\n')
f.close()

###############################################################################



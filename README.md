# Steps for running the code:


1. Source a version of python3 that has all packages installed. E.G.:
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_93python3 x86_64-slc6-gcc62-opt

2. Turn the .root files into .csv files usign code in folder 'RootToCsv':
python3 RootToCsv/copyToCsv.py

3. Run the actual analysis:
python3 DataAnalysis/main.py

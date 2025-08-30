# fastjet-fccanalyses-bugreport

you can change the clustering radius inside `standalone.py` and see how the behavior changes. 

R = 2 : Crashes
R = 0.39 does NOT Crash
R = 0.4 Crashes

This is not consistent behavior. 

```bash
source /cvmfs/sw.hsf.org/key4hep/setup.sh -r 2025-01-28
fccanalysis run  standalone.py
```

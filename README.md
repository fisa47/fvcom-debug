# fvcom-debug

## Issue Summary
The evaporation variable (water_evaporation_amount) was not properly downloaded from MEPS archives for 2018.
The absence of evaporation data caused NaNs in the FVCOM forcing files and then NaNs in the output.
The missing evaporation values were set to zero in the forcing dataset.

## Files and Scripts
1. Data Checking & Debugging  
`check_MEPS_evap.py`: Checks for missing values in MEPS datasets via Opendap and verifies evaporation data.  
`qc_atm_forcing.py`: Quality check on atmospheric forcing variables, generates plots.
2. Fixing the Evaporation Issue  
`fix_evaporation.py`: Overwrites missing evaporation with zero (0) in the atmospheric forcing.
3. Preprocessing & Model Setup  
`convert_to_node.py`: Converts locations in rivers NML file from edges to nodes format.  
`add_fabm_river.ipynb`: Notebooks related to adding river (pipe) input to NML and also add FABM tracer to river files, nesting and restart.
4. Simulation Output & Validation  
`qc_output.py`: Analyzes FVCOM simulation output, generates plots.

## Fix Implementation
1. Check MEPS Data  
Use `check_MEPS_evap.py` to verify evaporation. water_evaporation_amount was available, but effie didn't download it.
2. Modify Forcing Data  
Use `fix_evaporation.py` to replace evaporation values with 0 in adamselv_forcing_evap0.nc.
3. Validate Fixes  
`qc_atm_forcing.py` to confirm no missing variables.
Check simulation results using `qc_output.py`.

## Future Improvements
- Fix Effie downloading evaporation (already tried to add base_names to try to download from THREDDS, but it didn't help).
- Improve Effie handling of missing variables

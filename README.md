# Correlating Disordered Activation Domain Ensembles with Gene Expression Levels #
## by Eduardo Flores, Aleah R. Camacho, Estefania Cuevas-Zepeda, Mary B. McCoy, Feng Yu, Max V. Staller, Shahar Sukenik

Welcome to the repository for the Flores et al. 2024 project! 
This repository contains all the data, analysis scripts, and 
figures associated Flores et al. 2024 from the Sukenik Lab.

Overview

This project correlates the ensemble dimensions of HIF1A and CITED2 with their transcriptional activity.

The repository includes:

Scripts for data analysis and figure generation.
Processed and raw datasets.
Reproducible workflows for statistical and biophysical analyses.
Repository Contents

DIRECTORIES
The following directories are included for data analysis and figure generation:

FIGURE_2A+2B: Scripts and data for Figure 2A and 2B.
FIGURE_2D+2F: Scripts and data for Figure 2D and 2F.
FIGURE_3A+3B: Scripts and data for Figure 3A and 3B.
FIGURE_3C: Scripts and data for Figure 3C.
FIGURE_3D: Scripts and datafor Figure 3D.
FIGURE_3E+3F: Scripts and data  for Figures 3E and 3F.
FIGURE_3G+3H: Scripts and data for Figures 3G and 3H.
FIGURE_4A+4B+4C: Scripts and data for Figures 4A, 4B, and 4C. 

AGADIR: Secondary structure prediction analysis using AGADIR.
ALPHAFOLD_PYMOL: DSSPS.ipynb: Scripts for DSSPS analysis.
SPARROW_SEQUENCE_FEATURES_HIF1A_SUPPLEMENTAL: Supplemental analysis of sequence features for HIF1A.
SPARROW_SEQUENCE_FEATURES_CITED2_2.5_SUPPLEMENTAL: Supplemental analysis of sequence features for CITED2.
FIJI_SCRIPTS:  ImageJ macro for segmenting cells in FRET microscopy experiments.

Data Files
Re_normalized.csv: Normalized R_e data for statistical analysis.
HIF1A_CITED2_SIGNIFICANT_ACTIVITY_STALLER.csv: Dataset of significant activity measurements.
OSMOTIC_PERTURBATIONS_MASTER_HIF1A_CITED2.csv: Master dataset for osmotic perturbation experiments.
BASAL_HIF1A_CITED2_MASTER.csv: Master dataset for basal activity measurements.
STALLER_2022_wREE.csv: Staller et al. 2022 dataset with calculated wREE values.
Shahar_ADvariants_20211203.csv: Activity measurements for AD sequences.
SEQUENCES_NAME.csv: Names of sequences fromatted for Figure 2A and 2B.
predictions.csv: raw predicted Re values for HIF1A and CITED2 sequences.

Getting Started

Clone the repository:
git clone https://github.com/sukeniklab/flores_et_al_2024.git

Navigate to the repository:
cd flores_et_al_2024

Install dependencies for Jupyter notebooks and Python scripts:
pip install dependency 

numpy
pandas
matplotlib
seaborn
scipy
jupyterlab
notebook
ipython
statsmodels
biopython  # For sequence analysis, if applicable
sparrow  # If you're using Sparrow for sequence features

Open and execute the Jupyter notebooks:
jupyter notebook

Requirements

Python 3.8+
Jupyter Notebook
Standard scientific libraries: numpy, pandas, matplotlib, etc.

Citation:
If you use this code or data in your research, please cite: Flores et al., 2024.

Acknowledgments

This research was conducted in the Sukenik Lab at UC Merced/Syracuse University. Special thanks to Max Staller at UC Berkeley and all funding sources.

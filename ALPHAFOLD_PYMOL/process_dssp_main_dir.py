import os
import csv
from pymol import cmd  # Import the PyMOL command module

# List of subdirectories to process
subdirectories = [
    "CITED2LW_5b72e",
    "CITED2RKAmut20to39_0cab3",
    "CITED2RKE_3eea4",
    "CITED2WT_28a97",
    "CITED2_EDAmut0to20",
    "CITED2_LF",
    "CITED2killmotif1_e4567",
    "GS39_b78cc",
    "Hif1AD2_46_supercharge6_fbee4",
    "Hif1AD2_46_WT_ea1ca",
    "Hif1AD2_46_RKD",
    "Hif1AD2_46_NQ>W_8365c",
    "Hif1AD2_46_MA>W",
    "GS46_43947"

]

# Main directory where the script is being run
main_directory = os.getcwd()

# Process each subdirectory
for subdir in subdirectories:
    # Look for .pdb files in the subdirectory containing 'rank_001'
    pdb_files = [f for f in os.listdir(subdir) if f.endswith('.pdb') and 'rank_001' in f]
    if not pdb_files:
        print(f"No 'rank_001' PDB files found in {subdir}. Skipping...")
        continue
    
    # Process the first 'rank_001' .pdb file found in the subdirectory
    pdb_file = pdb_files[0]
    pdb_path = os.path.join(subdir, pdb_file)
    object_name = os.path.splitext(pdb_file)[0]  # Extract object name from filename
    
    # Load the PDB file
    cmd.load(pdb_path)
    
    # Calculate DSSP
    cmd.dss(object_name)
    
    # Save DSSP data to a CSV file in the main directory
    output_csv = os.path.join(main_directory, f"{object_name}_dssp.csv")
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Residue Number', 'Residue Name', 'Secondary Structure'])
        cmd.iterate(f"({object_name})", "writer.writerow([resi, resn, ss])", space={'writer': writer})
    
    print(f"DSSP data saved to {output_csv}")
    
    # Save the structure with updated DSSP assignments in the main directory
    output_pdb = os.path.join(main_directory, f"{object_name}_dssp.pdb")
    cmd.save(output_pdb, object_name)
    
    # Remove the object from memory to process the next file
    cmd.delete(object_name)

print("DSSP processing complete for all subdirectories.")

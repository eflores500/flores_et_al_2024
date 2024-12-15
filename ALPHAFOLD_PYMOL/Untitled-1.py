import os
import csv
from pymol import cmd  # Import the PyMOL command module

# List of subdirectories to process
subdirectories = [
    "CITED2EDAmut0to20_094e4",
    "CITED2LF_af5c8",
    "CITED2LW_5b72e",
    "CITED2RKAmut20to39_0cab3",
    "CITED2RKE_3eea4",
    "CITED2WT_28a97",
    "GS39_b78cc",
    "GS46_43947",
    "Hif1AD2_46_MA>W",
    "Hif1AD2_46_NQ>W_8365c",
    "Hif1AD2_46_RKD_312ec",
    "Hif1AD2_46_WT_ea1ca",
    "Hif1AD2_46_supercharge6_fbee4"
]

# Process each subdirectory
for subdir in subdirectories:
    # Look for .pdb files in the subdirectory
    pdb_files = [f for f in os.listdir(subdir) if f.endswith('.pdb')]
    if not pdb_files:
        print(f"No PDB files found in {subdir}. Skipping...")
        continue
    
    # Process the first .pdb file found in the subdirectory
    pdb_file = pdb_files[0]
    pdb_path = os.path.join(subdir, pdb_file)
    object_name = os.path.splitext(pdb_file)[0]  # Extract object name from filename
    
    # Load the PDB file
    cmd.load(pdb_path)
    
    # Calculate DSSP
    cmd.dss(object_name)
    
    # Save DSSP data to a CSV file
    output_csv = os.path.join(subdir, f"{object_name}_dssp.csv")
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Residue Number', 'Residue Name', 'Secondary Structure'])
        cmd.iterate(f"({object_name})", "writer.writerow([resi, resn, ss])", space={'writer': writer})
    
    print(f"DSSP data saved to {output_csv}")
    
    # Display the structure in cartoon representation
    cmd.show('cartoon', object_name)
    
    # Color secondary structures
    cmd.color('red', f"ss H and {object_name}")  # Helices
    cmd.color('yellow', f"ss S and {object_name}")  # Sheets
    cmd.color('green', f"ss L+ and {object_name}")  # Loops/Other
    
    # Save the structure with updated DSSP assignments
    output_pdb = os.path.join(subdir, f"{object_name}_dssp.pdb")
    cmd.save(output_pdb, object_name)
    
    # Remove the object from memory to process the next file
    cmd.delete(object_name)

print("DSSP processing complete for all subdirectories.")

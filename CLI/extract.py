import os # interation with the OS

def extract_BNF(file):
     # Define the output directory and ensure it exists
     output_dir = os.path.join(os.path.dirname(__file__), "extracted_BNF")
     os.makedirs(output_dir, exist_ok=True)
     
     # Define the base filename for the output CSV
     csv_fname = os.path.join(output_dir, "feature_extract_file")
     csv_fname_with_ext = csv_fname+".csv"

     #### To remove the old file if it exists
     if os.path.isfile(csv_fname_with_ext):
          os.remove(csv_fname_with_ext)
          
     # Construct the full path to the script to be executed
     script_path = os.path.join(os.path.dirname(__file__), "BUT/mkhaudio2bottleneck.py")
     
     # Execute the bottleneck feature extraction script
     os.system(f"python {script_path} BabelMulti {file} {csv_fname}")
     
     return csv_fname_with_ext

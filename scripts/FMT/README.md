# Scripts used to combine normalized gene coverage, KEGG info and MAG info
### You will need the following files:
  - exported functions (generated from anvio with the anvi-export-functions command)
  - gene coverage (generated from anvio with the anvi-export-splits-and-coverages command)
  - KEGG orthology table (generated following these instructions https://merenlab.org/2018/01/17/importing-ghostkoala-annotations/)
  
### Steps:  
1) Run the script **file_per_bin.sh** - This will create one file per bin 
2) Run the script **add_bug_name.py** - This script adds a ? so you can replace it later with the right bin name
3) Run the script **replace_bug_name.sh** - This script will create a **genedict** file
4) Modify the genedict file by importing the file into R and following the instructions in the *modify-genedict-FMT.R* script
5) Run the script **merge_names_withBinNames.py** - This script contains the normalization values (obtained from the **RUNLOG.txt** file that was generated during the anvi-merge step)
   
   *This script will generate 5 files:*
   - **outfile1.csv**
   - **outfile2.csv**
   - **outfile3.csv**
   - **Pathways.csv**
   - **KOs.csv**

6) Run the script **collapsed_pathways_then_r.py** - Will create the **collapsed_pathways.csv** file


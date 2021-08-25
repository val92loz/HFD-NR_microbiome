# Scripts used to combine normalized gene coverage, KEGG info and MAG info
### You will need the following files:
  - exported functions (generated from anvio with the anvi-export-functions command)
  - gene coverage (generated from anvio with the anvi-export-splits-and-coverages command)
  - KEGG orthology table (generated following these instructions https://merenlab.org/2018/01/17/importing-ghostkoala-annotations/)
  - genedict zip file (Because this file is so large, I uploaded it as 3 zipped files. Download all three zip files, unzip and then combine all files into one)
    - *cat genedict-** *> genedict* 
 
  
### Steps:  
1) Modify the **genedict** file by importing the file into R and following the instructions in the **modify-genedict-FMT.R** script
2) Run the script **merge_names_withBinNames.py** - This script contains the normalization values (obtained from the **RUNLOG.txt** file that was generated during the anvi-merge step)
   
   *This script will generate 5 files:*
   - **outfile1.csv**
   - **outfile2.csv**
   - **outfile3.csv**
   - **Pathways.csv**
   - **KOs.csv**

3) Run the script **collapse_pathways.py** - Will create the **collapsed_pathways.csv** file


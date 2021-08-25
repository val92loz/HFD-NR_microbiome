#To normalize you need the normalization values found in the RUNLOG.txt file created during the anvi-merge step
import pandas as pd

#import your file
df_raw_cov = pd.read_csv('Gene_COV_and_Detection-GENE-COVERAGES.csv')

#normalize by
df_norm_cov = pd.DataFrame(
    {
        "gene_callers_id": df_raw_cov.gene_callers_id,
        "NR_SAMPLE198":df_raw_cov.NR_SAMPLE198 * 0.97,
        "NR_SAMPLE200":df_raw_cov.NR_SAMPLE200 * 1,
        "NR_SAMPLE201":df_raw_cov.NR_SAMPLE201 * 0.97,
        "NR_SAMPLE202":df_raw_cov.NR_SAMPLE202 * 0.98,
        "NR_SAMPLE203":df_raw_cov.NR_SAMPLE203 * 0.99,
        "NR_SAMPLE204":df_raw_cov.NR_SAMPLE204 * 0.96,
        "CONTRL_SAMPLE205":df_raw_cov.CONTRL_SAMPLE205 * 0.94,
        "CONTRL_SAMPLE209":df_raw_cov.CONTRL_SAMPLE209 * 0.96,
        "CONTRL_SAMPLE210":df_raw_cov.CONTRL_SAMPLE210 * 0.94,
        "CONTRL_SAMPLE211":df_raw_cov.CONTRL_SAMPLE211 * 0.94,
        "CONTRL_SAMPLE212":df_raw_cov.CONTRL_SAMPLE212 * 0.95,
        "CONTRL_SAMPLE213":df_raw_cov.CONTRL_SAMPLE213 * 0.94
        }
    ) 

df_norm_cov.to_csv('normalized-gene-coverages.csv', index= False)

#first you want to start merge the gene calls with the different KO annotations

#import your files

df1 = pd.read_csv('genedict-modified.csv')
df2 = pd.read_csv('KeggOrthology_Table1.csv')
results=df1.merge(df2,on='accession', how='left')
results.to_csv('outfile1.csv')

#so that outfile1 will be a new table that has all the ids for gene calls and all the KEGG categories

#now you need to add on the gene coverages. 
#make sure that in the coverage table the header included 'gene_callers_id'

df3=pd.read_csv('normalized-gene-coverages.csv')

results2=df3.merge(results, on='gene_callers_id', how='left')

results2.to_csv('outfile2.csv')

#now all the gene coverages will not have a KEGG annotation. you will want to compute those later separate to make sure you're accounting for all of the data/all of the genes
#but for now we're going to just drop those lines

results3=results2.dropna(axis=0, subset=['Category1'])

#outfile3 is now a csv file that has all the coverages for each mouse with all the annotations

results3.to_csv('outfile3.csv')

#now you want to generate a table for each KEGG level (category1, category2, category3)

#first delete all the columns that are not used

resultsPathways=results3.drop(['gene_callers_id','contig','sequence','accession','Category1','Category2','description','accession'],axis=1)

resultsKOs=results3.drop(['gene_callers_id','contig','sequence','Category1','Category2','description'],axis=1)

resultsPathways.columns = ['NR_SAMPLE198', 'NR_SAMPLE200', 'NR_SAMPLE201', 'NR_SAMPLE202', 'NR_SAMPLE203', 'NR_SAMPLE204', 'CONTRL_SAMPLE205','CONTRL_SAMPLE209','CONTRL_SAMPLE210','CONTRL_SAMPLE211','CONTRL_SAMPLE212', 'CONTRL_SAMPLE213',  'bin', 'Category3']

resultsPathways = resultsPathways[['bin','Category3','NR_SAMPLE198', 'NR_SAMPLE200', 'NR_SAMPLE201', 'NR_SAMPLE202', 'NR_SAMPLE203', 'NR_SAMPLE204', 'CONTRL_SAMPLE205','CONTRL_SAMPLE209','CONTRL_SAMPLE210','CONTRL_SAMPLE211','CONTRL_SAMPLE212', 'CONTRL_SAMPLE213']]

resultsPathways.to_csv('Pathways.csv', index= False)

resultsKOs.to_csv('KOs.csv', index= False)

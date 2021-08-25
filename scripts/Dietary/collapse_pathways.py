#This script will collapse/sum KOs into pathways 
import pandas as pd

df1=pd.read_csv('Pathways.csv')

collapsedPathways=df1.groupby(
    ['bin','Category3'],as_index=False
        ).agg(
            {
    "CONTRL_SAMPLE250":sum,
    "CONTRL_SAMPLE251":sum,
    "CONTRL_SAMPLE253":sum,
    "CONTRL_SAMPLE254":sum,
    "CONTRL_SAMPLE255":sum,
    "CONTRL_SAMPLE256":sum,
    "NR_SAMPLE258":sum,
    "NR_SAMPLE259":sum,
    "NR_SAMPLE260":sum,
    "NR_SAMPLE261":sum,
    "NR_SAMPLE264":sum,
    "NR_SAMPLE265":sum
        }
    )

collapsedPathways.to_csv('collapsedPathways.csv', index = False)

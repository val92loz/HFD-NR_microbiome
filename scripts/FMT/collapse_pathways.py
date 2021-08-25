#This script will collapse/sum KOs into pathways 
import pandas as pd

df1=pd.read_csv('Pathways.csv')

collapsedPathways=df1.groupby(
    ['bin','Category3'],as_index=False
        ).agg(
            {
    "NR_SAMPLE198":sum,
    "NR_SAMPLE200":sum,
    "NR_SAMPLE201":sum,
    "NR_SAMPLE202":sum,
    "NR_SAMPLE203":sum,
    "NR_SAMPLE204":sum,
    "CONTRL_SAMPLE205":sum,
    "CONTRL_SAMPLE209":sum,
    "CONTRL_SAMPLE210":sum,
    "CONTRL_SAMPLE211":sum,
    "CONTRL_SAMPLE212":sum,
    "CONTRL_SAMPLE213":sum
        }
    )

collapsedPathways.to_csv('collapsedPathways.csv', index = False)

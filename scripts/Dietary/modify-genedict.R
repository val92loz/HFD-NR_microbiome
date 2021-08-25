#Script to modify the genedict file that contains all of the KOs with the bins 

#import packages
library(readr)

#import genedict
genedict <- read_csv("genedict", col_names = FALSE, 
                     col_types = cols(X1 = col_number(), 
                                      X10 = col_skip(), X11 = col_skip(), 
                                      X12 = col_skip(), X13 = col_skip(), 
                                      X14 = col_skip(), X15 = col_skip(), 
                                      X4 = col_skip(), X5 = col_skip(), 
                                      X6 = col_skip(), X7 = col_skip(), 
                                      X8 = col_skip(), X9 = col_skip()))

#add col names
colnames(genedict) <- c("gene_callers_id", "contig", "bin","accession","sequence")

#make it a dataframe
genedict <- as.data.frame(genedict)
head(genedict)

#send df to a csv file
write.table(genedict, file = "genedict-modified.csv", sep = ",",
            row.names = FALSE)

# HFD-NR_microbiome
This repository provides the scripts used to analyze the metagenomics data from the paper Nicotinamide Riboside-Conditioned Microbiota Deflects High-Fat Diet-Induced Weight Gain in Mice. 

# Download Raw data
Raw reads for shotgun metagenomes are available in the Sequence Read Archive: PRJNA704567.

# Shotgun metagenomics workflow 
In this study, 24 murine fecal samples from the Dietary and FMT experiments were subjected to 2 x 150 paired-end shotgun metagenomics sequencing using the Illumina NovaSeq platform by the University of Wisconsin – Madison Biotechnolgy Center. 

Steps:
- Generated reads were trimmed using Trimmomatic (version 0.38) (1) to remove low-quality reads. 
- Forward and reverse reads were merged using Illumina-utils (version 1.5.0) (2), and then subsampled to the lowest number of reads per sample using Mothur (version 1.35.1) (3). 
- Reads from all samples were co-assembled using MegaHit (version 1.1.1) (4, 5) resulting in a single contigs file. 
- The contigs file was simplified using the anvi-script-reformat-fasta, which is part of Anvi’o (version 5.4) (6), and was then indexed using Bowtie2 (version 2.2.8) (7). 
- Individual sample read files were mapped back to the contigs file, also using Bowtie2 (7) and samtools (version 1.3) (8). 
- The resulting BAM files provided sample information compared to the whole. 
- Anvi’o was used to 
    - create a contigs database, which calculated k-mer frequencies for each contig, identified open reading frames (ORF) using Prodigal (9), and split the contigs into 20,000 bp regions (6).
    - run Hidden Markov Models (HMMs), which searched for single-copy genes to predict the amount of total genomes present (6). 
    - Add protein annotation using COGs (10), Pfam (11), and InterproScan (12) and add taxonomic identity using KAIJU (version 1.7.2) (13). 
    - generate profile databases for each sample; these databases store sample-specific information about the contigs, such as mean coverage, standard deviation of coverage, and single nucleotide variant information (6)
    - merge individual profiles into one profile with hierarchical clustering
    - import results generated using CONCOCT (version 0.4.1) (14). Bins (>2 Mb length) were manually curated to decrease redundancy (<10%) and increase completion (>50%) of metagenomic assembled genomes (MAGs). We assessed the quality of these MAGs using the four previously published bacterial single-copy core gene collections found in Anvi’o (15).
    
- MAGs were subjected to LDA Effect Size (LEfSe) (16) algorithm to identify discriminant  features. The alpha value for the factorial Kruskal-Wallis test among classes and for the pairwise Wilcoxon test between subclasses was set to 0.05. The threshold on the logarithmic LDA score for discriminative features was set to 2.0. The analysis was run on the http://huttenhower.sph.harvard.edu/galaxy/ site.
- The mean coverage of genes, and functional annotations were exported from Anvi’o as tables. Using in-house python scripts, we matched the mean coverage to the corresponding gene annotations (KEGG database) and normalized it to mapped reads per sample (Normalization values found in the RUNLOG.txt output file from anvi-merge command). The data was formatted to have the features (Pathways or KOs) as rows and Subjects as columns. The KOs from enriched Pathways were analyzed using LEfSe (16).
- The discriminant KOs identified by LEfSe were used to generate a network analysis using the following python modules: pandas, numpy, matplotlib.pyplot and network. The network was reformatted, imported into Cytoscape, where the Compound Spring Embedded (CoSE) layout was applied. The node size represents the LDA score (LEfSe analysis), and the edge width represents the r value (Pearson’s correlation). We set a cutoff of 0.7 for the r values to decrease the number of edges and improve the visualization of the network. 
- Butyrate KO analysis - we annotated microbial genes using Kyoto Encyclopedia of Genes and Genomes (KEGG) orthology (KOs). To identify discriminant KOs from butyrate production pathways, we implemented LEfSe on the following KOs: K00004, K00019, K00074, K00100, K00132, K00169, K00170, K00171, K00172, K00174, K00175, K00209, K00239, K00240, K00241, K00244, K00246, K00626, K00634, K00656, K00823, K00929, K01027, K01029, K01034, K01035, K01039, K01040, K01580, K01615, K01640, K01641, K01715, K03366, K03737, K04072, K04073, K07246, K07250, K07516, K14534, K17865, K18118, K18119, K18120, K18121, K18122, K18366, K19709, K20509, K23351, K23352, K00248, K03522, and K03521.

# References
1- Bolger AM, Lohse M, Usadel B. 2014. Trimmomatic: a flexible trimmer for Illumina sequence data. Bioinformatics 30:2114–2120.

2- Eren AM, Vineis JH, Morrison HG, Sogin ML. 2013. A Filtering Method to Generate High Quality Short Reads Using Illumina Paired-End Technology. PLOS ONE 8:e66643.

3- Schloss PD, Westcott SL, Ryabin T, Hall JR, Hartmann M, Hollister EB, Lesniewski RA, Oakley BB, Parks DH, Robinson CJ, Sahl JW, Stres B, Thallinger GG, Horn DJV, Weber CF. 2009. Introducing mothur: Open-Source, Platform-Independent, Community-Supported Software for Describing and Comparing Microbial Communities. Appl Environ Microbiol 75:7537–7541.

4- Li D, Liu C-M, Luo R, Sadakane K, Lam T-W. 2015. MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph. Bioinformatics 31:1674–1676.

5- Li D, Luo R, Liu C-M, Leung C-M, Ting H-F, Sadakane K, Yamashita H, Lam T-W. 2016. MEGAHIT v1.0: A fast and scalable metagenome assembler driven by advanced methodologies and community practices. Methods 102:3–11.

6- Eren AM, Esen ÖC, Quince C, Vineis JH, Morrison HG, Sogin ML, Delmont TO. 2015. Anvi’o: an advanced analysis and visualization platform for ‘omics data. PeerJ 3:e1319.

7- Langmead B, Salzberg SL. 2012. Fast gapped-read alignment with Bowtie 2. Nat Methods 9:357–359.

8- Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R. 2009. The Sequence Alignment/Map format and SAMtools. Bioinformatics 25:2078–2079.

9- Hyatt D, Chen G-L, LoCascio PF, Land ML, Larimer FW, Hauser LJ. 2010. Prodigal: prokaryotic gene recognition and translation initiation site identification. BMC Bioinformatics 11:119.

10- Tatusov RL, Galperin MY, Natale DA, Koonin EV. 2000. The COG database: a tool for genome-scale analysis of protein functions and evolution. Nucleic Acids Res 28:33–36.

11- Finn RD, Bateman A, Clements J, Coggill P, Eberhardt RY, Eddy SR, Heger A, Hetherington K, Holm L, Mistry J, Sonnhammer ELL, Tate J, Punta M. 2014. Pfam: the protein families database. Nucleic Acids Res 42:D222–D230.

12- Jones P, Binns D, Chang H-Y, Fraser M, Li W, McAnulla C, McWilliam H, Maslen J, Mitchell A, Nuka G, Pesseat S, Quinn AF, Sangrador-Vegas A, Scheremetjew M, Yong S-Y, Lopez R, Hunter S. 2014. InterProScan 5: genome-scale protein function classification. Bioinformatics 30:1236–1240.

13- Menzel P, Ng KL, Krogh A. 2016. Fast and sensitive taxonomic classification for metagenomics with Kaiju. Nature Communications 7:11257.

14- Alneberg J, Bjarnason BS, de Bruijn I, Schirmer M, Quick J, Ijaz UZ, Lahti L, Loman NJ, Andersson AF, Quince C. 2014. Binning metagenomic contigs by coverage and composition. Nature Methods 11:1144.

15- Campbell JH, O’Donoghue P, Campbell AG, Schwientek P, Sczyrba A, Woyke T, Söll D, Podar M. 2013. UGA is an additional glycine codon in uncultured SR1 bacteria from the human microbiota. PNAS 110:5540–5545.

16- Segata N, Izard J, Waldron L, Gevers D, Miropolsky L, Garrett WS, Huttenhower C. 2011. Metagenomic biomarker discovery and explanation. Genome Biology 12:R60.







import pandas as pd

base_path = '~/tfprojects/pnet_prostate_paper_external/_database/prostate/raw_data/brca/brca_mbcproject_2022/'



def gen_genes_list():
    express_file = "data_mrna_agilent_microarray.txt"
    gene_selected = "expressed_genes.csv"
    df1= pd.read_csv(base_path+express_file,sep="\t")
    genes = list(df1["Hugo_Symbol"])
    with open(gene_selected,"w") as f:
        f.write("genes"+"\n")
        for gene in genes:
            f.write(gene+"\n")

def gen_format_file():
    express_file = "data_cna.txt"
    #express_file = "data_methylation_hm450.txt"
    #final_cna = "data_methylation_hm450_processed.txt"
    final_cna = "data_cna_processed.txt"
    df1 = pd.read_csv( base_path+express_file, sep="\t", index_col='Hugo_Symbol')
    df1 = df1.drop(columns=['Cytoband'])
    df2= pd.DataFrame(df1.values.T, columns=df1.index, index=df1.columns)
    print(df2)
    df2.to_csv(final_cna,sep=",")


def caltotalsample():
    cna_file = "./raw/brca/data_cna.txt"
    express_file = "./raw/brca/data_mrna_agilent_microarray.txt"
    promoter_file = "./raw/brca/data_methylation_promoters_rrbs.txt"
    mutation_file = "./raw/brca/data_mutations.txt"
    df1 = pd.read_csv(cna_file,sep='\t')
    df2 = pd.read_csv(express_file,sep='\t')
    df3 = pd.read_csv(promoter_file,sep='\t')
    df4 = pd.read_csv(mutation_file,sep='\t')
    df1 = df1.drop(columns=['Hugo_Symbol','Entrez_Gene_Id'])
    s_df1 = set(df1.columns)
    df2 = df2.drop(columns=['Hugo_Symbol', 'Entrez_Gene_Id'])
    s_df2 = set(df2.columns)
    df3 = df3.drop(columns=['Hugo_Symbol'])
    s_df3 = set(df3.columns)
    s_df4 = set(df4['Tumor_Sample_Barcode'])
    s_df = set.intersection(s_df1,s_df2,s_df3,s_df4)
    print(len(s_df1),len(s_df2),len(s_df3),len(s_df4),len(s_df))


def gen_mutation_file():
    mutation_file = "data_mutations.txt"
    df1 = pd.read_csv(base_path+mutation_file,sep='\t',index_col='Hugo_Symbol')
    df2 = df1['Tumor_Sample_Barcode']
    samples = list(set(df2))
    genens = list(set(df1.index))
    new_df = pd.DataFrame(index=samples,columns=genens,data=0)
    for idx in range(len(list(df1.index))):
        g = df1.index[idx]
        s = df2[idx]
        new_df.loc[s,g] = 1
    new_df.to_csv("data_mutations_processed.csv",sep=",")

def ge_response_file():
    er_status_file = "./raw/brca/ER_STATUS.txt"
    df1 = pd.read_csv(er_status_file,sep='\t',index_col='ids')
    df1.to_csv("ER_STATUS.csv",sep=",")




def compare():
    df1 = pd.read_csv("breast_data_cna.csv")
    df2 = pd.read_csv("data_cna_processed.txt")
    col1 = set(df1.columns)
    col2 = set(df2.columns)
    # aa=col1.union(col1)-col1.intersection(col2)
    aa = col1-col2
    print(aa)
    print(len(aa),len(col1),len(col2))

    df1 = pd.read_csv("breast_data_mutations.csv")
    df2 = pd.read_csv("data_mutations_processed.csv")
    col1 = set(df1.columns)
    col2 = set(df2.columns)
    # aa=col1.union(col1)-col1.intersection(col2)
    aa = col1-col2
    print(aa)
    print(len(aa),len(col1),len(col2))

if __name__=="__main__":
    compare()
    #ge_response_file()
    #gen_format_file()
    #gen_mutation_file()
    #caltotalsample()
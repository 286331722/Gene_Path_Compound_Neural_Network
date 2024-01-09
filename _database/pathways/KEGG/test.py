import pandas as pd
import tensorflow as tf


df = pd.DataFrame(0,index=[1,2,3],columns=[4,5,6])
df.loc[1,4]=1


file = "gens.csv"
df = pd.read_csv(file,header=None,index_col=0,sep="\t")
col = df.index
a=set(col)
file = "breast_expressed_genes.csv"
df = pd.read_csv(file,header=None,index_col=0)
col = df.index
b=set(col)

c = set.union(a,b)
c=list(c)
with open('breast_expressed_genes_select.csv', mode='w') as f:
    for i in c:
        f.write(str(i)+"\n")




#m = tf.keras.metrics.binary_accuracy([[1], [2], [3], [4]], [[0], [2], [3], [4]])
#m.update_state([[1], [2], [3], [4]], [[0], [2], [3], [4]])
#print m.result().numpy()


from keras import backend as K
import tensorflow as tf
import tensorflow as tf
import numpy as np

# taken from https://stackoverflow.com/questions/43547402/how-to-calculate-f1-macro-in-keras
def f1(y_true, y_pred):
    def recall(y_true, y_pred):
        """Recall metric.

        Only computes a batch-wise average of recall.

        Computes the recall, a metric for multi-label classification of
        how many relevant items are selected.
        """
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

    def precision(y_true, y_pred):
        """Precision metric.

        Only computes a batch-wise average of precision.

        Computes the precision, a metric for multi-label classification of
        how many selected items are relevant.
        """
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision


    precision = precision(y_true, y_pred)
    recall = recall(y_true, y_pred)
    return 2 * ((precision * recall) / (precision + recall + K.epsilon()))

y_true = tf.constant([[1.0,0.0,1.0]])
y_pred = tf.constant([1.0,0.0,1.0])
print y_pred,y_true.numpy()
print f1(y_true,y_pred)






file_path_gen = 'paths.csv'
file_path_cmp = ''
df = pd.read_csv(file_path_gen,header=None,index_col=0)

c=('a','b','c')
r=[5,6,7,8]
df1 = pd.DataFrame(index=c,columns=r)
df1[df1!=0]=0.0
df1.loc['a',5]=8

a = df1[[5,7]]

for i,r in df1.iterrows():
    print(i,r.get(5))


#1. path and cmp index
    #2. two df: gen-path, path-cmp
    from config_path import *

    pathway_path = PATHWAY_PATH
    processed_path = join(pathway_path, 'KEGG')
    file_paths = join(processed_path, 'paths.csv')
    file_cmps = join(processed_path, 'cmps.csv')
    file_path_gen = join(processed_path, 'path-gen.csv')
    file_path_cmp = join(processed_path, 'path-cmp.csv')

    df_path = pd.read_csv(file_paths, header=None, index_col=0)
    df_cmps = pd.read_csv(file_cmps, header=None, index_col=0)
    paths = df_path.index
    cmps = df_cmps.index
    df_gene_path = pd.DataFrame(index=genes, columns=paths)
    df_gene_path[df_gene_path != 0] = 0.0
    df_path_cmp = pd.DataFrame(index=paths, columns=cmps)
    df_path_cmp[df_path_cmp != 0] = 0.0

    df_gen_path_temp = pd.read_csv(file_path_gen, header=None, index_col=0)
    for i, r in df_gen_path_temp.iterrows():
        row = i
        col = r.get(0)
        df_gene_path.loc[row,col]=1.0

    df_path_cmp_temp = pd.read_csv(file_path_cmp, header=None, index_col=0)
    for i, r in df_path_cmp_temp.iterrows():
        row = i
        col = r.get(0)
        df_path_cmp.loc[row,col]=1.0
    maps = []

    maps.append(df_gene_path)
    maps.append(df_path_cmp)
    print 'gene_path_map', df_gene_path.shape
    print 'path_cmp_map', df_path_cmp.shape


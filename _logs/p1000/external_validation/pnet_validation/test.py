from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from utils.plots import plot_confusion_matrix
cnf_matrix=np.array([[33,17],[14,37]])
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=['Positive', 'Negative'],
                                  title='Confusion matrix, without normalization')
file_name = "confusion_normalized_P-net__mets.png"
plt.savefig(file_name)

plt.figure()
plot_confusion_matrix(cnf_matrix, normalize=True, classes=['Positive', 'Negative'],
                                  title='Normalized confusion matrix')
file_name = "confusion_P-net__mets.png"
plt.savefig(file_name)
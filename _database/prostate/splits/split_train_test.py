import pandas as pd



def divid_train_test_valid():
    file = "breast_response.csv"
    df = pd.read_csv(file,sep=',')
    test = []
    train = []
    val = []
    for i in range(len(df.index)):
        if i%20 == 2 or i%20 == 3:
            test.append(i)
        elif i%20 == 4:
            val.append(i)
            #train.append(i)
        else:
            train.append(i)

    df_test = df.loc[test]
    df_train = df.loc[train]
    df_val = df.loc[val]

    df = pd.DataFrame(df_test.values)
    df.to_csv("test_set.csv")
    df = pd.DataFrame(df_train.values)
    df.to_csv("training_set.csv")
    df = pd.DataFrame(df_val.values)
    df.to_csv("validation_set.csv")


def divid_train_20():
    trains = []
    file = "training_set.csv"
    df = pd.read_csv(file, sep=',')
    for i in range(20):
        trains.append([]);

    for i in range(len(df.index)):
        row = i%20
        trains[row].append(i)

    idx=[]
    for j in range(20):
        idx=idx+trains[j]
        df_train = df.loc[idx]
        df1 = pd.DataFrame(df_train.values)
        df1.columns=['','id','response']
        df1.to_csv('training_set_{}.csv'.format(19-j),columns=['id','response'])

if __name__=='__main__':

    #divid_train_test_valid()
    divid_train_20()





import pandas as pd
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings("ignore")

df = pd.read_pickle('C:\\Users\\eitan\\Downloads\\masters\\x_y_cnbc.pkl', compression='xz', storage_options=None)

df.fillna(0, inplace=True)

df.to_csv('C:\\Users\\eitan\\Downloads\\masters\\x_y_cnbc.csv')
print(df.shape)

sectors = ["XLE","XLB","XLI","XLY","XLP","XLV","XLF","XLK","VOX","XLU","VNQ"]
lst = []
for sector in sectors:
    lst.append(str(sector + " change"))
y_df = pd.DataFrame(df[lst])
x_df = df.drop(lst, axis=1)

y_df[y_df <= 0] = -1
y_df[y_df > 0] = 1
x_df = x_df['2006-09-30':'2019-1-31']
y_df = y_df['2006-09-30':'2019-1-31']

train_x = x_df['2006-09-30':'2011-12-31']
test_x = x_df['2012-1-1':'2014-12-31']
validation_x = x_df['2015-1-1':'2019-1-31']
dates = test_x.index
dates2 = x_df.index
dates3 = validation_x.index
train_y = y_df['2006-09-30':'2011-12-31']
test_y  = y_df['2012-1-1':'2014-12-31']
validation_y = y_df['2015-1-1':'2019-1-31']

train_xle = train_y["XLE change"]
test_xle = test_y["XLE change"]
validation_xle = validation_y["XLE change"]
all_xle = y_df["XLE change"]
train_xlb = train_y["XLB change"]
test_xlb = test_y["XLB change"]
validation_xlb = validation_y["XLB change"]
all_xlb = y_df["XLB change"]
train_xli = train_y["XLI change"]
test_xli = test_y["XLI change"]
validation_xli = validation_y["XLI change"]
all_xli = y_df["XLI change"]
train_xly = train_y["XLY change"]
test_xly = test_y["XLY change"]
validation_xly = validation_y["XLY change"]
all_xly = y_df["XLY change"]
train_xlp = train_y["XLP change"]
test_xlp = test_y["XLP change"]
validation_xlp = validation_y["XLP change"]
all_xlp = y_df["XLP change"]
train_xlv = train_y["XLV change"]
test_xlv = test_y["XLV change"]
validation_xlv = validation_y["XLV change"]
all_xlv = y_df["XLV change"]
train_xlf = train_y["XLF change"]
test_xlf = test_y["XLF change"]
validation_xlf = validation_y["XLF change"]
all_xlf = y_df["XLF change"]
train_xlk = train_y["XLK change"]
test_xlk = test_y["XLK change"]
validation_xlk = validation_y["XLK change"]
all_xlk = y_df["XLK change"]
train_vox = train_y["VOX change"]
test_vox = test_y["VOX change"]
validation_vox = validation_y["VOX change"]
all_vox = y_df["VOX change"]
train_xlu = train_y["XLU change"]
test_xlu = test_y["XLU change"]
validation_xlu = validation_y["XLU change"]
all_xlu = y_df["XLU change"]
train_vnq = train_y["VNQ change"]
test_vnq = test_y["VNQ change"]
validation_vnq = validation_y["VNQ change"]
all_vnq = y_df["VNQ change"]

train_Y_lst = [train_xle,train_xlb, train_xli, train_xly, train_xlp,
               train_xlv, train_xlf, train_xlk, train_vox, train_xlu, train_vnq]
test_Y_lst = [test_xle,test_xlb, test_xli, test_xly, test_xlp,
               test_xlv, test_xlf, test_xlk, test_vox, test_xlu, test_vnq]
validation_Y_lst = [validation_xle,validation_xlb, validation_xli, validation_xly, validation_xlp,
               validation_xlv, validation_xlf, validation_xlk, validation_vox, validation_xlu, validation_vnq]

all_Y_lst = [all_xle,all_xlb, all_xli, all_xly, all_xlp,
               all_xlv, all_xlf, all_xlk, all_vox, all_xlu, all_vnq]


def computing_confusion_matrices(train_x,test_x,trains_y,tests_y,names):

    rc = RidgeClassifier(alpha=1)

    param = {}
    param['booster'] = 'gbtree'
    param['objective'] = 'binary:logistic'
    param["eval_metric"] = "error"
    param['eta'] = 0.3
    param['gamma'] = 0
    param['max_depth'] = 6
    param['min_child_weight'] = 1
    param['max_delta_step'] = 0
    param['subsample'] = 1
    param['colsample_bytree'] = 1
    # param['silent'] = 1
    param['seed'] = 0
    param['base_score'] = 0.5

    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(train_x)
    X_test = sc_X.transform(test_x)

    logistic_regression_classifier = LogisticRegressionCV(cv=3)
    elastic_net_classifier = LogisticRegressionCV(cv=3, penalty='elasticnet', l1_ratios=[0.1, 0.5, 0.75], solver='saga')

    predicted_months = pd.DataFrame()
    for l in range(0,len(trains_y)):
        sector = str(names[l])

        rc.fit(train_x, trains_y[l])
        predicted_ridge = rc.predict(test_x)
        R = str(sector + 'ridge')
        print(len(predicted_ridge))
        print(len(tests_y[l]))
        cr = classification_report(tests_y[l], predicted_ridge)
        print(R)
        print(cr)

        model = XGBClassifier(**param)
        model.fit(train_x, trains_y[l])
        y_pred = model.predict(test_x)
        predicted_xgboost = [round(value) for value in y_pred]
        XGB = str(sector+'xgboost')
        cr = classification_report(tests_y[l], predicted_xgboost)
        print(XGB)
        print(cr)

        logistic_regression_classifier.fit(train_x, trains_y[l])
        logistic_predicted = logistic_regression_classifier.predict(test_x)
        LOG = str(sector+"Logistic Regression")
        cr = classification_report(tests_y[l], logistic_predicted)
        print(LOG)
        print(cr)

        elastic_net_classifier.fit(train_x, trains_y[l])
        elastic_predicted = elastic_net_classifier.predict(test_x)
        E = str(sector+"Elastic Net with L1 penalty")
        cr = classification_report(tests_y[l], elastic_predicted)
        print(E)
        print(cr)

        clf = RandomForestClassifier(max_depth=2, random_state=0)
        clf.fit(train_x, trains_y[l])
        rf_predicted = clf.predict(test_x)
        RF = str(sector + "Random Forest")
        cr = classification_report(tests_y[l], rf_predicted)
        print(RF)
        print(cr)

        class_df = pd.DataFrame(list(zip(predicted_ridge, predicted_xgboost, logistic_predicted, elastic_predicted, rf_predicted)),
                                      columns=[R, XGB, LOG, E, RF])
        # print(class_df.head())
        predicted_months = pd.concat([predicted_months, class_df],axis=1)
    return predicted_months

predicted_months = computing_confusion_matrices(train_x=train_x,test_x=test_x,trains_y=train_Y_lst,tests_y=test_Y_lst, names=sectors)
print(predicted_months.shape)
predicted_months["index"] = dates
predicted_months.set_index(predicted_months['index'], inplace=True)
predicted_months.to_csv('C:\\Users\\eitan\\Downloads\\masters\\predicted_sectors_cnbc.csv')
predicted_validation_months = computing_confusion_matrices(train_x=train_x,test_x=validation_x,trains_y=train_Y_lst,tests_y=validation_Y_lst, names=sectors)
predicted_validation_months["index"] = dates3
predicted_validation_months.set_index(predicted_validation_months['index'], inplace=True)
predicted_validation_months.set_index(predicted_validation_months['index'], inplace=True)
predicted_validation_months.to_csv('C:\\Users\\eitan\\Downloads\\masters\\predicted_sectors_cnbc_validation.csv')
# print(x_df.shape)
# print(y_df.shape)
predicted_all_months = computing_confusion_matrices(train_x=train_x,test_x=x_df,trains_y=train_Y_lst,tests_y=all_Y_lst, names=sectors)
predicted_all_months["index"] = dates2
predicted_all_months.set_index(predicted_all_months['index'], inplace=True)
predicted_all_months.set_index(predicted_all_months['index'], inplace=True)
predicted_all_months.to_csv('C:\\Users\\eitan\\Downloads\\masters\\predicted_sectors_cnbc_for_all.csv')



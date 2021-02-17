from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from collections import Counter
from imblearn.over_sampling import RandomOverSampler

def fahrenheit_to_celsius(tempinF):
    tempinC = round((tempinF -32)*(5/9),2)
    return tempinC
def inches_to_cm(inch):
    mm = round(inch * 25.4,2)
    return mm

dataset = read_csv('Clear_Data_20192020_1.csv')
dataset.drop(["Unnamed: 0"], axis = 1, inplace = True)
print(dataset)
print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())

array = dataset.values
X = array[:,0:5]
print(X)
y = array[:,5]
print(y)
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)


model =  DecisionTreeRegressor()
model.fit(X_train,Y_train)
predicts= model.predict(X_validation)



dataset_forecast = read_csv('Weather_Forecast_Clear_As_Input.csv')
dataset_forecast['Temperature'] = dataset_forecast['Temperature'].apply(fahrenheit_to_celsius)
dataset_forecast['Precipitation'] = dataset_forecast['Precipitation'].apply(inches_to_cm)
array1 = dataset_forecast.values
print(array1)
X1 = array1[:,1:6]
print(X1)

print(model.predict([[3.2,5,9,0,958]]))


fileObject = open("ML_report.txt", "w")
fileObject.write(str(model.predict([[3.2,5,9,0,958]])))
fileObject.close()
    
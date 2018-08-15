import pandas as pd

visits = pd.read_csv('visits.csv')
application=pd.read_csv("applications.csv")
fitness_test=pd.read_csv("fitness_tests.csv")
purchases=pd.read_csv("purchases.csv")


print visits.head(5)
print application.head(5)
print fitness_test.head(5)
print purchases.head(5)

print visits.describe()
print application.describe()
print fitness_test.describe()
print purchases.describe()

print purchases["purchase_date"].describe()
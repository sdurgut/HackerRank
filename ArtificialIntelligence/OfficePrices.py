# https://www.hackerrank.com/challenges/predicting-office-space-price/problem

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import numpy as np



def main():
	f,n = map(int,input().strip().split())

	model = Pipeline([
		('poly',PolynomialFeatures(degree = 3)),
		('linear',LinearRegression(fit_intercept = False))
		])

	train = [map(float, input().split()) for i in range(n)]
	X_train = []
	y_train = []
	for row in train:
		tmp = [i for i in row]
		X_train.append( tmp[:-1] )
		y_train.append( tmp[-1:] )

	model.fit(X_train, y_train)


	n = int(input().strip())
	test = [map(float, input().split()) for i in range(n)]
	X_test = []
	for row in test:
		X_test.append( [i for i in row] )


	predictions =  model.predict(X_test)
	for p in predictions:
		print (p[0])

if __name__ == '__main__':
	main()
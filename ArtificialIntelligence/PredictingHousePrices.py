# https://www.hackerrank.com/challenges/predicting-house-prices/problem
from sklearn import linear_model


def main():
	f,n = map(int,input().strip().split())
	train = [map(float,input().strip().split()) for i in range(n)]
	X_train  = []
	y_train = []
	for row in train:
		tmp = [i for i in row]
		X_train.append( tmp[:-1] )
		y_train.append( tmp[-1:] )

	n = int(input().strip())
	test = [map(float,input().strip().split()) for i in range(n)]
	X_test = []
	for row in test:
		X_test.append( [i for i in row] )

	clf = linear_model.Lasso(alpha=0.1)
	clf.fit(X_train,y_train)
	predictions =  clf.predict(X_test)
	for p in predictions:
		print(p)

if __name__ == '__main__':
	main()
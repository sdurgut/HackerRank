# from sklearn.tree import DecisionTreeRegressor
# from sklearn.linear_model import Lasso
# from sklearn.linear_model import Ridge
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

def main():
	nMonths = 12
	nTestCase = int(input().strip())
	monthArray = []
	X_train = []
	y_train = []
	X_test = []

	# build y_train
	for i in range(nTestCase):
		line = input().strip()
		y_train.append( int(line.split("\t")[1]) )
		monthArray.append( int( line.split("\t")[0].split("_")[1] ) )

	y_max = max(y_train)
	y_train = [i/y_max for i in y_train]

	# build X_train
	for month in monthArray:
		remainder = month%12
		tmp = [0 for x in range(12)]
		tmp[remainder] = 1
		# tmp.append(month)
		X_train.append(tmp)

	# build X_test for the next 12 months
	monthArray_test = [x for x in range(monthArray[-1],monthArray[-1]+12)]
	for month in monthArray_test:
		remainder = month%12
		tmp = [0 for x in range(12)]
		tmp[remainder] = 1
		# tmp.append(month)
		X_test.append(tmp)


	# regressor = DecisionTreeRegressor(random_state=0)
	# regressor = GradientBoostingRegressor('n_estimators': 800, 'max_depth': 8, 'min_samples_split': 2, 'learning_rate': 0.01, 'loss': 'ls')
	# params = {'n_estimators': 800, 'max_depth': 8, 'min_samples_split': 2, 'learning_rate': 0.01, 'loss': 'ls'}
	# regressor = GradientBoostingRegressor(**params)
	# regressor = RandomForestRegressor(max_depth=2, random_state=0)
	# regressor = Lasso(alpha = 1.0)
	# regressor = Ridge(alpha=1.0)
	regressor = KNeighborsRegressor(n_neighbors = 3)


	regressor.fit(X_train,y_train)
	myPrediction = regressor.predict(X_test)
	for i in myPrediction:
		print(i*y_max)


if __name__ == "__main__":
	main()

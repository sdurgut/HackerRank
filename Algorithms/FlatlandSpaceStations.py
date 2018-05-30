#!/bin/python3
# https://www.hackerrank.com/challenges/flatland-space-stations/problem

import sys

def flatlandSpaceStations(n, c):
	cityLocations = list(range(n))
	stationLocations = c
	maxDistances = []
	for ct in cityLocations:
		dists = []
		for st in stationLocations:
			dists.append(abs(ct-st))
		maxDistances.append(min(dists))


	return max(maxDistances)




if __name__ == "__main__":
	n, m = input().strip().split(' ')
	n, m = [int(n), int(m)]
	c = list(map(int, input().strip().split(' ')))
	result = flatlandSpaceStations(n, c)
	print(result)

import math
def canCollide(R1,R2,position1,position2):
	distance  = math.sqrt ((position2[0] - position1[0])**2 + (position2[1] - position1[1])**2 + (position2[2] - position1[2])**2)
	if distance <= (R1+R2):
		return "YES"
	else:
		return "NO"


def getPosition(position,acceleration,time):
	xf = position[0] + 0.5*acceleration[0]*time*time
	yf = position[1] + 0.5*acceleration[1]*time*time
	zf = position[2] + 0.5*acceleration[2]*time*time

	return [xf,yf,zf]


def propagateInTime(R1,R2,position1,acceleration1, position2, acceleration2):
	for time in range(10000):
		deltaTime = 0
		if time>0:
			deltaTime = 1
		# time is continuous
		for i in range (10):
			timeStamp = 0.1*i
			pos1 = getPosition(position1,acceleration1,time+timeStamp)
			pos2 = getPosition(position2,acceleration2,time+timeStamp)
			result = canCollide(R1,R2,pos1,pos2)
			if result == "YES":
				return "YES"
	return "NO"



def spheres(inputValues):
	for case in inputValues:
		R1 = case["Radius"][0]
		R2 = case["Radius"][1]
		position1 = case["Position1"]
		acceleration1 = case["Acceleration1"]
		position2 = case["Position2"]
		acceleration2 = case["Acceleration2"]

		print ( propagateInTime(R1,R2,position1,acceleration1, position2, acceleration2)  )




if __name__ == "__main__":
	nTestCase = int(input())
	inputValues = []
	for i in range(nTestCase):
		case = {}
		radiuses = [int(i) for i in input().strip().split()]
		position1 = [int(i) for i in input().strip().split()]
		acceleration1 = [int(i) for i in input().strip().split()]
		position2 = [int(i) for i in input().strip().split()]
		acceleration2 = [int(i) for i in input().strip().split()]
		case["Radius"] = radiuses
		case["Position1"] = position1
		case["Acceleration1"] = acceleration1
		case["Position2"] = position2
		case["Acceleration2"] = acceleration2
		inputValues.append(case)
	# print (inputValues)
	spheres(inputValues)



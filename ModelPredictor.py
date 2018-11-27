import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow.keras as keras

def convertToCategoricalValues(arr):
	i = 1
	dic = {}
	CategoricalArr = []
	for item in arr:
		if not item in dic:
			dic[item] = i
			i += 1
		CategoricalArr.append(dic[item])
	return np.asarray(CategoricalArr)
def ticketInfoToData(ticketArr):
	ticketLocation = []
	ticketNumber = []
	for ticketInfo in ticketArr:
		splitInfo = ticketInfo.split(" ")
		print(splitInfo)
		if(len(splitInfo) > 1):
			locationInfo = ""
			for locationData in splitInfo[0:-1]:
				locationInfo += locationData
			ticketLocation.append(locationInfo)
			ticketNumber.append(int(splitInfo[-1]))
		elif(splitInfo[0] == "LINE"):
			ticketLocation.append(splitInfo[0])
			ticketNumber.append(0)
		else:
			ticketLocation.append("N/A")
			ticketNumber.append(int(splitInfo[0]))
	return convertToCategoricalValues(ticketLocation),ticketNumber
if __name__ == "__main__":
	df = pd.read_csv("train.csv")
	print(df)
	X = np.asarray(df.drop(["Survived"],axis=1).values)
	y = np.asarray(df["Survived"])
	genders = np.asarray(df["Sex"])
	ticketArr = np.asarray(df["Ticket"])
	arr1,arr2 = ticketInfoToData(ticketArr)
	print(arr1)
	print(arr2)
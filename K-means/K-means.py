# thou shall not cross 80 columns in thy file

import csv
import random
import math
import matplotlib.pyplot as plot


centriod = list()   # Stores the coordinates of centriods we generate
clustered = list()  # Stores the clustered data in orderered form ,for plotting
newData = []        # Stores the type converted data
K = 3               # k is the number of clusters to be develped from the data


def cluster():
    "This function performs the k-means clustering algorithm"
    distance = [0]*K

    for val in newData:
        for i in range(0, K):
            distance[i] = euclideanDistance(centriod[i], val)
            # Only this statement should be in the inner loop
            '''
            Here I am calculating the distance between centriod & each
            value to classify them into differnt clusters
            '''
        minIndex = distance.index(min(distance))  # Both of these should be
        clustered[minIndex].append(val)           # should be in the outer loop


def euclideanDistance(p, q):
    "This calculates the Euclidean Distance b/w p & q, in the standard way"
    distance = math.sqrt(((p[0]-q[0])**2) + ((p[1]-q[1])**2))
    return distance


def parse():
    "Parses the data sets from the csv file we are given to work with"
    file = open("exercise-3.csv")  # should be manualized later
    rawFile = csv.reader(file)    # Reading the csv file into a raw form
    rawData = list(rawFile)       # Converting the raw data into list from.
    return rawData
    '''
    Csv reader reads the file line by line, and for the files
    that are given to us first line is always meta data and we don't want
    that to be taken into clustering as well. Which is why we use the list
    from index 1 rather than 0.
    Since we have 2 columns, when converted into list/array it is 2D list.
    Here, index 0 in each line is x-coordinate, index 1 is the y-coordinate
    '''


def draw(xCords, yCords, xLabel, yLabel, clusterLabel, pointerColor):
    "This method draws the clusterd plot using Matplotlib"
    plot.xlabel(xLabel)
    plot.ylabel(yLabel)
    plot.title("Initial Plot")
    plot.scatter(xCords, yCords, color=pointerColor, s=10, label=clusterLabel)
    plot.legend()


def kFinder():
    "This finds the apt K value from the given cluster using gap-statistics"
    return 0
    # TODO


def MeanCords(groupedCords):
    "This finds the mean of the clusters to reassign the centriods"
    listSize = len(groupedCords)
    total = 0
    for i in range(0, listSize):
        total += groupedCords[i] # Only this statement is in the loop BTW
    avg = total/listSize
    return avg  # Return the mean of the x or y co-ordinates


def toXandY(unorderedData):
    "This method converts seperates x and y co-ordinates for plotting"
    orderedData = []
    orderedData.append([])        # Add a new sublsit every time
    orderedData.append([])        # Add a new sublsit every time
    listSize = len(unorderedData)
    for x in range(0, listSize):
        orderedData[0].append(unorderedData[x][0])  # Seperates the x-cords
    for y in range(0, listSize):
        orderedData[1].append(unorderedData[y][1])  # Seperates the y-cords
    return orderedData


def main():
    "This is the main method were execusion begins"
    names = ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]
    color = ["r", "g", "b", "m", "c"]  # Stores the color values
    data = parse()
    labels = data.pop(0)
    listSize = len(data)

    for i in range(K):
        clustered.append([]) # Making a sublist for every cluster

    for i in range(0, listSize):    # Converting the string list to float
        newData.append([])          # Add a new sublsit every time
        for j in range(0, 2):       # Append converted data to the new list
            newData[i].append(float(data[i][j]))

    # These are the randomly picked centroids, should be re-calculated later
    for i in range(0, K):
        centriod.append(random.choice(newData))

    cluster() # Executes the algorithm

    # Now we plot them
    for i in range(0, K):
        clustered[i] = toXandY(clustered[i])
        draw(clustered[i][0], clustered[i][1],
             labels[0], labels[1], names[i], color[i])

    plot.show() # Shows the graph that is drawn in memory


if __name__ == "__main__":
    main()

from matplotlib import pyplot
import numpy

#randint() will generate 20 numbers from 1-99, store output in list named numList
numList = numpy.random.randint(100, size = 20)
#print to console for testing
print("the list of numbers we generated is:", numList)

#this creates a graphical window of size 10 inches by 5 inches:
screen = pyplot.figure(figsize =(10, 5))

#1) set up a histogram, let pyplot use default bins
#pyplot.hist(numList)
#2)set up a histogram, set number of bins:
#pyplot.hist(numList, 10)
#3) set up a histogram, set edges of bins:
pyplot.hist(numList, bins = [0, 25, 50, 75, 100])
pyplot.hist(numList)
pyplot.hist(numList, 10)


#set title
pyplot.title("amazing histogram ig")

#show plot
pyplot.show()

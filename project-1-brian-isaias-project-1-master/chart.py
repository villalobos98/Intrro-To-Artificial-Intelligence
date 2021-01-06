'''
All these functions are helper functions that will be called from another file by being imported
The following are examples of helper functions: such as createChart(), display(), and createBarChart()
'''
import time
import matplotlib.pyplot as plot
import pandas as pd
import asteroids_ga as ga
import asteroids_sa as sa
import asteroids_ta as ta

'''
@param treeSearchList: A list that should have times for solving the asteroids problem using Tree Search
@param simmulatedAnnealingList: A list that should have times for solving the asteroids problem using Simmulated Annealing
@param geneticAlgorithmList: A list that should have times for solving the asteroids problem using Genetic Algorithm
@note: This function MUST have the SAME LENGTH LISTS
'''
def createChart(numGames, treeSearchList, simulatedAnnealingList, geneticAlgorithmList):
    data = {'Game #': [x for x in range(numGames)],
            'Tree Search': [treeSearchList[x] for x in range(len(treeSearchList))],
            'Simulated Annealing': [simulatedAnnealingList[x] for x in range(len(simulatedAnnealingList))],
            'Genetic Algorithms': [geneticAlgorithmList[x] for x in range(len(geneticAlgorithmList))]
            }
    df = pd.DataFrame(data, columns=["Game #", "Tree Search", "Simulated Annealing", "Genetic Algorithms"])
    return df


"""
@param dataframe: a Pandas data frame that contains all the times from the Tree Search, Annealing, or Genetic Algorithms
@desc: does not return anything, simply prints chart
"""
def displayChart(dataframe):
    print(dataframe.to_string(index=False))

"""
@param dataframe: a Pandas data frame that contains all the times from the Tree Search, Annealing, or Genetic Algorithms
@desc: does not return anything, simply shows bar chart
"""
def createBarChart(dataframe, xAxisLabel, yAxisLabel, nameOfChart):
    barChart = dataframe[['Tree Search', 'Simulated Annealing', 'Genetic Algorithms']].plot(kind='bar',
                                                                                            title=nameOfChart,
                                                                                            legend=True)
    barChart.set_xlabel(xAxisLabel, fontsize=12)
    barChart.set_ylabel(yAxisLabel, fontsize=12)
    plot.savefig(str(nameOfChart) + ".pdf")
    plot.show(block=True)


def createBoxPlot(dataframe, xAxis, yAxis, numberOfGames, a, b, c):
    myDict = {}
    string = "Game "

    gameDict = {}
    for i in range(numberOfGames):
        a = [x for x in range(20)]
        b = [x for x in range(20)]
        c = [x for x in range(20)]

        gameDict[i] = [a, b, c]

    print(gameDict)

    d = {}
    for i in range(len(a)):
        if string + str(i) not in myDict:
            myDict[i] = [a, b[i], c[i]]

    fig, ax = plot.subplots()
    print(gameDict.values()[0])
    ax.boxplot(gameDict.values())
    ax.set_xticklabels(gameDict.keys())
    plot.title("Fuel used by End of Game")
    ax.set_xlabel("Game #")
    ax.set_ylabel("Fuel")
    print(myDict)
    plot.show(block=True)


"""
This functions is for testing purposes only.
The point is to generate arrays that are going to be used in the data visualization
"""
def createData(numberOfGames):
    treeStatsTuple = treeArray(numberOfGames)
    geneticStatsTuple = geneticArray(numberOfGames)
    simulatedStatsTuple = simulatedArray(numberOfGames)

    return treeStatsTuple, geneticStatsTuple, simulatedStatsTuple

"""
This function contains the statistics that are relevant to the Genetic Algorithm.
The statistics include, fuel, system time, and steps(path length)
It will also compute the average of those statistics 
"""
def geneticArray(numberOfGames):
    averageTimeList = []
    averageStepsList = []
    averageFuelList = []
    for i in range(numberOfGames):
        timeList = []
        stepsList = []
        fuelList = []
        start_time = time.time()
        gameString = "asteroid_game_" + str(i) + ".json"
        GA = ga.main(gameString)
        fuelAmount, steps = GA
        val = time.time() - start_time
        timeList.append(val)
        fuelList.append(fuelAmount)
        stepsList.append(len(steps))
        averageTimeList.append(sum(timeList) / len(timeList))
        if (len(stepsList) == 0):
            averageStepsList.append(0)
        else:
            averageStepsList.append(sum(stepsList) / len(stepsList))
        if (len(stepsList) == 0):
            averageFuelList.append(0)
        else:
            averageFuelList.append(sum(fuelList) / len(fuelList))

    return averageTimeList, averageStepsList, averageFuelList

"""
This function contains the statistics that are relevant to the Tree Search Algorithm.
The statistics include, fuel, system time, and steps(path length)
It will also compute the average of those statistics 
"""
def treeArray(numberOfGames):
    averageTimeList = []
    averageStepsList = []
    averageFuelList = []
    for i in range(numberOfGames):
        timeList = []
        stepsList = []
        fuelList = []
        start_time = time.time()
        gameString = "asteroid_game_" + str(i) + ".json"
        TA = ta.main(gameString)
        fuelAmount, steps = TA
        val = time.time() - start_time
        timeList.append(val)
        fuelList.append(fuelAmount)
        stepsList.append(len(steps))
        averageTimeList.append(sum(timeList) / len(timeList))
        if (len(stepsList) == 0):
            averageStepsList.append(0)
        else:
            averageStepsList.append(sum(stepsList) / len(stepsList))

        if (len(stepsList) == 0):
            averageFuelList.append(0)
        else:
            averageFuelList.append(sum(fuelList) / len(fuelList))

    return averageTimeList, averageStepsList, averageFuelList

"""
This function contains the statistics that are relevant to the Simulated Annealing Algorithm.
The statistics include, fuel, system time, and steps(path length)
It will also compute the average of those statistics 
"""
def simulatedArray(numberOfGames):
    averageTimeList = []
    averageStepsList = []
    averageFuelList = []
    for i in range(numberOfGames):
        timeList = []
        stepsList = []
        fuelList = []
        start_time = time.time()
        gameString = "asteroid_game_" + str(i) + ".json"
        SA = sa.main(gameString)
        fuelAmount, steps = SA
        val = time.time() - start_time
        timeList.append(val)
        fuelList.append(fuelAmount)
        stepsList.append(len(steps))
        averageTimeList.append(sum(timeList) / len(timeList))
        if (len(stepsList) == 0):
            averageStepsList.append(0)
        else:
            averageStepsList.append(sum(stepsList) / len(stepsList))
        if (len(stepsList) == 0):
            averageFuelList.append(0)
        else:
            averageFuelList.append(sum(fuelList) / len(fuelList))

    return averageTimeList, averageStepsList, averageFuelList

"""
The main driver of the code, that is going to use the GA stats, TA stats, SA stats to create
the Pandas dataframe, and display the chart, along with the visual representation, bar chart
"""
def main():
    numberOfGames = 25

    treeStatsTuple, geneticStatsTuple, simulatedStatsTuple = createData(numberOfGames)
    timeTA = treeStatsTuple[0]
    stepsTA = treeStatsTuple[1]
    fuelTA = treeStatsTuple[2]
    averageTimesArrayTA = timeTA
    averageStepsArrayTA = stepsTA
    averageFuelArrayTA = fuelTA

    timeGA = geneticStatsTuple[0]
    stepsGA = geneticStatsTuple[1]
    fuelGA = geneticStatsTuple[2]
    averageTimesArrayGA = timeGA
    averageStepsArrayGA = stepsGA
    averageFuelArrayGA = fuelGA

    timeSA = simulatedStatsTuple[0]
    stepsSA = simulatedStatsTuple[1]
    fuelSA = simulatedStatsTuple[2]

    averageTimesArraySA = timeSA
    averageStepsArraySA = stepsSA
    averageFuelArraySA = fuelSA

    dataframeTime = createChart(numberOfGames, averageTimesArrayTA, averageTimesArrayGA, averageTimesArraySA)
    dataframeSteps = createChart(numberOfGames, averageStepsArrayTA, averageStepsArrayGA, averageStepsArraySA)
    dataframeFuel = createChart(numberOfGames, averageFuelArrayTA, averageFuelArrayGA, averageFuelArraySA)

    displayChart(dataframeTime)
    displayChart(dataframeSteps)
    displayChart(dataframeFuel)

    dataframeTime.to_html("time_used.html", index=False)
    dataframeSteps.to_html("step_taken.html", index=False)
    dataframeFuel.to_html("fuel_left.html", index=False)

    createBarChart(dataframeTime, "Game #", "System Time Used", "System Time Used")
    createBarChart(dataframeSteps, "Game #", "Fuel Used", "Fuel Remaining at End of Game")
    createBarChart(dataframeFuel, "Game #", "Steps Used", "Steps Lefts at the End of Game")


if __name__ == '__main__':
    main()

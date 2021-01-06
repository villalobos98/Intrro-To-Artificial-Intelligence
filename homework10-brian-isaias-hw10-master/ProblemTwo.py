import pandas as pd
def makeProbs():
    df = pd.read_csv("rearangedData.csv")
    countRSE = 0
    countEFalse = 0
    for i in df.values:
        g, s, t, l, r, e, o = i
        if r==True and s==True and e ==False:
            countRSE +=1
        if e == False:
            countEFalse += 1

    print(countRSE/countEFalse)

def main():
    makeProbs()
if __name__ == '__main__':
    main()

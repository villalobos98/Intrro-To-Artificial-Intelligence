import pandas as pd

def makeProbs():
    df = pd.read_csv("rearangedData.csv")
    countGST = 0
    countTS= 0
    for i in df.values:
        g, s, t, l, r, e, o = i

        if g == True and s == True and t==True:
            countGST += 1
        if t == True and s==True:
            countTS += 1
    print(countGST/countTS)

def main():
    makeProbs()
if __name__ == '__main__':
    main()

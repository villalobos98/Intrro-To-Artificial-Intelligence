import pandas as pd

def makeProbs():
    df = pd.read_csv("rearangedData.csv")
    countLGOT = 0
    countT= 0
    for i in df.values:
        g, s, t, l, r, e, o = i

        if l == True or g == True:
            if o == True:
                if t == True:
                    countLGOT += 1
        if t == True:
            countT += 1
    print(countLGOT/countT)

def main():
    makeProbs()

if __name__ == '__main__':
    main()

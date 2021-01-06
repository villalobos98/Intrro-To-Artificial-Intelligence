import pandas as pd

def makeProbs():
    df = pd.read_csv("rearangedData.csv")
    countRESOL = 0
    countSOL = 0
    for i in df.values:
        g, s, t, l, r, e, o = i
        if r == False and e == True and s == True and o == True and l == True:
               countRESOL += 1
        if s == True and o == True and l == True:
            countSOL += 1
    print(countRESOL/countSOL)

def main():
    makeProbs()

if __name__ == '__main__':
    main()

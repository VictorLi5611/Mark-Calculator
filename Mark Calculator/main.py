import markCalc
USER = input("Please enter your name:\n").upper()
COURSE_CODE = input("Please enter your course code:\n").upper()
ALL_MARKS = markCalc.getMarks("marks.csv")
data = []
find = {}
VALID_INPUT = [1,2,3,4]

def main():
    for eval in ALL_MARKS:
        currentMarks = eval.split(",")
        item, weight = currentMarks.pop(0).upper(), float(currentMarks.pop(0))
        total = markCalc.weightedAverage(currentMarks, weight)
        avg = markCalc.average(currentMarks)
        temp = [item, weight, avg, total]
        find[item] = [weight,avg,total]
        data.append(temp) 



    while True:
        inpt = int(input("SEE CURRENT PROGRESS PRESS 1, CALCULATE WHAT YOU NEED TO PASS PRESS 2, QUIT PRESS 3:\n"))
        if inpt not in VALID_INPUT:
            print("You entered an incorrect input, please try again.")
        else:
            if inpt == 1:
                markCalc.markBreakdown(data,USER,COURSE_CODE)
            elif inpt == 2:
                markCalc.passingMark(data,COURSE_CODE)
            elif inpt == 3:
                quit()

if __name__ == "__main__":
    main()
    




    
   








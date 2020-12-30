
def weightedAverage (marks , weight):
    if marks == [] or float(weight) <= 0:
        return 0
    total = 0
    for mark in marks:
        total += int(mark) 
        
    result = total // len(marks)
    return result * float(weight)

def average(marks):
    if marks == []:
        return 0
    total = 0
    for mark in marks:
        total += int(mark) 
        
    result = total // len(marks)
    return result

def getMarks(fileName):
    mark = []
    with open(fileName, "r") as f:
        for lines in f:
            mark.append(lines.strip())
    del mark[0]
    return mark

def markBreakdown(data,USER,COURSE_CODE):   
    print("\n\nCURRENT MARKS FOR {} IN {}\n".format(USER,COURSE_CODE))
    total = 0
    for eval in data:
        if eval[1] == 0 or eval[2] == 0:
            break
        else:
            total += eval[3]
            print("\t{} -> Weight {}, Average {}%, Weighted Average {}%\n".format(eval[0],eval[1],eval[2],eval[3]))
            print("Your total mark so far is {}%".format(int(total)))

def passingMark(data,COURSE_CODE):
    passingMark = int(input("What is the minimum passing mark?\n"))
    finalWeight = float(input("What is the Weight of the Final Exam (decimal form)\n"))
    total = 0
    for eval in data:
        total += eval[3]
    diff = passingMark - total
    toPass = (diff // finalWeight) + 1
    print("You will need to get {}% to pass {}".format(toPass,COURSE_CODE))
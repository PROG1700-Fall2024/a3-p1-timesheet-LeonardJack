#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:  W0499622  
#Student Name:  Jack Leonard

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    hours = []
    totalHours = 0
    for i in range(5):
        dayHour = int(input("Enter hours worked on day {0} ".format(i+1)))
        totalHours += dayHour
        hours.append(dayHour)

    print("----------------------------------------\nYour most hours worked was on:")
    mostHours = max(hours)
    for i in range(5):
        if hours[i] == mostHours :
            print("Day {0} where you worked for {1} hours".format(i+1, hours[i]))
    
    print("----------------------------------------\nYour total number of hours worked is {0}".format(totalHours))
    print("Your average hours worked was {}\n----------------------------------------".format(totalHours/5))
    print("Days you slacked off (worked less than 7 hours)")

    for i in range(5):
        if hours[i] < 7:
            print("Day {0} where you worked {1} hours".format(i+1, hours[i]))




    # YOUR CODE ENDS HERE

main()
#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:  W0499622  
#Student Name:  Jack Leonard

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    hours = [] #empty list, used for keeping track of our hours 
    totalHours = 0 #our total hours starts at zero
    for i in range(5):
        dayHour = int(input("Enter hours worked on day {0} ".format(i+1))) #collecting inputs by iterating through each work day (monday to friday)
        totalHours += dayHour #adds the hours to our total hours 
        hours.append(dayHour) #appends our hours value to our list

    print("----------------------------------------\nYour most hours worked was on:")
    mostHours = max(hours) #gets the highest number in the hours list 
    for i in range(5):
        if hours[i] == mostHours : # you will only go to the print statement if the given day you worked the most hours 
            print("Day {0} where you worked for {1} hours".format(i+1, hours[i])) #prints the day(s) you worked the most hours 
    
    print("----------------------------------------\nYour total number of hours worked is {0}".format(totalHours)) #prints total hours worked
    print("Your average hours worked was {}\n----------------------------------------".format(totalHours/5))# prints your average hours worked (is calculated in the format statement)
    print("Days you slacked off (worked less than 7 hours)") #this print statement precedes the next bit 

    for i in range(5):  #used to iterate through each day and print the days you slacked off
        if hours[i] < 7:    #you slacked off if you worked less than 7 hours
            print("Day {0} where you worked {1} hours".format(i+1, hours[i])) #formatted print statement




    # YOUR CODE ENDS HERE

main()
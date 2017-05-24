#S.McDonald 11/19/2016
#average_numbers
#show the contents of the file and compute the average


#define main
def main():
    try:
        #open the file numbers.txt
        #input
        #myfile is a file object
        myfile = open('numbers.txt', 'r') #open the file for reading

        #open the file for writing
        my_output_file = open('my_average.txt', 'w')

        total = 0 #start total count at 0

        #compute total and find average
        for line in myfile:
            total = total + int(line) #find the sum of all the numbers in the 'numbers.txt' file
            average = total / 10 #divide the sum of the numbers in the 'numbers.txt' file to find the average
            print(line, end="")

        #write to an output file
        my_output_file.write(str(average) + '\n')

        #close both files
        myfile.close()
        my_output_file.close()

    #exceptions
    except:
        print("ERROR! AN ERROR HAS OCCURED!") #if an error occurs, print this

    else:
        print("\nThe average is: ", average) #else, print the average of all the numbers in file

#call the main function
main()




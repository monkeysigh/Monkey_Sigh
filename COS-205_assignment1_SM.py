# futval_interest.py

def main():

    # User enters principal_amount. As we are dealing with strings, we then use float()
    ## to allow the program for arithmetic operations. I will store in numerical value.
    principal = float(input("Enter the principal amount: $"))

    # Works the same way as #6. the parenthesis used for as a decimal +Please give me feedback
    ## trying to understand why to the question.
    rate = float(input("Enter the yearly interest rate (as a decimal): "))

#Before we dealt with variables expressing a value that are usually deecimals.
##Now we will see INT( to facilitate the use of whole numbers.
    
    # Same as the input process as on lines 7 and 12. Here, we include the int( as a form of
    ##data type to allow the use of values/numbers that are more oftenly expressed in whole #'s.
    periods_per_year = int(input("Enter the number of compounding periods per year: "))

     # Same process as line 18. Applying the same reasoning for the application of INT( and not float(.
    years = int(input("Enter the duration in years: "))

    # By using the value of principal. We provide more clarity and help the loop execute using total_value
    ## to complete the calculation over the same initial investment. Total_value will now track
    ### the value of principal PLUS interests accrued.
    total_value = principal

    # How many times within the range we can the calculation to be perform. 
    for i in range(years * periods_per_year):
        # Will add the interests earned for this perior and include this value to
        ## total_value.
        total_value += total_value * (rate / periods_per_year)

    # Display the principal with calculated interests to  10 years.
    ## We intruduced f-strings and curly brackets to insert variables to be insert it into the string
    ###  Since we are working in values express in decimals, we include a format 2f, in order to
    ### observe the total value within this format. ONLY 2 decimals at the end. 
    print(f"The principal value after {years} years is: ${total_value:.2f}")
    
 ## It assures this file is being executed from within this shell. If it will be from the module, the system
    ## will fail to execute as it is not listed to the script. 
if __name__ == "__main__":
    main()

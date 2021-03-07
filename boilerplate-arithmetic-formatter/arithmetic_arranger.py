def arithmetic_arranger(problems,solve=False):


    def errors(problems,solve):
        if len(problems) > 5:
            return "Error: Too many problems."

    def split_input(problems):
        temp = ''
        arr_numbers = []  # for nums
        arr_operands = []  # for +/-

        for calculations in problems:  # seperates numbers and operands into seperate strings
            temp = calculations
            arr_numbers.append(temp.split())

        for i in range(len(arr_numbers)):  # isolate operands , then delete value in array
            arr_operands.append(arr_numbers[i][1])
            arr_numbers[i].pop(1)
        

        return arr_numbers,arr_operands
        


    def determine_dash(numbers):  # takes in array of the two numbers
    #dashes used in calculations are always 2 more than longest number
        def calculate(numbers):
            biggest = max(numbers, key=len)
            dash = '-'
            for i in range(len(biggest)+1):
                dash = dash + '-'
            return dash

        arr_dash = []
        for i in arr_numbers:  # array of dashes , correctly sized
            arr_dash.append(calculate(i))
            
        return arr_dash

    #["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
    #seperate the operands and numbers into seperate arrays

    def determine_spaces(arr_numbers,arr_dash):
        #spit arrays in top and bottom
        #minus num[i] from len dash[i] of same index
        #left over number = arr_spaces[i]
        
        arr_topnums = []
        arr_botnums = [] 

        for i in range(len(arr_numbers)): #split top and bottom numbers into arrays
            arr_topnums.append(arr_numbers[i][0])
            arr_botnums.append(arr_numbers[i][1])

        arr_toplen = [] 
        arr_botlen = []
        arr_topspaces = []
        arr_bottomspaces = []

        for i in range(len(arr_topnums)): #find the length of spaces in numbers
            arr_toplen.append(len(arr_dash[i]) - len(arr_topnums[i]))
            arr_botlen.append(len(arr_dash[i]) - len(arr_botnums[i]))

        for i in range(len(arr_toplen)): #convert spaces in numbers into spaces
            arr_topspaces.append(' '*arr_toplen[i])
            arr_bottomspaces.append(' '*arr_botlen[i])
        

        return arr_topspaces,arr_bottomspaces,arr_topnums,arr_botnums #return array of spaces for line 1 and 2
    

     
    line1 = '' #top numbers
    line2 = '' #operand and bottom numbers
    line3 = '' #dashes 
    line4 = '' #total of sum
    combinedline = ''


    '''
    ----------------
    Start of program
    ----------------
    '''
    arr_numbers,arr_operands = split_input(problems)
    print(arr_numbers)
    print(arr_operands)
    arr_dash = determine_dash(arr_numbers)
    print(arr_dash)
    arr_topspaces,arr_bottomspaces,arr_topnums,arr_bottomnums = determine_spaces(arr_numbers,arr_dash)


            


    # errors(problems,solve)
    # return arranged_problems
    
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])

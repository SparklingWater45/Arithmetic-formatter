def arithmetic_arranger(problems, solve=False):

    for i, problem in enumerate(problems):  # error checks
        num_top, operand, num_bot = problem.split()

        if len(problems) > 5:
            return "Error: Too many problems."
        if not operand in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not num_top.isdigit() or not num_bot.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num_top) > 4 or len(num_bot) > 4:
            return "Error: Numbers cannot be more than four digits."

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

        return arr_numbers, arr_operands

    def determine_sum(arr_numbers, arr_operands):
        arr_inttopnums = []
        arr_intbotnums = []
        arr_sum = []
        for i in range(len(arr_numbers)):  # split top and bottom strings into integers
            arr_inttopnums.append(int(arr_numbers[i][0]))
            arr_intbotnums.append(int(arr_numbers[i][1]))

        for i in range(len(arr_numbers)):
            if arr_operands[i] == '+':
                arr_sum.append(arr_inttopnums[i] + arr_intbotnums[i])
            else:
                arr_sum.append(arr_inttopnums[i] - arr_intbotnums[i])

        for i in range(len(arr_sum)):
            arr_sum[i] = str(arr_sum[i])  # change back to str

        return arr_sum

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

    def determine_spaces(arr_numbers, arr_dash, arr_sum):
        #spit arrays in top and bottom
        #minus num[i] from len dash[i] of same index
        #left over number = arr_spaces[i]s

        arr_topnums = []
        arr_botnums = []

        for i in range(len(arr_numbers)):  # split top and bottom numbers into arrays
            arr_topnums.append(arr_numbers[i][0])
            arr_botnums.append(arr_numbers[i][1])

        arr_toplen = []
        arr_botlen = []
        arr_topspaces = []
        arr_bottomspaces = []
        arr_sumlen = []
        arr_sumspaces = []

        for i in range(len(arr_topnums)):  # find the length of spaces in numbers
            arr_toplen.append(len(arr_dash[i]) - len(arr_topnums[i]))
            # -1 for operand taking 1 space positon
            arr_botlen.append(len(arr_dash[i]) - len(arr_botnums[i])-1)

            if '-' not in arr_sum[i]:
                arr_sumlen.append(len(arr_dash[i]) - len(arr_sum[i]))
            else:
                # for negative numbers
                arr_sumlen.append(len(arr_dash[i]) - len(arr_sum[i]))

        for i in range(len(arr_toplen)):  # convert spaces in numbers into spaces
            arr_topspaces.append(' '*arr_toplen[i])
            arr_bottomspaces.append(' '*arr_botlen[i])
            arr_sumspaces.append(' ' * arr_sumlen[i])

        # return array of spaces for line 1 and 2
        return arr_topspaces, arr_bottomspaces, arr_sumspaces, arr_topnums, arr_botnums

    def display_output(arr_topspaces, arr_bottomspaces, arr_sumspaces, arr_topnums, arr_bottomnums, arr_sum):
        line1 = ''  # top numbers
        line2 = ''  # operand and bottom numbers
        line3 = ''  # dashes
        line4 = ''  # total of sum

        for i in range(len(arr_topnums)-1):
            line1 = line1 + arr_topspaces[i] + arr_topnums[i] + '    '
            line2 = line2 + arr_operands[i] + arr_bottomspaces[i] + arr_bottomnums[i] + '    '
            line3 = line3 + arr_dash[i] + '    '
            line4 = line4 + arr_sumspaces[i] + arr_sum[i] + '    '
        
        line1 = line1 + arr_topspaces[len(arr_topnums)-1] + arr_topnums[len(arr_topnums)-1]
        line2 = line2 + arr_operands[len(arr_topnums)-1] + arr_bottomspaces[len(arr_topnums)-1] + arr_bottomnums[len(arr_topnums)-1]
        line3 = line3 + arr_dash[len(arr_topnums)-1]
        line4 = line4 + arr_sumspaces[len(arr_topnums)-1] + arr_sum[len(arr_topnums)-1]



        line1 = line1  # + '\n''
        line2 = line2  # + '\n'
        line3 = line3  # + '\n'
        final_output = line1 + '\n' + line2 + '\n' + line3

        if solve == False:  # if no sum required
            return final_output
        else:
            final_output = final_output + '\n' + line4
            return final_output

    '''
    ----------------
    Start of run sequence
    ----------------
    '''

    arr_numbers, arr_operands = split_input(
        problems)  # splits the initial string for use
    # determine amount of dashes for each sum
    arr_dash = determine_dash(arr_numbers)
    arr_sum = determine_sum(
        arr_numbers, arr_operands)  # calculate arrsum
    arr_topspaces, arr_bottomspaces, arr_sumspaces, arr_topnums, arr_bottomnums = determine_spaces(
        arr_numbers, arr_dash, arr_sum)  # determine spaces infront of numbers
    arranged_problems = display_output(
        arr_topspaces, arr_bottomspaces, arr_sumspaces, arr_topnums, arr_bottomnums, arr_sum)  # display output
    return arranged_problems




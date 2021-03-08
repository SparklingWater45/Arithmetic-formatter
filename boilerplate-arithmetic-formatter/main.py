# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))#normal
# print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])) #normal
# print(arithmetic_arranger((["44 + 815", "909 - 2", "45 + 43","123 + 49", "888 + 40", "653 + 87"]))#too many problems
#print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))#only + or /#
# print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))#over 4 length
# #print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])) #not all digits
# print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))#normal , with answer

# Run unit tests automatically
main(module='test_module', exit=False)

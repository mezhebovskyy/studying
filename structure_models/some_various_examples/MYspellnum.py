# def int_to_num(num):
#     d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
#           6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
#           11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
#           15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
#           19 : 'ninteen', 20 : 'twenty',
#           30 : 'thirty', 40 : 'fourty', 50 : 'fifty', 60 : 'sixty',
#           70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

#     if num < 21:
#         print d[num]

#     if num <= 99:
#         if num >= 21:
#             if num % 10 == 0:
#                 print d[num]
#             else:
#                 print d[num // 10 * 10] + '-' + d[num % 10]
                
#     if num < k:
#         if num % 100 == 0:
#             print d[num / 100] + " hundred"
#         else:
#             print d[num // 100] + " hundred and " + int_to_num(num % 100) 

    

# def main():
#     number = int(raw_input("Type a number from 1 to 999999999999999: "))
#     if number < 1:
#         print "The number should be higher than 0, you dickhead!"
#         number1 = int(raw_input("Type a number FROM ONE to 99999999999999: "))
#         number = number1

#     if number > 999999999999:
#         print "The number should NOT be higher than 999999999999999, you dickhead!"
#         number1 = int(raw_input("Type a number from 1 to 99999999999999: "))
#         number = number1

#     s = str(number)
#     length = len(s)
#     num_of_3 = length/3
#     rest = length % 3

#     hundred = s[length-3:length] 
#     thousand = s[length-6:length-3]
#     million = s[length-9:length-6]
#     billion = s[length-12:length-9]
#     trillion = s[length-15:length-12]

#     if num_of_3 == 1:
#         if rest == 0:
#             thousand, million, billion, trillion = 0, 0, 0, 0
#         else:
#             thousand = s[length-6+(3-rest):length-3]
#             million, billion, trillion = 0, 0, 0
#     elif num_of_3 == 2:
#         if rest == 0:
#             million, billion, trillion = 0, 0, 0
#         else:
#             million = s[length-9+(3-rest):length-6]
#             billion, trillion = 0, 0
#     elif num_of_3 == 3:
#         if rest == 0:
#             billion, trillion = 0, 0
#         else:
#             billion = s[length-12+(3-rest):length-9]
#             trillion = 0
#     elif num_of_3 == 4:
#         if rest == 0:
#             trillion = 0
#         else:
#             trillion = s[length-15+(3-rest):length-12]




# if __name__== "__main__":
#     main()
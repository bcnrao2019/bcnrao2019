# 4.5 Calendar Year Program2
# this function prepares a character array for the whole year, forming 12 character arrays month wise
def year_calender(day, yr1):
    year_char = ['', '', '', '', '', '', '', '', '', '', '', '']
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    leap_year = chk_lp_year(yr1)
    if leap_year:
        days_in_month[1] = 29

    # print(f'Day in month Feb {yr1} are {days_in_month[1]}')
    month_names1 = ('January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December')

    # this routine prepares the year array
    for j in range (0,12):
        # this routine prepares the blank space before first day of week
        if day == 0:
            day = 7
        for i in range(0, day-1):
            year_char[j] = year_char[j] + '   '

            # this for loop create character for the month to hold all days of month
        for i in range(1, days_in_month[j]+1):
            # this routine adjusts the "day word" length to keep size of 3 characters like '  1' and ' 10'
            if i > 9:
                year_char[j] = year_char[j] + ' ' + str(i)
            else:
                year_char[j] = year_char[j] + '  ' + str(i)
            # day = day + 1
        day = day + days_in_month[j]

        # if (len(year_char[j]) < 126):
        for i in range(len(year_char[j]), 126):
            year_char[j] = year_char[j] + ' '

        day = day % 7
        # if not j == 11:
        #     print(f'First Day in next month of {month_names1[j+1]} is {day}')
    return year_char

# this function finds the first day of year for the given year and returns the first day
def fst_day_of_year(yr):
    century_digit = yr // 100
    yr_digit = yr % 100

    value = yr_digit + (yr_digit // 4)
    # print(value)
    # if century_digit == 18:
    #     value = value + 2
    # elif century_digit == 20:
    #     value = value + 6
    value = value + 6

    leap_year = chk_lp_year(yr)
    if not leap_year:
        value = value + 1

    first_day_of_year = (value + 1) % 7
    return first_day_of_year


# this function checks if the year is leap, and returns true if year is leap otherwise returns false
def chk_lp_year(yr):
    if (yr % 4 == 0) and (not (yr % 100 == 0) or (yr % 400 == 0)):
        lp_yr = True
    else:
        lp_yr = False
    return lp_yr


# year = 2008
year = int(input('Enter year:  <-1 to quit> : '))
while year < 1800 or year > 2099:
    year = int (input ('Enter year: '))

file = open('cal.txt', 'w')
first_day_of_month  = fst_day_of_year(year)
day_list = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
string = year_calender(first_day_of_month, year)
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']


for i in (0, 3, 6, 9):
    print('-' * 75)
    print('', year , format(month_names[i], '>15'), format(month_names[i + 1], '>26'),
          format(month_names[i + 2], '>26'))
    print(' Su Mo Tu We Th Fr Sa      ' * 3)
    file.write('-' * 72)
    file.write('\n')
    file_line = ' '
    file_line = file_line + str(year) + format(month_names[i], '>16') + format(month_names[i + 1], '>25') + \
          format(month_names[i + 2], '>25') + '\n'
    file.write(file_line)

    file.write(' Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa      \n')
    for j in range(0, 6):
        print(string[i][21 * j:21 * j + 21], '    ', string[i + 1][21 * j:21 * j + 21], '    ', string[i + 2][21 * j:21 * j + 21])
        file_line = ''
        file_line = file_line + string[i][21 * j:21 * j + 21] + '    ' + string[i + 1][21 * j:21 * j + 21] + \
            '    ' + string[i + 2][21 * j:21 * j + 21] + '\n'
        file.write(file_line)

print('-' * 75)
file.write('-' * 72)
file.write('\n')
file.close()


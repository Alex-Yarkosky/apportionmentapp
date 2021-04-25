import csv
import math

def get_state_populations(year):
    ''' Parameters: census year
    Summary: gets populations for each states for given census year from a text file
    Return: list of state populations ordered alphabetically by state name '''

    try:
        file = ('../resources/census_data/{}population.txt').format(year)
        population_text = open(file, 'r')
    except:
        raise Exception('Please give a census year from 1900 to 2010 as parameters')
    population = []
    for line in population_text:
        stripped_line = line.strip()
        population.append(stripped_line)
    return population

def find_national_pop(year):
    ''' Parameters: census year
    Summary: combines state populations to come up with a national population
    Return: combined population of all 50 states '''

    natl_pop = 0
    states = get_state_populations(year)

    # Loop through every state for the given year and add their pop to natl_pop
    for state in states:
        natl_pop += int(state)
    # print(natl_pop)
    return natl_pop

# unused
def district_pop_difference(highest, lowest):
    ''' Parameters: most populous district (state average), least populous district (state average)
    Return: difference of most populous district minus least poplous district '''

    return highest - lowest

# unused
def find_largest_pop_district(apportionment, year):
    ''' Parameters: list of apportioned seats, census year used in the apportionment
    Return: largest average district size from the given apportionment '''

    state_pops = get_state_populations(year)
    largest = 0

    for i in range(0, 50):
      district_size = int(state_pops[i]) / apportionment[i]
      if district_size > largest:
          largest = district_size

    return largest

# unused
def find_smallest_pop_district(apportionment, year):
    ''' Parameters: list of apportioned seats, census year used in the apportionment
    Return: smallest average district size from the given apportionment '''

    state_pops = get_state_populations(year)
    smallest = 999999999

    for i in range(0, 50):
      district_size = int(state_pops[i]) / apportionment[i]
      if district_size < smallest:
          smallest = district_size

    return smallest

def find_divisor(house_size, national_pop):
    ''' Parameters: size of the House, population of the US states
    Return: divisor created from the national population over the house size '''

    return int(national_pop / house_size)

def find_quota(state_pop, divisor):
    ''' Parameters: population of a state, divisor to divide by
    Return: population of a state divided by the given divisor '''

    return int(state_pop) / divisor

def average_constituency(state_pop, seats):
    ''' Parameters: population of a state, number of seats assigned to that state
    Return: average constiuency size for the given state '''

    return int(state_pop) / seats

def average_constituencies(apportionment, year):
    ''' Parameters: list of apportioned seats, census year used in apportionment
    Summary: finds the average constiuency size for each state and then finds the average of that total
    Return: average of the average constiuency size for each state '''

    state_pops = get_state_populations(year)
    total = 0

    for i in range(0, 50):
        total += average_constituency(state_pops[i], apportionment[i])

    return total / 50

def multiple_runs_variable_house_size(starting_seats, ending_seats, year):
    ''' Parameters: start of range of house sizes, end of range of house seats, census year
    Summary: apportions for each method for a given year for every house size within the given endpoints of the range;
    outputs results from each apportionment in a single CSV file
    Return: None '''

    # lists that will be outputted
    house_sizes = []
    years = []
    methods = []
    results = []

    # set initial house size
    house_size = starting_seats

    # clear output file
    file = open("apportionments.csv","r+")
    file.truncate(0)

    # loop through the range of house sizes
    while(house_size <= ending_seats):

        # apportion using the hamilton method
        hamilton_app = hamilton_method(house_size, year)
        house_sizes.append(house_size)
        years.append(year)
        methods.append('hamilton')
        results.append(average_constituencies(hamilton_app, year))
        # str = ('Hamilton for {} with {} seats completed').format(year, house_size)
        # print(str)

        # apportion using the lowndes method
        lowndes_app = lowndes_method(house_size, year)
        house_sizes.append(house_size)
        years.append(year)
        methods.append('lowndes')
        results.append(average_constituencies(lowndes_app, year))
        # str = ('Lowndes for {} with {} seats completed').format(year, house_size)
        # print(str)

        # apportion using the jefferson method
        jefferson_app = jefferson_method(house_size, year)
        house_sizes.append(house_size)
        years.append(year)
        methods.append('jefferson')
        results.append(average_constituencies(jefferson_app, year))
        # str = ('Jefferson for {} with {} seats completed').format(year, house_size)
        # print(str)

        # apportion using the adams method
        adams_app = adams_method(house_size, year)
        house_sizes.append(house_size)
        years.append(year)
        methods.append('adams')
        results.append(average_constituencies(adams_app, year))
        # str = ('Adams for {} with {} seats completed').format(year, house_size)
        # print(str)

        # apportion using the webster method
        webster_app = webster_method(house_size, year)
        house_sizes.append(house_size)
        years.append(year)
        methods.append('webster')
        results.append(average_constituencies(webster_app, year))
        # str = ('Webster for {} with {} seats completed').format(year, house_size)
        # print(str)

        # apportion using the dean method
        dean_app = dean_method(house_size, year)
        house_sizes.append(house_size)
        years.append(year)
        methods.append('dean')
        results.append(average_constituencies(dean_app, year))
        # str = ('Dean for {} with {} seats completed').format(year, house_size)
        # print(str)

        # apportion using the huntington-hill method
        huntington_hill_app = huntington_hill_method(house_size, year)
        house_sizes.append(house_size)
        years.append(year)
        methods.append('huntington-hill')
        results.append(average_constituencies(huntington_hill_app, year))
        # str = ('Huntington-Hill for {} with {} seats completed').format(year, house_size)
        # print(str)

        # str = ('Apportionments for {} completed').format(house_size)
        # print(str)

        # increment the house size
        house_size += 1

        # exit the loop once outside the range of house sizes
        if house_size > ending_seats:
            break

    # output house size, year, method, and average of average constiuency size for each apportionment done
    outputs(house_sizes, years, methods, results)

    return

def multiple_runs_varible_year(house_size):
    ''' Parameters: house size to apportion
    Summary: apportions for each method for a given house size for every census year available;
    outputs results from each apportionment in a single CSV file
    Return: None '''

    # census years available
    years = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]

    # clear output file
    file = open("apportionments.csv","r+")
    file.truncate(0)

    # loop through each year
    for year in years:

        # apportion using the hamilton method
        hamilton_app = hamilton_method(house_size, year)
        result = average_constituencies(hamilton_app, year)
        # str = ('Hamilton for {} with {} seats completed').format(year, house_size)
        # print(str)
        # output house size, year, method, and average of average constiuency size
        output(house_size, year, 'Hamilton', result)

        # apportion using the lowndes method
        lowndes_app = lowndes_method(house_size, year)
        result = average_constituencies(lowndes_app, year)
        # str = ('Lowndes for {} with {} seats completed').format(year, house_size)
        # print(str)
        # output house size, year, method, and average of average constiuency size
        output(house_size, year, 'Lowndes', result)

        # apportion using the jefferson method
        jefferson_app = jefferson_method(house_size, year)
        result = average_constituencies(jefferson_app, year)
        # str = ('Jefferson for {} with {} seats completed').format(year, house_size)
        # print(str)
        # output house size, year, method, and average of average constiuency size
        output(house_size, year, 'Jefferson', result)

        # apportion using the adams method
        adams_app = adams_method(house_size, year)
        result = average_constituencies(adams_app, year)
        # str = ('Adams for {} with {} seats completed').format(year, house_size)
        # print(str)
        # output house size, year, method, and average of average constiuency size
        output(house_size, year, 'Adams', result)

        # apportion using the webster method
        webster_app = webster_method(house_size, year)
        result = average_constituencies(webster_app, year)
        # str = ('Webster for {} with {} seats completed').format(year, house_size)
        # print(str)
        # output house size, year, method, and average of average constiuency size
        output(house_size, year, 'Webster', result)

        # apportion using the dean method
        dean_app = dean_method(house_size, year)
        result = average_constituencies(dean_app, year)
        # str = ('Dean for {} with {} seats completed').format(year, house_size)
        # print(str)
        # output house size, year, method, and average of average constiuency size
        output(house_size, year, 'Dean', result)

        # apportion using the huntington-hill method
        huntington_hill_app = hamilton_method(house_size, year)
        result = average_constituencies(huntington_hill_app, year)
        # str = ('Huntington-Hill for {} with {} seats completed').format(year, house_size)
        # print(str)
        # output house size, year, method, and average of average constiuency size
        output(house_size, year, 'Huntington-Hill', result)

        # str = ('Apportionments for {} completed').format(year)
        # print(str)

        # exit the loop at the end of the available census years
        if year == 2010:
            # str = ('Apportionments for {} completed').format(house_size)
            # print(str)
            break

    return

def output(house_sizes, years, methods, results):
    ''' Parameters: houses size, year, apportionment method, district population difference
    Summary: data formatted into outputted CSV file
    Return: None'''

    # creates and opens CSV file
    with open('apportionments.csv', mode='a') as apportionments:
        results_writer = csv.writer(apportionments, delimiter=',')

        # adds a row to the CSV file
        results_writer.writerow([methods, years, house_sizes, results])

    return

def outputs(house_sizes, years, methods, results):
    ''' Parameters: list of houses sizes, list of years, list of apportionment methods, list of district population differences
    Summary: data formatted into outputted CSV file
    Return: None'''

    # creates and opens CSV file
    with open('apportionments.csv', mode='a') as apportionments:
        results_writer = csv.writer(apportionments, delimiter=',')

        # adds each row to the CSV file
        for i in range(0, len(methods)):
            results_writer.writerow([methods[i], years[i], house_sizes[i], results[i]])

    return

def print_apportionment(apportionment, STATES):
    ''' Parameters: list of apportioned seats, list of state names
    Summary: print state name and number of seats apportioned to it
    Return: None '''

    for i in range (0, 50):
        print(STATES[i] + ': ' + str(apportionment[i]))

    return


def hamilton_method(house_size, year):
    ''' Choose the size of the house to be apportioned.
    Find the quotas and give to each state the whole number contained in its quota.
    Assign any seats which are yet unapportioned to those states having the largest fractions or remainders.
    -Fair Representation page 17 '''

    ''' Find quotas for each state assigning seats for the whole numbers of each quota.
    Assign the rest of the seats to states with the largest decimals in their quotas. '''

    national_pop = find_national_pop(year)
    state_pops = get_state_populations(year)
    quotas = []
    quotas_whole = []
    quotas_decimal = []
    divisor = find_divisor(house_size, national_pop)

    # find quotas for each state
    for state_pop in state_pops:
        quota = find_quota(state_pop, divisor)
        quotas.append(quota)
        quotas_whole.append(math.floor(quota))
        quotas_decimal.append(quota - math.floor(quota))

    # print(quotas)
    # print(quotas_whole)
    # print(quotas_decimal)

    # find how many seats have been assigned so far
    seats_assigned = 0
    for quota in quotas_whole:
        seats_assigned += quota

    # print(seats_assigned)

    remaining_seats = house_size - seats_assigned

    # assign seats to any state without one yet first
    for i in range (0, remaining_seats):
        index = 0
        # look for any states with no assigned seats
        for quota in quotas_whole:
            if quota == 0:
                # assign seat to state without any seats yet
                quotas_whole[index] += 1
                # remove decimal so state does not get selected again
                quotas_decimal[index] = 0
                # increment index to keep track of which state the decimal belongs to
            index += 1

    # find how many seats have been assigned so far
    seats_assigned = 0
    for quota in quotas_whole:
        seats_assigned += quota

    # recalculate remaining seats
    remaining_seats = house_size - seats_assigned

    # assign remaining seats one by one to states whose quotas have the largest decimals
    for i in range (0, remaining_seats):
        highest_value = 0
        highest_index = 0 # be mindul of this otherwise rip Alabama
        index = 0
        # find largest decimal in the state quotas
        for decimal in quotas_decimal:
            if decimal > highest_value:
                # set this state as having the highest decimal
                highest_value = decimal
                highest_index = index
            # increment index to keep track of which state the decimal belongs to
            index += 1
        # assign seat to state with highest decimal in their quota
        quotas_whole[highest_index] += 1
        # remove decimal so state does not get selected again
        quotas_decimal[highest_index] = 0

    seats_assigned = 0
    for quota in quotas_whole:
        seats_assigned += quota

    # print(quotas_whole)
    # print(quotas_decimal)
    # print(seats_assigned)

    return quotas_whole

def jefferson_method(house_size, year):
    ''' Choose the size of the house to be apportioned.
    Find a divisor x so that the whole numbers contained in the quotients of the states sum to the required total.
    Give to each each state its whole number.
    -Fair Representation page 18 '''

    ''' Choose a divisor such that dividing the state populations by it produces quotients whose whole numbers add up to the desired house size. '''

    national_pop = find_national_pop(year)
    state_pops = get_state_populations(year)
    quotients = []
    quotients_whole = []
    divisor = find_divisor(house_size, national_pop)

    # find the correct divisor
    while(True):

        # clear lists
        quotients = []
        quotients_whole = []

        # find quotas for each state
        for state_pop in state_pops:
            quotient = find_quota(state_pop, divisor)
            quotients.append(quotient)
            quotients_whole.append(math.floor(quotient))

        # find how many seats have been assigned so far
        seats_assigned = 0
        for quotient in quotients_whole:
            seats_assigned += quotient

        remaining_seats = house_size - seats_assigned

        # assign seats to any state without one yet first
        for i in range (0, remaining_seats):
            index = 0
            # look for any states with no assigned seats
            for quotient in quotients_whole:
                if quotient == 0:
                    # assign seat to state without any seats yet
                    quotients_whole[index] += 1
                # increment index to keep track of which state the decimal belongs to
                index += 1

        # find how many seats have been assigned so far
        seats_assigned = 0
        for quotient in quotients_whole:
            seats_assigned += quotient

        # print('seats_assigned', seats_assigned)
        # print('divisor', divisor)

        # decrease the divisor if the desired house size was not reached
        if(seats_assigned != house_size):
            divisor -= 1
        else:
            # print('Divisor used:', divisor)
            break

    return quotients_whole

def lowndes_method(house_size, year):
    ''' Choose the size of the house to be apportioned.
    Find the quotas and give to each state the whole number contained in its quota.
    Adjust each state state's remainder by dividing by the whole number in its quota.
    Assign any seats which are as yet unapportioned to those states having the largest adjusted remainer.
    -Fair Representation page 25 '''

    ''' Modification of the Hamilton Method and how it distributes the final seats.
    Remaining seats go to the seats that would benefit the most from additional representation, typically smaller states. '''

    national_pop = find_national_pop(year)
    state_pops = get_state_populations(year)
    quotas = []
    quotas_whole = []
    quotas_decimal = []
    divisor = find_divisor(house_size, national_pop)

    # find quotas for each state
    for state_pop in state_pops:
        quota = find_quota(state_pop, divisor)
        quotas.append(quota)
        quotas_whole.append(math.floor(quota))
        quotas_decimal.append(quota - math.floor(quota))

    # print(quotas)
    # print(quotas_whole)
    # print(quotas_decimal)

    # find how many seats have been assigned so far
    seats_assigned = 0
    for quota in quotas_whole:
        seats_assigned += quota

    # print(seats_assigned)

    remaining_seats = house_size - seats_assigned

    # assign seats to any state without one yet first
    for i in range (0, remaining_seats):
        index = 0
        # look for any states with no assigned seats
        for quota in quotas_whole:
            if quota == 0:
                # assign seat to state without any seats yet
                quotas_whole[index] += 1
                # remove decimal so state does not get selected again
                quotas_decimal[index] = 1
            # increment index to keep track of which state the decimal belongs to
            index += 1

    # find how many seats have been assigned so far
    seats_assigned = 0
    for quota in quotas_whole:
        seats_assigned += quota

    # recalculate remaining seats
    remaining_seats = house_size - seats_assigned

    # assign remaining seats one by one to states whose quotas have the largest decimals
    for i in range (0, remaining_seats):
        lowest_value = 1
        lowest_index = 0 # be mindul of this otherwise rip Alabama
        index = 0
        # find largest decimal in the state quotas
        for decimal in quotas_decimal:
            if decimal < lowest_value:
                # set this state as having the highest decimal
                lowest_value = decimal
                lowest_index = index
            # increment index to keep track of which state the decimal belongs to
            index += 1
        # assign seat to state with highest decimal in their quota
        quotas_whole[lowest_index] += 1
        # remove decimal so state does not get selected again
        quotas_decimal[lowest_index] = 1

    seats_assigned = 0
    for quota in quotas_whole:
        seats_assigned += quota

    # print(quotas_whole)
    # print(quotas_decimal)
    # print(seats_assigned)

    return quotas_whole

def adams_method(house_size, year):
    ''' Choose the size of the house to be apportioned.
    Find a divisor x so taht the smallest whole numbers containing the quotients of the states sum to the required total.
    Give to each state its whole number.
    -Fair Representation page 28 '''

    ''' Inversion of the Jefferson Method.
    Rounds all quotients up instead of down. '''

    national_pop = find_national_pop(year)
    state_pops = get_state_populations(year)
    quotients = []
    quotients_whole = []
    divisor = find_divisor(house_size, national_pop)

    # find the correct divisor
    while(True):

        # clear lists
        quotients = []
        quotients_whole = []

        # find quotas for each state
        for state_pop in state_pops:
            quotient = find_quota(state_pop, divisor)
            quotients.append(quotient)
            quotients_whole.append(math.ceil(quotient))

        # find how many seats have been assigned so far
        seats_assigned = 0
        for quotient in quotients_whole:
            seats_assigned += quotient

        # print('seats_assigned', seats_assigned)
        # print('divisor', divisor)

        # increase the divisor if the desired house size was not reached
        if(seats_assigned != house_size):
            divisor += 1
        else:
            # print('Divisor used:', divisor)
            break

    return quotients_whole

def webster_method(house_size, year):
    ''' Choose the size of the house to be apportioned.
    Find a divisor x so that the whole numbers nearest to the quotients of the states sum to the required total.
    Give to each state its whole number.
    -Fair Representation page 32 '''

    ''' Modification of the Jefferson Method.
    Rounds quotients to the nearest whole number. '''

    national_pop = find_national_pop(year)
    state_pops = get_state_populations(year)
    quotients = []
    quotients_whole = []
    divisor = find_divisor(house_size, national_pop)

    # find the correct divisor
    while(True):

        # clear lists
        quotients = []
        quotients_whole = []

        # find quotas for each state
        for state_pop in state_pops:
            quotient = find_quota(state_pop, divisor)
            quotients.append(quotient)
            # rounds quotients to nearest whole number unless that number is 0
            # change other solutions to dealing with 0 seats asssigned to this method?
            if round(quotient) != 0:
                quotients_whole.append(round(quotient))
            else:
                quotients_whole.append(1)

        # find how many seats have been assigned so far
        seats_assigned = 0
        for quotient in quotients_whole:
            seats_assigned += quotient

        # print('seats_assigned', seats_assigned)
        # print('divisor', divisor)

        # changes the divisor if the desired house size was not reached
        if(seats_assigned > house_size):
            divisor += 1
        elif(seats_assigned < house_size):
            divisor -= 1
        else:
            # print('Divisor used:', divisor)
            break

    return quotients_whole

def huntington_hill_method(house_size, year):
    ''' Choose the size of the house to be apportioned.
    Give to each state a number of seats so that no transfer of any one seat can reduce the percentage difference in represenation between those states.
    -Fair Representation page 48 '''

    ''' Prioritizes relative difference over absolute difference.
    Accounts for the fact that adding a seat to a state with few assigned to it has more of an effect than adding that seat to a state with a lot already assigned.
    Divides population of a state by the square root of the number of assigned seats multipled by the number of assigned seats minus 1.
    Uses results from that equation from each state to assign a seat to the seat with the largest result. '''

    state_pops = get_state_populations(year)
    assigned_seats = []

    # assign each state one seat to start with
    for i in range (0, 50):
        assigned_seats.append(1)

    while(True):

        priority_number = []
        highest = 0
        highest_index = 0 # check for Alabama issues

        # find the state to assign the next seat to
        for i in range (0, 50):
            # calculation based on assigning the next seat so 1 is added to current assigned_seats value for each state
            priority_number.append(int(state_pops[i]) / math.sqrt((assigned_seats[i] + 1) * assigned_seats[i]))
            if priority_number[i] > highest:
                highest = priority_number[i]
                highest_index = i

        # assign seat to state that had the highest priority number
        assigned_seats[highest_index] += 1

        # find how many seats have been assigned so far
        seats_assigned = 0
        for seat in assigned_seats:
            seats_assigned += seat

        # end once the desired number of seats have been assigned
        if seats_assigned == house_size:
            break

    return assigned_seats

def dean_method(house_size, year):
    ''' Choose the size of the house to be apportioned.
    Find a divisor x so that the whole numbers which make the average constituencies of the states closest to x sum to the required total.
    Give to each state its whole number.
    -Fair Representation page 30'''

    ''' Proritizes absolute difference over relative difference.
    Same equation as the Huntington Hill Method except without the square root. '''

    national_pop = find_national_pop(year)
    state_pops = get_state_populations(year)
    quotients = []
    quotients_whole = []
    divisor = find_divisor(house_size, national_pop)

    # find the correct divisor
    while(True):

        # clear lists
        quotients = []
        quotients_whole = []

        # find quotas for each state
        for state_pop in state_pops:
            quotient = find_quota(state_pop, divisor)
            quotients.append(quotient)
            quotient_rounded_down = math.floor(quotient)
            if quotient_rounded_down == 0:
                quotient_rounded_down = 1
            average = average_constituency(state_pop, quotient_rounded_down)
            next_average = average_constituency(state_pop, (quotient_rounded_down + 1))
            # find average constiuency closest to the divisor
            if (abs(average - divisor) > abs(next_average - divisor)):
                quotients_whole.append(quotient_rounded_down + 1)
            else:
                quotients_whole.append(quotient_rounded_down)

        # find how many seats have been assigned so far
        seats_assigned = 0
        for quotient in quotients_whole:
            seats_assigned += quotient

        # print('seats_assigned', seats_assigned)
        # print('divisor', divisor)

        # changes the divisor if the desired house size was not reached
        if(seats_assigned > house_size):
            divisor += .5
        elif(seats_assigned < house_size):
            divisor -= .5
        else:
            # print('Divisor used:', divisor)
            break

    return quotients_whole

if __name__ == '__main__':

    # print welcome message at start up of app
    print('Welcome to the Apportionment App!')
    # explain how to input choices
    print('To interact with the application, input the number that comes after an option to select it.')
    # let the user know how to exit the app
    print('Anytime you would like to exit the application, enter a 0 when choosing between options.')

    # create list of each state's name
    states_text = open('../resources/states.txt', 'r')
    STATES = []
    for line in states_text:
        stripped_line = line.strip()
        STATES.append(stripped_line)
    # print(STATES)

    while(True):
        type = input('Would you like do apportionment one at a time (1) or would you like to do apportionment en masse (2)? ')
        if type == '0':
            print('Exiting now.')
            break
        elif type == '1':
            method = input('Would you like to apportion using the Hamilton Method (1), Jefferson Method (2), Lowndes Method (3), Adams Method (4), Webster Method (5), Dean Method (6), or Huntington-Hill Method (7)? ')
            if method == '1':
                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                house_size = input('What house size would you like to apportion for? ')
                apportionment = hamilton_method(int(house_size), year)
                output_message = ('Hamilton Method for {} seats for {}').format(house_size, year)
                print(output_message)
                print_apportionment(apportionment, STATES)
            elif method == '2':
                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                house_size = input('What house size would you like to apportion for? ')
                apportionment = jefferson_method(int(house_size), year)
                output_message = ('Jefferson Method for {} seats for {}').format(house_size, year)
                print(output_message)
                print_apportionment(apportionment, STATES)
            elif method == '3':
                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                house_size = input('What house size would you like to apportion for? ')
                apportionment = lowndes_method(int(house_size), year)
                output_message = ('Lowndes Method for {} seats for {}').format(house_size, year)
                print(output_message)
                print_apportionment(apportionment, STATES)
            elif method == '4':
                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                house_size = input('What house size would you like to apportion for? ')
                apportionment = adams_method(int(house_size), year)
                output_message = ('Adams Method for {} seats for {}').format(house_size, year)
                print(output_message)
                print_apportionment(apportionment, STATES)
            elif method == '5':
                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                house_size = input('What house size would you like to apportion for? ')
                apportionment = webster_method(int(house_size), year)
                output_message = ('Webster Method for {} seats for {}').format(house_size, year)
                print(output_message)
                print_apportionment(apportionment, STATES)
            elif method == '6':
                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                house_size = input('What house size would you like to apportion for? ')
                apportionment = dean_method(int(house_size), year)
                output_message = ('Dean Method for {} seats for {}').format(house_size, year)
                print(output_message)
                print_apportionment(apportionment, STATES)
            elif method == '7':
                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                house_size = input('What house size would you like to apportion for? ')
                apportionment = huntington_hill_method(int(house_size), year)
                output_message = ('Huntington-Hill Method for {} seats for {}').format(house_size, year)
                print(output_message)
                print_apportionment(apportionment, STATES)
            else:
                while(method != '1' or '2' or '3' or '4' or '5' or '6' or '7'):
                    method = input('Invalid input received, please re-enter your input. Would you like to apportion using the Hamilton Method (1), Jefferson Method (2), Lowndes Method (3), Adams Method (4), Webster Method (5), Dean Method (6), or Huntington-Hill Method (7)? ')
                    if type == '0':
                        print('Exiting now.')
                        break
                    elif method == '1':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = hamilton_method(int(house_size), year)
                        output_message = ('Hamilton Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                        break
                    elif method == '2':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = jefferson_method(int(house_size), year)
                        output_message = ('Jefferson Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                        break
                    elif method == '3':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = lowndes_method(int(house_size), year)
                        output_message = ('Lowndes Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                        break
                    elif method == '4':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = adams_method(int(house_size), year)
                        output_message = ('Adams Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                        break
                    elif method == '5':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = webster_method(int(house_size), year)
                        output_message = ('Webster Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                        break
                    elif method == '6':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = dean_method(int(house_size), year)
                        output_message = ('Dean Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                        break
                    elif method == '7':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = huntington_hill_method(int(house_size), year)
                        output_message = ('Huntington-Hill Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                        break
        elif type == '2':
            variable = input('Would you like to apportion over a range of house sizes (1) or over multiple years (2)? ')
            if type == '0':
                print('Exiting now.')
                break
            elif variable == '1':
                starting_seats = input('What house size would you like to start the range at? ')
                ending_seats = input('What house size would you like to end the range at? ')
                year = input('What census year between 1900-2010 would you like to apportion for? ')
                try:
                    # needs revising when first size is larger than second
                    multiple_runs_variable_house_size(int(starting_seats), int(ending_seats), year)
                    output_message = ('Apportionments from {} to {} seats for {} outputted as a CSV file.').format(starting_seats, ending_seats, year)
                    print(output_message)
                except:
                    raise Exception('Unable to do mulitple apportionments for given inputs.')
            elif variable == '2':
                house_size = input('What house size would you like to apportion for? ')
                try:
                    multiple_runs_varible_year(int(house_size))
                    output_message = ('Apportionments for {} seats from 1900-2010 outputted as a CSV file.').format(house_size)
                    print(output_message)
                except:
                    raise Exception('Unable to do multiple apportionments for given input.')
            else:
                while(variable != '1' or '2'):
                    variable = input('Invalid input received, please re-enter your input. Would you like to apportion over a range of house sizes (1) or over multiple years (2)? ')
                    if type == '0':
                        print('Exiting now.')
                        break
                    elif variable == '1':
                        starting_seats = input('What house size would you like to start the range at? ')
                        ending_seats = input('What house size would you like to end the range at? ')
                        year = input('What census year between 1900-2010 would you like to apportion for? ')
                        try:
                            # needs revising when first size is larger than second
                            multiple_runs_variable_house_size(int(starting_seats), int(ending_seats), year)
                            output_message = ('Apportionments from {} to {} seats for {} outputted as a CSV file.').format(starting_seats, ending_seats, year)
                            print(output_message)
                            # exit while loop
                            break
                        except:
                            raise Exception('Unable to do mulitple apportionments for given inputs.')
                            # exit while loop
                            break
                    elif variable == '2':
                        house_size = input('What house size would you like to apportion for? ')
                        try:
                            multiple_runs_varible_year(int(house_size))
                            output_message = ('Apportionments for {} seats from 1900-2010 outputted as a CSV file.').format(house_size)
                            print(output_message)
                            # exit while loop
                            break
                        except:
                            raise Exception('Unable to do multiple apportionments for given input.')
                            # exit while loop
                            break
        else:
            while(type != '1' or '2'):
                type = input('Invalid input received, please re-enter your input. Would you like do apportionment one at a time (1) or would you like to do apportionment en masse (2)? ')
                if type == '0':
                    print('Exiting now.')
                    break
                elif type == '1':
                    method = input('Would you like to apportion using the Hamilton Method (1), Jefferson Method (2), Lowndes Method (3), Adams Method (4), Webster Method (5), Dean Method (6), or Huntington-Hill Method (7)? ')
                    if method == '1':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = hamilton_method(int(house_size), year)
                        output_message = ('Hamilton Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                    elif method == '2':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = jefferson_method(int(house_size), year)
                        output_message = ('Jefferson Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                    elif method == '3':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = lowndes_method(int(house_size), year)
                        output_message = ('Lowndes Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                    elif method == '4':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = adams_method(int(house_size), year)
                        output_message = ('Adams Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                    elif method == '5':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = webster_method(int(house_size), year)
                        output_message = ('Webster Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                    elif method == '6':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = dean_method(int(house_size), year)
                        output_message = ('Dean Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                    elif method == '7':
                        year = input('Which census year between 1900-2010 would you like to apportion for? ')
                        house_size = input('What house size would you like to apportion for? ')
                        apportionment = huntington_hill_method(int(house_size), year)
                        output_message = ('Huntington-Hill Method for {} seats for {}').format(house_size, year)
                        print(output_message)
                        print_apportionment(apportionment, STATES)
                    else:
                        while(method != '1' or '2' or '3' or '4' or '5' or '6' or '7'):
                            method = input('Invalid input received, please re-enter your input. Would you like to apportion using the Hamilton Method (1), Jefferson Method (2), Lowndes Method (3), Adams Method (4), Webster Method (5), Dean Method (6), or Huntington-Hill Method (7)? ')
                            if type == '0':
                                print('Exiting now.')
                                break
                            elif method == '1':
                                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                                house_size = input('What house size would you like to apportion for? ')
                                apportionment = hamilton_method(int(house_size), year)
                                output_message = ('Hamilton Method for {} seats for {}').format(house_size, year)
                                print(output_message)
                                print_apportionment(apportionment, STATES)
                                break
                            elif method == '2':
                                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                                house_size = input('What house size would you like to apportion for? ')
                                apportionment = jefferson_method(int(house_size), year)
                                output_message = ('Jefferson Method for {} seats for {}').format(house_size, year)
                                print(output_message)
                                print_apportionment(apportionment, STATES)
                                break
                            elif method == '3':
                                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                                house_size = input('What house size would you like to apportion for? ')
                                apportionment = lowndes_method(int(house_size), year)
                                output_message = ('Lowndes Method for {} seats for {}').format(house_size, year)
                                print(output_message)
                                print_apportionment(apportionment, STATES)
                                break
                            elif method == '4':
                                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                                house_size = input('What house size would you like to apportion for? ')
                                apportionment = adams_method(int(house_size), year)
                                output_message = ('Adams Method for {} seats for {}').format(house_size, year)
                                print(output_message)
                                print_apportionment(apportionment, STATES)
                                break
                            elif method == '5':
                                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                                house_size = input('What house size would you like to apportion for? ')
                                apportionment = webster_method(int(house_size), year)
                                output_message = ('Webster Method for {} seats for {}').format(house_size, year)
                                print(output_message)
                                print_apportionment(apportionment, STATES)
                                break
                            elif method == '6':
                                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                                house_size = input('What house size would you like to apportion for? ')
                                apportionment = dean_method(int(house_size), year)
                                output_message = ('Dean Method for {} seats for {}').format(house_size, year)
                                print(output_message)
                                print_apportionment(apportionment, STATES)
                                break
                            elif method == '7':
                                year = input('Which census year between 1900-2010 would you like to apportion for? ')
                                house_size = input('What house size would you like to apportion for? ')
                                apportionment = huntington_hill_method(int(house_size), year)
                                output_message = ('Huntington-Hill Method for {} seats for {}').format(house_size, year)
                                print(output_message)
                                print_apportionment(apportionment, STATES)
                                break
                elif type == '2':
                    variable = input('Would you like to apportion over a range of house sizes (1) or over multiple years (2)? ')
                    if type == '0':
                        print('Exiting now.')
                        break
                    elif variable == '1':
                        starting_seats = input('What house size would you like to start the range at? ')
                        ending_seats = input('What house size would you like to end the range at? ')
                        year = input('What census year between 1900-2010 would you like to apportion for? ')
                        try:
                            # needs revising when first size is larger than second
                            multiple_runs_variable_house_size(int(starting_seats), int(ending_seats), year)
                            output_message = ('Apportionments from {} to {} seats for {} outputted as a CSV file.').format(starting_seats, ending_seats, year)
                            print(output_message)
                        except:
                            raise Exception('Unable to do mulitple apportionments for given inputs.')
                    elif variable == '2':
                        house_size = input('What house size would you like to apportion for? ')
                        try:
                            multiple_runs_varible_year(int(house_size))
                            output_message = ('Apportionments for {} seats from 1900-2010 outputted as a CSV file.').format(house_size)
                            print(output_message)
                        except:
                            raise Exception('Unable to do multiple apportionments for given input.')
                    else:
                        while(variable != '1' or '2'):
                            variable = input('Invalid input received, please re-enter your input. Would you like to apportion over a range of house sizes (1) or over multiple years (2)? ')
                            if type == '0':
                                print('Exiting now.')
                                break
                            elif variable == '1':
                                starting_seats = input('What house size would you like to start the range at? ')
                                ending_seats = input('What house size would you like to end the range at? ')
                                year = input('What census year between 1900-2010 would you like to apportion for? ')
                                try:
                                    # needs revising when first size is larger than second
                                    multiple_runs_variable_house_size(int(starting_seats), int(ending_seats), year)
                                    output_message = ('Apportionments from {} to {} seats for {} outputted as a CSV file.').format(starting_seats, ending_seats, year)
                                    print(output_message)
                                    # exit while loop
                                    break
                                except:
                                    raise Exception('Unable to do mulitple apportionments for given inputs.')
                                    # exit while loop
                                    break
                            elif variable == '2':
                                house_size = input('What house size would you like to apportion for? ')
                                try:
                                    multiple_runs_varible_year(int(house_size))
                                    output_message = ('Apportionments for {} seats from 1900-2010 outputted as a CSV file.').format(house_size)
                                    print(output_message)
                                    # exit while loop
                                    break
                                except:
                                    raise Exception('Unable to do multiple apportionments for given input.')
                                    # exit while loop
                                    break

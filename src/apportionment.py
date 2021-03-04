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

def district_pop_difference(highest, lowest):
    ''' Parameters: most populous district (state average), least populous district (state average)
    Return: difference of most populous district minus least poplous district '''

    return highest - lowest

def find_divisor(house_size, national_pop):
    ''' Parameters: size of the House, population of the US states
    Return: divisor created from the national population over the house size '''

    return int(national_pop / house_size)

def find_quota(state_pop, divisor):
    ''' Parameters: population of a state, divisor to divide by
    Return: population of a state divided by the given divisor '''

    return int(state_pop) / divisor

def average_constiuency(state_pop, seats):
    ''' Parameters: population of a state, number of seats assigned to that state
    Return: average constiuency size for the given state '''

    return int(state_pop) / seats

def output(house_sizes, years, methods, differences):
    with open('apportionments.csv', mode='w') as apportionments:
        results_writer = csv.writer(apportionments, delimiter=',')

        for i in range(0, len(methods)):
            results_writer.writerow([methods[i], years[i], house_sizes[i], differences[i]])

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
            average = average_constiuency(state_pop, quotient_rounded_down)
            next_average = average_constiuency(state_pop, (quotient_rounded_down + 1))
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
            divisor += 1
        elif(seats_assigned < house_size):
            divisor -= 1
        else:
            # print('Divisor used:', divisor)
            break

    return quotients_whole

# Create function to loop through multiple runs for data collection purposes (varying house sizes for 2010 data and varying years for 435 seats)

states_text = open('../resources/states.txt', 'r')
STATES = []
for line in states_text:
    stripped_line = line.strip()
    STATES.append(stripped_line)
# print(STATES)

hamilton_app = hamilton_method(435, 2010)

print('Hamilton Method for 435 seats for 2010')

for i in range (0, 50):
    print(STATES[i] + ': ' + str(hamilton_app[i]))

lowndes_app = lowndes_method(435, 2010)

print('Lowndes Method for 435 seats for 2010')

for i in range (0, 50):
    print(STATES[i] + ': ' + str(lowndes_app[i]))

jefferson_app = jefferson_method(435, 2010)

print('Jefferson Method for 435 seats for 2010')

for i in range (0, 50):
    print(STATES[i] + ': ' + str(jefferson_app[i]))

adams_app = adams_method(435, 2010)

print('Adams Method for 435 seats for 2010')

for i in range (0, 50):
    print(STATES[i] + ': ' + str(adams_app[i]))

webster_app = webster_method(435, 2010)

print('Webster Method for 435 seats for 2010')

for i in range (0, 50):
    print(STATES[i] + ': ' + str(webster_app[i]))

huntington_hill_app = huntington_hill_method(435, 2010)

print('Huntington-Hill Method for 435 seats for 2010')

for i in range (0, 50):
    print(STATES[i] + ': ' + str(huntington_hill_app[i]))

dean_app = dean_method(435, 2010)

print('Dean Method for 435 seats for 2010')

for i in range (0, 50):
    print(STATES[i] + ': ' + str(dean_app[i]))

output([435, 436], [2010, 2010], ['dean', 'dean'], [12300, 12200])

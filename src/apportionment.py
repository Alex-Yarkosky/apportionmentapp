import math

def get_state_populations(year):
    ''' Parameters: census year
    Summary: gets populations for each states for given census year from a text file
    Return: list of state populations ordered alphabetically by state name '''

    try:
        file = ('../resources/census_data/{}population.txt').format(year)
        population_text = open(file, 'r')
    except:
        raise Exception('Please give a census year from 1900 to 2010 as Parameters')
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

def find_quota(state_pop, house_size, national_pop):
    ''' Parameters: population of a state, size of the House, population of the US states
    Return: population of a state divided by the given divisor '''

    return int(state_pop) / find_divisor(house_size, national_pop)

def hamilton_method(house_size, year, national_pop):
    ''' Choose the size of the house to be apportioned.
    Find the quotas and give to each state the whole number contained in its quota.
    Assign any seats which are yet unapportioned to those states having the largest fractions or remainders.
    -Fair Representation page 17 '''

    ''' Find quotas for each state assigning seats for the whole numbers of each quota.
    Assign the rest of the seats to states with the largest decimals in their quotas. '''

    state_pops = get_state_populations(year)
    quotas = []
    quotas_whole = []
    quotas_decimal = []

    # find quotas for each state
    for state_pop in state_pops:
        quota = find_quota(state_pop, house_size, national_pop)
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

    ''' Choose a divisor such that dividing the state populations by produces quotients whose whole numbers add up to the desired house size. '''

    return 0

def lowndes_method(house_size, year, national_pop):
    ''' Choose the size of the house to be apportioned.
    Find the quotas and give to each state the whole number contained in its quota.
    Adjust each state state's remainder by dividing by the whole number in its quota.
    Assign any seats which are as yet unapportioned to those states having the largest adjusted remainer.
    -Fair Representation page 25 '''

    ''' Modification of the Hamilton Method and how it distributes the final seats.
    Remaining seats go to the seats that would benefit the most from additional representation, typically smaller states. '''

    state_pops = get_state_populations(year)
    quotas = []
    quotas_whole = []
    quotas_decimal = []

    # find quotas for each state
    for state_pop in state_pops:
        quota = find_quota(state_pop, house_size, national_pop)
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

    return 0

def webster_method(house_size, year):
    ''' Choose the size of the house to be apportioned.
    Find a divisor x so that the whole numbers nearest to the quotients of the states sum to the required total.
    Give to each state its whole number.
    -Fair Representation page 32 '''

    ''' Modification of the Jefferson Method.
    Rounds quotients to the nearest whole number. '''

    return 0

def huntington_hill_method(house_size, year):
    ''' Choose the size of the house to be apportioned.
    Give to each state a number of seats so that no transfer of any one seat can reduce the percentage difference in represenation between those states.
    -Fair Representation page 48 '''

    ''' Prioritizes relative difference over absolute difference.
    Accounts for the fact that adding a seat to a state with few assigned to it has more of an effect than adding that seat to a state with a lot already assigned.
    Divides population of a state by the square root of the number of assigned seats multipled by the number of assigned seats minus 1.
    Uses results from that equation from each state to assign a seat to the seat with the largest result. '''

    return 0

def dean_method(house_size, year):
    ''' Choose the house to be apportioned.
    Find a divisor x so that the whole numbers which make the average constituencies of the states closest to x sum to the required total.
    Give to each state its whole number.
    -Fair Representation page 30'''

    ''' Proritizes absolute difference over relative difference.
    Same equation as the Huntington Hill Method except without the square root. '''

    return 0

# Create function to loop through multiple runs for data collection purposes (varying house sizes for 2010 data and varying years for 435 seats)

states_text = open('../resources/states.txt', 'r')
STATES = []
for line in states_text:
    stripped_line = line.strip()
    STATES.append(stripped_line)
# print(STATES)

hamilton_app = hamilton_method(435, 2010, find_national_pop(2010))

print('Hamilton Method for 435 seats for 2010')

for i in range (0, 50):
    print(STATES[i] + ': ' + str(hamilton_app[i]))

lowndes_app = lowndes_method(435, 2010, find_national_pop(2010))

print('Lowndes Method for 435 seats for 2010')

for i in range (0, 50):
    print(STATES[i] + ': ' + str(lowndes_app[i]))

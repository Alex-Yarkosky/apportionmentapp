def district_pop_difference(highest, lowest):
    return highest - lowest

def find_quota(state_pop, divisor):
    return state_pop / divisor

def find_national_pop(year):
    natl_pop = 0
    # loop through every state for the given year and add their pop to natl_pop
    return natl_pop

def hamilton_method(house_size, national_pop):
    ''' Choose the size of the house to be apportioned.
    Find the quotas and give to each state the whole number contained in its quota.
    Assign any seats which are yet unapportioned to those states having the largest fractions or remainders.
    -Fair Representation page 17 '''

    ''' ADD PERSONAL SUMMARY '''

    return 0

def jefferson_method():
    ''' Choose the size of the house to be apportioned.
    Find a divisor x so that the whole numbers contained in the quotients of the states sum to the required total.
    Give to each each state its whole number.
    -Fair Representation page 18 '''

    ''' ADD PERSONAL SUMMARY '''

    return 0

def lowndes_method():
    ''' Choose the size of the house to be apportioned.
    Find the quotas and give to each state the whole number contained in its quota.
    Adjust each state state's remainder by dividing by the whole number in its quota.
    Assign any seats which are as yet unapportioned to those states having the largest adjusted remainer.
    -Fair Representation page 25 '''

    ''' Modification of the Hamilton Method and how it distributes the final seats.
    Remaining seats go to the seats that would benefit the most from additional representation, typically smaller states. '''

    return 0

def adams_method():
    ''' Choose the size of the house to be apportioned.
    Find a divisor x so taht the smallest whole numbers containing the quotients of the states sum to the required total.
    Give to each state its whole number.
    -Fair Representation page 28 '''

    ''' Inversion of the Jefferson Method.
    Rounds quotients up instead of down. '''

    return 0

def webster_method():
    ''' Choose the size of the house to be apportioned.
    Find a divisor x so that the whole numbers nearest to the quotients of the states sum to the required total.
    Give to each state its whole number.
    -Fair Representation page 32 '''

    ''' ADD PERSONAL SUMMARY '''

    return 0

def huntington_hill_method():
    ''' Choose the size of the house to be apportioned.
    Give to each state a number of seats so that no transfer of any one seat can reduce the percentage difference in represenation between those states.
    -Fair Representation page 48 '''

    ''' ADD PERSONAL SUMMARY '''

    return 0

def dean_method():
    ''' Choose the house to be apportioned.
    Find a divisor x so that the whole numbers which make the average constituencies of the states closest to x sum to the required total.
    Give to each state its whole number.
    -Fair Representation page 30'''

    ''' Proritizes absolute difference over relative difference.
    Same equation as the Huntington Hill Method except without the square root. '''

    return 0

# Create function to loop through multiple runs for data collection purposes (varying house sizes for 2010 data and varying years for 435 seats)

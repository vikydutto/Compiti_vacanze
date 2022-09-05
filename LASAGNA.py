EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 30
TIME_LAYER = 2
def bake_time_remaining(elapsed_bake_time:int) -> int:
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(num_layers:int) -> int:
    '''
    :param num_layers:int numer of layers of the Lasagna
    :return: int the prepartion time in minutes
    '''
    return num_layers * TIME_LAYER
def elapsed_time_in_minutes(layers:int,time:int) -> int:
    '''    
    :param layers: int number of layers
    :param time: int the elapsed baking time
    :return: the total number of minutes to prepare and cook the lasagna
    '''
    return preparation_time_in_minutes(layers) + time

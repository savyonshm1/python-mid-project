# question 1 file
import random


def create_nums_str(start:int, end:int, step:int):
    """
    :param start, end & step: the limits of the loop and the num of steps
    :return: the string with the numbers
    """
    numbers_str = ""
    # for the range 1-9 or 9-1 (depends on the step parameter)
    for num in range(start, end, step):
        appearances = random.randint(1, 20)
        numbers_str += str(num) * appearances
    # returns the whole numbers string
    return numbers_str


def create_nums_file():
    # creating the string for the game
    with open("numbers_str_file.txt", 'w') as nums_file:
        nums_str = (create_nums_str(1, 10, 1) +
                         'TREASURE' + create_nums_str(9, 0, -1))
        nums_file.write(nums_str)


def main():
    # reading the numbers string from the file
    create_nums_file()  # 'w' parameter inside the function creates a new file / overrides existing content
    game_file = open("numbers_str_file.txt", 'r')  # won't raise an error,
                                                   # since a new file is created earlier if the file doesn't exist
    nums_treasure_str = game_file.read()

    # starting the game
    index = 0
    treasure_found = False
    while not treasure_found:
        steps = input(f'You are in a "{nums_treasure_str[index]}".\n'
                      f'How many steps do you wanna move (positive number to move forward, negative for backward)? \n'
                      f'Answer: ')

        # check if it's a valid, integer number
        if not steps.replace('-','').isdigit():  # to check if its only digits the '-' in negative nums is erased
            print('Your answer should contain digits only. Please try again.\n')
            continue

        # if the input raises another error
        try:
            steps = int(steps)
        except ValueError:
            print('This answer is invalid. Please try again\n.')
            continue

        # check if the number of steps is in the range of the string
        if steps > 0:
            # stepped too much steps forwards
            if index + steps >= len(nums_treasure_str):
                print('Too many steps forwards - out of range. Please try again.\n')
                continue
        elif steps < 0:
            # stepped too much steps backwards
            if index + steps < 0:
                print('Too many steps backwards - out of range. Please try again.\n')
                continue
        # 0 steps
        else:
            print("0 steps - you didn't move at all :( \ntry again\n")
            continue

        # if the code reached here the input is valid and in range
        index += steps  # updating the index
        # check if the treasure is found
        if nums_treasure_str[index].isalpha():  # the only letters in the str are the "treasure" letters
            treasure_found = True
            print("Congrats! You've found the treasure!!!")

    # closing the game file
    game_file.close()


if __name__ == '__main__':
    main()
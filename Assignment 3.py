# Define functions
# Define quarterback rating function
def quarterback(attempts, completions, passing_yards, touchdown_passes, interceptions):
    # The program calculates the rating
    rating = 100 * ((5 * (completions / attempts - 0.3)) + (0.25 * (passing_yards / attempts - 3)) + (
            20 * (touchdown_passes / attempts)) + 2.375 - (25 * interceptions / attempts)) / 6
    # if the rating is 158.3, the program says it is perfect
    if rating == 158.3:
        print("A perfect rating!")
    # The program prints the rating
    print("The rating is " + str(rating))


# Define quidditch score function
def quidditch(goals, snitch):
    # Calculate score
    score = (goals * 10) + (snitch * 30)
    # print score
    print("The score of the Quidditch game is: " + str(score))


# Define gymnastics
def gymnastics(difficulty, score1, score2, score3, score4, score5):
    # Calculate the average and add difficulty
    gymscore = ((score1 + score2 + score3 + score4 + score5) / 5) + difficulty
    # Print gymscore
    print("The score of the gymnast is: " + str(gymscore))


# Define the main function
def main():
    # ask user for choice of sports statistic
    choice = input("Choose what sports statistic you would like to calculate. (Quarterback Rating, Quidditch Score, "
                   "Gymnastics) ")
    choice = choice.strip().lower()
    # if choice is quarterback rating, request inputs and call quarterback function
    if choice == "quarterback rating":
        # request inputs
        attempt = int(input("Input number of attempts: "))
        comp = int(input("Input number of completions: "))
        passing = int(input("Input number of passing yards: "))
        touch = int(input("Input number of touchdown passes: "))
        intercept = int(input("Input number of interceptions: "))
        # call quarterback function if attempts is not 0
        if attempt > 0:
            quarterback(attempt, comp, passing, touch, intercept)
        else:
            print("Number of attempts must be greater than 0.")
    # if choice is quidditch score, request inputs and call quidditch function
    elif choice == "quidditch score":
        # request inputs
        goal = int(input("Input number of goals: "))
        caught = input("Was the snitch caught? (y/n) ")
        # process input for caught
        if caught == 'y':
            caught = 1
        else:
            caught = 0
        # call quidditch function
        quidditch(goal, caught)
    # if choice is gymnastics, request inputs and call gymnastics function
    elif choice == "gymnastics":
        # user inputs variables
        diff = int(input("Input the difficulty from 1 - 10: "))
        s1 = int(input("Input score 1: "))
        s2 = int(input("Input score 2: "))
        s3 = int(input("Input score 3: "))
        s4 = int(input("Input score 4: "))
        s5 = int(input("Input score 5: "))
        # Call gymnastics
        gymnastics(diff, s1, s2, s3, s4, s5)
    else:
        print("Not a valid choice.")


# Run main
main()

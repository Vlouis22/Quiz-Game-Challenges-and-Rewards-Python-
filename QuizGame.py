import random
import time

''' goal of this quiz game: 
    1. Developed a quiz game with multiple difficulty levels using Python

    2. Utilized random module to randomly select questions \
    from a pool of pre-defined questions

    3. Implemented input validation and error handling to ensure user input is valid

    4. Created a scoring system to track user progress and \
    display results upon completion of the quiz'''


def easy_game():
    # This is the easy level difficulty quiz.
    guesses = []
    correct_guesses = 0
    question_num = 1

    # Start the timer for elapsed time calculation
    start_time = time.time()

    # go with this set of question if the random module returns 1
    if random_pick_easy == 1:
        # Loops through the first predefined questions and asks questions
        for key in easy_questions:
            # print a blank line and then print the question after
            print()
            print(key)
            # This is to print the options for the question
            for i in easy_options[question_num - 1]:
                print(i)
            # get guess input
            guess = input("Enter (A, B, C, or D):")
            # This is to make sure that they user get a point if they answer using either upper case or lower case
            guess = guess.upper()
            # add guess to the guesses list
            guesses.append(guess)
            question_num += 1
            # Check the answer and gave the user a point if the guess is correct
            correct_guesses += check_answer(easy_questions.get(key), guess)
        # display the final scores after the game
        display_score(correct_guesses, guesses)

    # go with this set of question if the random module returns 2
    elif random_pick_easy == 2:
        for key in easy_questions_2:
            print()
            print(key)
            for i in easy_options_2[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D):")
            guess = guess.upper()

            # This is to make sure that they user get a point if they answer using either upper case or lower case

            guesses.append(guess)
            question_num += 1
            correct_guesses += check_answer(easy_questions_2.get(key), guess)
        display_score(correct_guesses, guesses)

    # go with this set of question if the random module returns 3
    else:
        for key in easy_questions_3:
            print()
            print(key)
            for i in easy_options_3[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D):")
            # This is to make sure that they user get a point if they answer using either upper case or lower case
            guess = guess.upper()
            guesses.append(guess)
            question_num += 1
            correct_guesses += check_answer(easy_questions_3.get(key), guess)
        display_score(correct_guesses, guesses)

    # end the timer and print the time elapsed when the game ends
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time = f'{elapsed_time:.2f}'
    print("Elapsed time: ", elapsed_time, "seconds")


def medium_game():
    # This is the medium level difficulty quiz
    guesses = []
    correct_guesses = 0
    question_num = 1

    start_time = time.time()

    if random_pick_medium == 1:
        for key in medium_questions:
            print()
            print(key)
            for i in medium_options[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D):")
            # This is to make sure that they user get a point if they answer using either upper case or lower case
            guess = guess.upper()
            guesses.append(guess)
            question_num += 1
            correct_guesses += check_answer(medium_questions.get(key), guess)
        display_score(correct_guesses, guesses)

    elif random_pick_medium == 2:
        for key in medium_questions_2:
            print()
            print(key)
            for i in medium_options_2[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D):")
            # This is to make sure that they user get a point if they answer using either upper case or lower case
            guess = guess.upper()
            guesses.append(guess)
            question_num += 1
            correct_guesses += check_answer(medium_questions_2.get(key), guess)
        display_score(correct_guesses, guesses)

    elif random_pick_medium == 3:
        for key in medium_questions_3:
            print()
            print(key)
            for i in medium_options_3[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D):")
            # This is to make sure that they user get a point if they answer using either upper case or lower case
            guess = guess.upper()
            guesses.append(guess)
            question_num += 1
            correct_guesses += check_answer(medium_questions_3.get(key), guess)
        display_score(correct_guesses, guesses)
    else:
        for key in medium_questions_4:
            print()
            print(key)
            for i in medium_options_4[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D):")
            # This is to make sure that they user get a point if they answer using either upper case or lower case
            guess = guess.upper()
            guesses.append(guess)
            question_num += 1
            correct_guesses += check_answer(medium_questions_4.get(key), guess)
        display_score(correct_guesses, guesses)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = f'{time_elapsed:.2f}'
    print("Elapsed time:", time_elapsed, "seconds")


def hard_game():
    # This is the hard level difficulty quiz
    guesses = []
    correct_guesses = 0
    question_num = 1

    start_time = time.time()

    if random_pick_hard == 1:
        for key in hard_questions:
            print()
            print(key)
            for i in hard_options[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D):")
            guess = guess.upper()

            # This is to make sure that they user get a point if they answer using either upper case or lower case

            guesses.append(guess)
            question_num += 1
            correct_guesses += check_answer(hard_questions.get(key), guess)
        display_score(correct_guesses, guesses)

    elif random_pick_hard == 2:
        for key in hard_questions_2:
            print()
            print(key)
            for i in hard_options_2[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D):")
            guess = guess.upper()

            # This is to make sure that they user get a point if they answer using either upper case or lower case

            guesses.append(guess)
            question_num += 1
            correct_guesses += check_answer(hard_questions_2.get(key), guess)
        display_score(correct_guesses, guesses)
    else:
        for key in hard_questions_3:
            print()
            print(key)
            for i in hard_options_3[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D):")
            # This is to make sure that they user get a point if they answer using either upper case or lower case
            guess = guess.upper()
            guesses.append(guess)
            question_num += 1
            correct_guesses += check_answer(hard_questions_3.get(key), guess)
        display_score(correct_guesses, guesses)

    # calculates the time elapsed while user is taking the quiz
    # displays the time taken at the end
    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = f'{time_elapsed:.2f}'
    print("Elapsed time:", time_elapsed, "seconds")


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        print("The correct answer is:", answer)
        return 0


def display_score(correct_guesses, guesses):
    print()
    print("Results:")
    # calculates the score percentage
    score = ((correct_guesses / len(guesses)) * 100)
    # score = f'{score:.2f}'
    score = int(score)
    print("Your score is: " + str(score) + "%")

    # if the game is easy and the user gets all the answers correct
    # it will ask the user if they would like to try a harder mode
    if game == 'easy' and score == 100:
        print("Too easy??? try a harder mode!")
    # if the user scores 100% in medium mode
    # it'll ask user if they want to try hard mode
    elif game == 'medium' and score == 100:
        print("You are too good, try the hard mode now!")
    # if user scores a 100% in hard mode then it will print you're a legend
    elif game == 'hard' and score == 100:
        print("You are a legend!")


def play_again():
    # This will ask the user if they want to play again,
    # if yes then they will need to choose what level difficulty, and if no, it will end the quiz
    response = input("Do you want to play again? (yes or no): ")
    # To run the game if the user use either capital letters or lowercase letters
    response = response.upper()

    if response == 'YES':
        return True
    else:
        return False


# this is the first set of easy questions and the answer key is on the right
easy_questions = {
    "What is the capital of California: ": "C",
    "What is the capital of New York: ": "D",
    "What is the capital of Texas: ": "A",
    "What is the capital of Georgia: ": "A",
    "What is the capital of Florida: ": "B",
}

# this is the second set of easy questions and the answer key is on the right
easy_questions_2 = {
    "What is the capital of Indiana: ": "A",
    "What is the capital of Ohio: ": "C",
    "What is the capital of Alabama: ": "D",
    "What is the capital of Massachusetts: ": "D",
    "What is the capital of New jersey: ": "D",
}

# this is the third set of easy questions and the answer key is on the right
easy_questions_3 = {
    "What is the capital of Virginia: ": "A",
    "What is the capital of Nevada: ": "C",
    "What is the capital of Illinois: ": "A",
    "What is the capital of Tennessee: ": "C",
    "What is the capital of South Carolina: ": "B",

}

# The options for the first set of easy questions
easy_options = [["A. Los Angeles", "B. San Francisco", "C. Sacramento", "D. San Jose"],
                ["A. Buffalo", "B. New York City", "C. Rochester", "D. Albany"],
                ["A. Austin", "B. Houston", "C. Dallas", "D. San Antonio"],
                ["A. Atlanta", "B. Augusta", "C. Columbus", "D. Savannah"],
                ["A. Miami", "B. Tallahassee", "C. Orlando", "D. Tampa"]]

# The options for the second set of easy questions
easy_options_2 = [["A. Indianapolis", "B. Fort Wayne", "C. Evansville", "D. Hammond"],
                  ["A. Cincinnati", "B. Toledo", "C. Columbus", "D. Cleveland"],
                  ["A. Birmingham", "B. Huntsville", "C. Alabama City", "D. Montgomery"],
                  ["A. Springfield", "B. Cambridge", "C. Worcester", "D. Boston"],
                  ["A. Newark", "B. Paterson", "C. Jersey City", "D. Trenton"]]

# The options for the third set of easy questions
easy_options_3 = [["A. Richmond", "B. Virginia Beach", "C. Chesapeake", "D. Virginia City"],
                  ["A. Las Vegas", "B. North Las Vegas", "C. Carson City", "D. Reno"],
                  ["A. Springfield", "B. Chicago", "C. Naperville", "D. Aurora"],
                  ["A. Memphis", "B. Knoxville", "C. Nashville", "D. Clarksville"],
                  ["A. Mount Pleasant", "B. Columbia", "C. Rock Hill", "D. Charleston"]]

# this is the first set of medium questions and the answer key is on the right
medium_questions = {
    "What is the capital of Arizona: ": "C",
    "What is the capital of Arkansas: ": "A",
    "What is the capital of Colorado: ": "C",
    "What is the capital of Delaware: ": "A",
    "What is the capital of Louisiana: ": "D",
}
# this is the second set of medium questions and the answer key is on the right
medium_questions_2 = {
    "What is the capital of Maryland: ": "D",
    "What is the capital of Minnesota: ": "B",
    "What is the capital of Missouri: ": "D",
    "What is the capital of New Hampshire: ": "C",
    "What is the capital of New Mexico: ": "A",
}
# this is the third set of medium questions and the answer key is on the right
medium_questions_3 = {
    "What is the capital of Oklahoma: ": "C",
    "What is the capital of Oregon: ": "A",
    "What is the capital of Pennsylvania: ": "B",
    "What is the capital of Rhode Island: ": "D",
    "What is the capital of South Dakota: ": "B",

}
# this is the fourth set of medium questions and the answer key is on the right
medium_questions_4 = {
    "What is the capital of Utah: ": "B",
    "What is the capital of Vermont: ": "D",
    "What is the capital of Wisconsin: ": "A",
    "What is the capital of Wyoming: ": "B",
    "What is the capital of Mississippi: ": "C",

}
# The options for the first set of medium questions
medium_options = [["A. Tucson", "B. Mesa", "C. Phoenix", "D. Chandler"],
                  ["A. Little Rock", "B. Fort Smith", "C. Fayetteville", "D. Springdale"],
                  ["A. Colorado Springs", "B. Aurora", "C. Denver", "D. Fort Collins"],
                  ["A. Dover", "B. Wilmington", "C. Newark", "D. Milford"],
                  ["A. New Orleans", "B. Shreveport", "C. Lafayette", "D. Baton Rouge"]]

# The options for the second set of medium questions
medium_options_2 = [["A. Baltimore", "B. Columbia", "C. Germantown", "D. Annapolis"],
                    ["A. Minneapolis", "B. Saint Paul", "C. Rochester", "D. Minnesota City"],
                    ["A. Kansas City", "B. St. Louis", "C. Springfield", "D. Jefferson City"],
                    ["A. Nashva", "B. Manchester", "C. Concord", "D. Dover"],
                    ["A. Santa Fe", "B. Albuquerque", "C. Las Cruces", "D. Rio Rancho"]]

# The options for the third set of medium questions
medium_options_3 = [["A. Tulsa", "B. Norman", "C. Oklahoma City", "D. Broken Arrow"],
                    ["A. Salem", "B. Portland", "C. Eugene", "D. Gresham"],
                    ["A. Philadelphia", "B. Harrisburg", "C. Pittsburgh", "D. Allentown"],
                    ["A. Warwick", "B. Cranston", "C. Pawtucket", "D. Providence"],
                    ["A. Sioux Falls", "B. Pierre", "C. Rapid City", "D. Watertown"]]

# The options for the fourth set of medium questions
medium_options_4 = [["A. West Valley City", "B. Salt Lake City", "C. East Valley City", "D. North Valley City"],
                    ["A. Burlington", "B. South Burlington", "C. North Burlington", "D. Montpelier"],
                    ["A. Madison", "B. Milwaukee", "C. Green Bay", "D. Kenosha"],
                    ["A. Casper", "B. Cheyenne", "C. Laramie", "D. Gillette"],
                    ["A. Gulfport", "B. Southaven", "C. Jackson", "D. Hattiesburg"]]

# this is the first set of hard questions and the answer key is on the right
hard_questions = {
    "What is the capital of Alaska: ": "A",
    "What is the capital of Connecticut: ": "B",
    "What is the capital of Hawaii: ": "A",
    "What is the capital of Idaho: ": "B",
    "What is the capital of Iowa: ": "C",
}
# this is the second set of hard questions and the answer key is on the right
hard_questions_2 = {
    "What is the capital of Kansas: ": "D",
    "What is the capital of Kentucky: ": "A",
    "What is the capital of Maine: ": "A",
    "What is the capital of Michigan: ": "C",
    "What is the capital of Montana: ": "C",
}
# this is the third set of easy questions and the answer key is on the right
hard_questions_3 = {
    "What is the capital of North Carolina: ": "B",
    "What is the capital of North Dakota: ": "A",
    "What is the capital of Washington: ": "B",
    "What is the capital of West Virginia: ": "D",
    "What is the capital of Nebraska: ": "D",

}
# The options for the first set of hard questions
hard_options = [["A. Juneau", "B. Anchorage", "C. Fairbanks", "D. Wasilla"],
                ["A. Bridgeport", "B. Hartford", "C. New Haven", "D. Stanford"],
                ["A. Honolulu", "B. Hilo", "C. Kailua", "D. Pearl City"],
                ["A. Nampa", "B. Boise", "C. Idaho Falls", "D. Meridian"],
                ["A. Cedar Rapids", "B. Davenport", "C. Des Moines", "D. Sioux City"]]

# The options for the second set of hard questions

hard_options_2 = [["A. Wichita", "B. Kansas City", "C. Overland Park", "D. Topeka"],
                  ["A. Frankfort", "B. Louisville", "C. Lexington", "D. Bowling Green"],
                  ["A. Augusta", "B. Portland", "C. Lewiston", "D. Bangor"],
                  ["A. Detroit", "B. Grand Rapids", "C. Lansing", "D. Warren"],
                  ["A. Billings", "B. Missoula", "C. Helena", "D. Great Falls"]]

# The options for the third set of hard questions

hard_options_3 = [["A. Charlotte", "B. Raleigh", "C. Greensboro", "D. Durham"],
                  ["A. Bismarck", "B. Fargo", "C. Grand Forks", "D. Minot"],
                  ["A. Seattle", "B. Olympia", "C. Spokane", "D. Tacoma"],
                  ["A. Huntington", "B. Morgantown", "C. Parkersburg", "D. Charleston"],
                  ["A. Lincoln", "B. Omaha", "C. Bellevue", "D. Grand Island"]]

# This is asking the user what quiz level difficulty they would like to play


random_pick_easy = random.randrange(1, 4)
random_pick_medium = random.randrange(1, 5)
random_pick_hard = random.randrange(1, 4)

# This ask the user what level difficulty they would like for their first quiz
game = input("Enter level difficulty, (easy, medium, or hard): ")
game = game.lower()
# if user type 'easy' then it will choose the easy quiz game
if game == 'easy':
    easy_game()
# if user type 'medium' then it will choose the medium quiz game
if game == 'medium':
    medium_game()
# if user type 'hard' then it will choose the hard quiz game
if game == 'hard':
    hard_game()

while play_again():
    game = input("Enter level difficulty, (easy, medium, or hard?): ")
    # Accepts input in either capital letters or lowercase letters

    game = game.lower()
    # This will randomly pick from the options when the user wants to play again
    # depending on what level difficulty they want to play
    if game == 'easy':
        random_pick_easy = random.randrange(1, 4)
        easy_game()
    if game == 'medium':
        random_pick_medium = random.randrange(1, 5)
        medium_game()
    if game == 'hard':
        random_pick_hard = random.randrange(1, 4)
        hard_game()

# If the user does not want to play again, it will print "thank you for playing" at the end of the quiz

print("""Thanks for playing
Have a nice day!""")

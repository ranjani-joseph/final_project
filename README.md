Metadata

Name   : Sivaranjani Kandasami
Project: Monte Carlo Simulator

Synopsis

Importing and Installing:
The package is available in GIT: https://github.com/ranjani-joseph/DS5100-2022-08-nyc2xu.git in the folder 'Project'
Download the folder to the desired location and use following command to install the package:
!pip install -e .


Run the tests with following command. All tests should pass with no errors
rivanna$ python montecarlo_test.py

Save results in a file named montecarlo_test_results.txt. 
rivanna$ python booklover_test.py 2> booklover_results.txt

Creating dice objects:
Create die object using a die class by parsing the faces of the die. Coins or cards could also be used

Playing games:
Play games i.e, roll a die or a number of dice using the Game class with the created die objects (using Die class)


Analyzing games:
The game results are stored in a dataframe which can be analyzed using the Analyze class.
This class can help to determine the cobminations or the jackpots(same face in all dice in a roll)

#----------Example-----------#

faces = ['H','T'] # Faces of the Coin
num_roll = 10     # Number of times the coin should be fliped. Weights are defaulted to 1 for each face but it can be changed using weight method

fair_coin = Die(faces)                # Create a coin object
fair_coin_face_list = fair_coin.faces # Faces of the coin object created
fair_coin.show()                      # Dataframe with faces and its weight

#Create 3 coin list
fair_coin_list = []
for i in range(3):
    fair_coin_list.append(fair_coin)

fair_game = Game(fair_coin_list)  # A game object is created with list of coins
fair_game.play(num_roll)          # Roll the die 'num_roll' times i.e, 10 times
fair_game.show()                  # Dataframe with games played with 3 coins rolled 10 times.

#Analyze if the game resulted in jackpot i.e, all die had same face in a game.
analyze_fair_game = Analyzer(fair_game.show())
fair_game_jackpot = analyze_fair_game.jackpot()

#----------End of Example-----------#


API description:

The Die class:

Docstring: A die has N sides, or “faces”, and W weights, and can be rolled to select a face.W defaults to 1.0 for each face but can be changed after the object is created.Note that the weights are just numbers, not a normalized probability distribution.The die has one behavior, which is to be rolled one or more times.
Note that what we are calling a “die” here can represent a variety of random variables associated with stochastic processes, such as using a deck of cards or flipping a coin or speaking a language. We can create these models by increasing the number of sides and defining the values of their faces. Our probability models for such variables are, however, very simple – since our weights apply to only to single events, we are assuming that the events are independent.  
Specific Methods and Attributes

Initializer() : Takes an array of faces as an argument.The array's data type (dtype) may be strings or numbers.The faces must be unique; no duplicates.Internally iInitializes the weights to 1.0 for each face.Saves faces and weights in a private dataframe that is to be shared by the other methods.
Change Weight: A method to change the weight of a single side.Takes two arguments: the face value to be changed and the new weight.Checks to see if the face passed is valid; is it in the array of weights?Checks to see if the weight is valid; is it a float? Can it be converted to one?

Roll():  A method to roll the die one or more times.Takes a parameter of how many times the die is to be rolled; defaults to 1.This is essentially a random sample from the vector of faces according to the weights.Returns a list of outcomes.Does not store internally these results.

Show(): A method to show the user the die’s current set of faces and weights (since the latter can be changed).Returns the dataframe created in the initializer but possibly updated by the weight changing method.


The Game class:

Docstring:Game class consists of rolling of one or more dice of the same kind one or more times.Each game is initialized with a list of one or more of similarly defined dice (Die objects). By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and set of faces, but each die object may have its own weights.The class has a behavior to play a game, i.e. to roll all of the dice a given number of times.The class keeps the results of its most recent play.


Initializer: Takes a single parameter, a list of already instantiated similar Die objects.

Play() :  Takes a parameter to specify how many times the dice should be rolled.Saves the result of the play to a private dataframe of shape N rolls by M dice.That is, each role is an observation and each column is a feature. Each cell should show the resulting face for the die on the roll. Note that this table is in wide form.The private dataframe should have the roll number as a named index.

Show() : A method to show the user the results of the most recent play.This method just passes the private dataframe to the user.Takes a parameter to return the dataframe in narrow or wide form.This parameter defaults to wide form, which is what the previously described method produces.
This parameter should raise an exception if the user passes an invalid option.The narrow form of the dataframe will have a two-column index with the roll number and the die number, and a single column for the face rolled.


The Analyzer class:

An analyzer takes the results of a single game and computes various descriptive statistical properties about it.A face counts per roll, i.e. the number of times a given face appeared in each roll. For example, if a roll of five dice has all sixes, then the counts for this roll would be 6 for the face value '6' and 0 for the other faces. A jackpot count, i.e. how many times a roll resulted in all faces being the same, e.g. six ones for a six-sided die. A combo count, i.e. how many combination types of faces were rolled and their counts. A permutation count, i.e. how may sequence types were rolled and their counts.


Initializer() : Takes a game object as its input parameter.At initialization time, it also infers the data type of the die faces used.A face counts per roll method to compute how many times a given face is rolled in each event.Stores the results as a dataframe in a public attribute.The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format)

Face_counts_per_roll(): A face counts per roll method to compute how many times a given face is rolled in each event.Stores the results as a dataframe in a public attribute.The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format).

Combo() : A combo method to compute the distinct combinations of faces rolled, along with their counts.Combinations should be sorted and saved as a multi-columned index.Stores the results as a dataframe in a public attribute.

Jackpot() : A jackpot method to compute how many times the game resulted in all faces being identical. Returns an integer for the number times to the user. Stores the results as a dataframe of jackpot results in a public attribute. The dataframe should have the roll number as a named index.




# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


class Die:
    '''A die has N sides, or “faces”, and W weights, and can be rolled to select a face.

       W defaults to 1.0 for each face but can be changed after the object is created.
       Note that the weights are just numbers, not a normalized probability distribution.
       The die has one behavior, which is to be rolled one or more times.
       Note that what we are calling a “die” here can represent a variety of random variables associated with stochastic processes, such as using a deck of cards or flipping a coin or speaking a language. 
       We can create these models by increasing the number of sides and defining the values of their faces. 
       Our probability models for such variables are, however, very simple – since our weights apply to only to single events, we are assuming that the events are independent.'''
    def __init__(self,faces):
        '''Initializer takes an array of faces as an argument.
        The array's data type (dtype) may be strings or numbers.
        The faces must be unique; no duplicates.
        Internally iInitializes the weights to 1.0 for each face.
        Saves faces and weights in a private dataframe that is to be shared by the other methods.'''
    
        self.faces = list(set(faces)) # array of strings or numbers
        self.weights =  [1.0 for self.face in range(len(self.faces))] # array of integers
        self.die = pd.DataFrame({'faces':self.faces, 'weights':self.weights}) #dataframe with faces and weights
    
        
    def change_weight(self,face_value,new_weight):
        '''This method is to change the weight of a single side.
        Takes two arguments: the face value to be changed and the new weight.
        Checks to see if the face passed is valid; is it in the array of weights?
        Checks to see if the weight is valid; is it a float? Can it be converted to one?'''
        self.checks = []
        if (type(face_value)==str or type(face_value)==int) and face_value in self.faces:
            self.checks.append(True)
#             print("Checks passed,valid face value and weight")
        else:
            self.checks.append(False)
            print("Face value should be array of strings or integer.  ")
            
        try:
            self.weight=float(new_weight)
            self.checks.append(True)
        except:
            print("Weight cannot be converted to float")
            self.checks.append(False)
        
        if self.checks:
            self.i = self.faces.index(face_value)
            self.weights[self.i] = new_weight
        else:
            print("Checks failed. Pass valid face value and weight")
            
        self.die = pd.DataFrame({'faces':self.faces, 'weights':self.weights})            
        return self.die
        
    def roll(self,num_roll=1):
        '''This method is to roll the die one or more times.
        Takes a parameter of how many times the die is to be rolled; defaults to 1.
        This is essentially a random sample from the vector of faces according to the weights.
        Returns a list of outcomes.
        Does not store internally these results.'''    
        return list(self.die.sample(n=num_roll,weights='weights',replace=True)['faces'])
         
    def show(self):
        '''This method is to show the user the die’s current set of faces and weights (since the latter can be changed).
        Returns the dataframe created in the initializer but possibly updated by the weight changing method.'''
        return self.die
    
    
    
class Game:
    '''Game class consists of rolling of one or more dice of the same kind one or more times.
       Each game is initialized with a list of one or more of similarly defined dice (Die objects).
       By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and set of faces, but each die object may have its own weights.
       The class has a behavior to play a game, i.e. to roll all of the dice a given number of times.
       The class keeps the results of its most recent play.'''
    
    
    def __init__(self,dice):
        '''Takes a single parameter, a list of already instantiated similar Die objects.'''
        self.dice = dice
    
    def play(self,num_roll):
        '''Takes a parameter to specify how many times the dice should be rolled. Saves the result of the play to a private dataframe of shape N rolls by M dice.
        That is, each role is an observation and each column is a feature. Each cell should show the resulting face for the die on the roll. Note that this table is in wide form.
        The private dataframe should have the roll number is a named index.'''
        self.num_roll = num_roll
        self.play_result = pd.DataFrame()
        n=1
        for die in self.dice:
            self.result = die.roll(num_roll)
            self.play_result['Die'+str(n)] = self.result
            n+= 1
        
        self.play_result['Roll']=list(np.arange(1,num_roll+1))
        self.result_df = self.play_result.set_index('Roll')
        return self.result_df
            
    def show(self,df_form='wide'):
        '''This method just passes the private dataframe to the user.
        Takes a parameter to return the dataframe in narrow or wide form.
        This parameter defaults to wide form, which is what the previously described method produces.
        This parameter should raise an exception if the user passes an invalid option.
        The narrow form of the dataframe will have a two-column index with the roll number and the die number, and a single column for the face rolled.
        As a reminder, the wide form of the dataframe will a have single column index with the roll number, and each die number as a column.'''
        
        self.df_form = df_form
        if self.df_form == 'wide':
#             print("wide")
            self.df_to_return = self.result_df
        elif df_form == 'narrow':   
            self.df_to_return = self.result_df.stack().to_frame('Face')
        else:
            raise Exception("Dataframe form should be wide or narrow")
        return self.df_to_return
    
    
class Analyzer:
    def __init__(self,game):
        '''Takes a game object as its input parameter.At initialization time, it also infers the data type of the die faces used.'''
        self.game = game
    
    def face_counts_per_roll(self):
        '''A face counts per roll method to compute how many times a given face is rolled in each event.
        Stores the results as a dataframe in a public attribute.
        The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format).'''
        face_counts_per_roll = pd.DataFrame()
        for i in range(len(self.game)):
            each_roll = pd.DataFrame(self.game.iloc[i].value_counts()).transpose()
            face_counts_per_roll = face_counts_per_roll.append(each_roll)
        face_counts_per_roll.index.name = 'Game'
        return face_counts_per_roll
    
    def combo(self):
        '''A combo method to compute the distinct combinations of faces rolled, along with their counts.
        Combinations should be sorted and saved as a multi-columned index.
        Stores the results as a dataframe in a public attribute.
        Note that this class helps compute the jackpot, since a jackpot is a combination in which only one face appears.'''
        self.combo_results = pd.DataFrame()
        for i in range(len(self.game)):
            self.combo_results = self.combo_results.append(pd.DataFrame(self.game.iloc[i].value_counts()).transpose())
            self.combo_results.index.name = "Roll"
        return self.combo_results
                                     
    
    def jackpot(self):
        '''A jackpot method to compute how many times the game resulted in all faces being identical.
        Returns an integer for the number times to the user.
        Stores the results as a dataframe of jackpot results in a public attribute.
        The dataframe should have the roll number as a named index.'''
        jackpot_results = pd.DataFrame()
        analyzer = Analyzer(self.game)
        self.combo_results = analyzer.combo()
        for i in range(len(self.combo_results)):
            if self.combo_results.iloc[i].count()==1:
                jackpot_results = jackpot_results.append(self.combo_results.iloc[i])
        all_faces_identical = len(jackpot_results)
        return all_faces_identical
          
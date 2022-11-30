import unittest
import numpy as np

import pkg_mc
from imp import reload
reload(pkg_mc)
from pkg_mc.montecarlo import *


class MonteCarloTestSuite(unittest.TestCase):
    def test_test(self):
        self.assertTrue(True)
        
    # 'test_1_change_weight()': Change weight of a face in list of faces.
    # 'test_2_roll_die()': Roll die 2 times and store results in dataframe
    # 'test_3_die_show()': Show faces of die
    # 'test_4_game_play()': Play game twice and see results
    # 'test_5_face_counts()': Count faces of game
    # 'test_6_combo()': Verify if the combos are summed
    # 'test_7_jackpot()': Verify jackpot results are correct

    
    def test_1_die_change_weight(self):
        # Change weight of a face
        faces_list = [2,3,4,5]
        mc_change_weight = Die(faces_list)
        df = mc_change_weight.change_weight(2,6)
        assert (df['weights'][0] == 6)
        
    def test_2_die_roll(self):
        # Roll die 2 times and store results in dataframe
        faces_list = [2,3,4,5]
        die = Die(faces_list)
        roll_list = die.roll(2)
        assert (len(roll_list) == 2)
        
    def test_3_die_show(self):
        # Roll die 2 times and store results in dataframe
        faces_list = [2,3,4,5]
        die = Die(faces_list)
        df = die.show()
        assert (len(df) == 4)
                  
    def test_4_game_play(self):
        # Play game and store the results in a wide dataframe
        faces_list = [1,2,3,4,5]
        die1 = Die(faces_list)
        die2 = Die(faces_list)
        dice_list = [die1,die2]
        game = Game(dice_list)
        game_play = game.play(4)
        game.show("wide")
        assert len(game_play)==4
               
    def test_5_face_counts(self):
        # Count faces of game
        df = pd.DataFrame({'Game':[1,2,3,4], 'die1':[2,6,4,7], 'die2':[4,8,4,2], 'die3':[1,5,4,6]})
        df = df.set_index('Game')
        analyze = Analyzer(df)
        face_counts = analyze.face_counts_per_roll()
        assert (face_counts.iloc[3][6] ==1)
      
    def test_6_combo(self):
        # Verify if the combos are summed
        df = pd.DataFrame({'Game':[1,2,3,4], 'die1':[2,6,4,7], 'die2':[4,8,4,2], 'die3':[1,5,4,6]})
        df = df.set_index('Game')
        analyze = Analyzer(df)
        game_combo = analyze.combo()
        assert (game_combo.iloc[2][4] == 3)
        
    def test_7_jackpot(self):
        #Verify jackpot results are correct
        df = pd.DataFrame({'Game':[1,2,3,4], 'die1':[2,6,4,7], 'die2':[4,8,4,2], 'die3':[1,5,4,6]})
        df = df.set_index('Game')
        analyze = Analyzer(df)
        game_combo = analyze.jackpot()
        assert (game_combo == 1)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
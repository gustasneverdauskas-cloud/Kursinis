import unittest
from main import Navigator #importuojamas navigatorius is maino

class TestNavigator(unittest.TestCase):
    def setUp(self):               #sukuriamas navigatorius pries kiekviena testa
        self.nav = Navigator()
        self.obs = set()           #nera kliuciu

    def test_path_found(self):
        start = (0, 0) #ar navigatorius suras kelia
        goal = (0, 2)
        path = self.nav.find(start, goal, self.obs)
        
        self.assertTrue(len(path) > 0) #kelias tuscias
        self.assertEqual(path[-1], goal)

    def test_obstacle_avoidance(self): #atsiranda kliutis
        start = (0, 0) 
        goal = (2, 0)
        obstacles = {(1, 0)} #kliutis
        
        path = self.nav.find(start, goal, obstacles)
        
        self.assertTrue(len(path) > 0) #ar rastas kelias
        self.assertNotIn((1, 0), path)

    def test_no_path(self): #jei taskas nepasiekiamas
        start = (0, 0)
        goal = (2, 2)
        obstacles = {(0, 1), (1, 0), (1, 1)}
        
        path = self.nav.find(start, goal, obstacles)
        self.assertEqual(path, [])   #turi grazinti tuscia sarasa

if __name__ == '__main__':
    unittest.main()

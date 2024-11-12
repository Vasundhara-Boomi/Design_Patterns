import unittest

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class TestSingleton(unittest.TestCase):

    def test_singleton_instance(self):
        s1 = Singleton()
        s2 = Singleton()
        self.assertIs(s1, s2)
    
    def test_singleton_type(self):
        s1 = Singleton()
        s2 = Singleton()
        self.assertIsInstance(s1, Singleton)
        self.assertIsInstance(s2, Singleton)

if __name__ == '__main__':
    unittest.main()
    
    

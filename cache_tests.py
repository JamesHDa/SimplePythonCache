import cache
import unittest
import time

class CacheTests(unittest.TestCase):
    def testAdding(self):
        self.assertEqual(cache.add("a","result",10),True)
    def testRetreving(self):
        self.assertEqual(cache.add("a","result",10),True)
        self.assertEqual(cache.get('a'),'result')
    def testExpired(self):
        self.assertEqual(cache.add("a","result",1),True)
        time.sleep(1)
        self.assertEqual(cache.get('a'),False)
    def testClear(self):
        cache.add("a","result",2)
        self.assertEqual(cache.get('a'),'result')
        self.assertEqual(cache.clear(),True)
        self.assertEqual(cache.get('a'),False)
    def testRemove(self):
        cache.add("a","result",2)
        self.assertEqual(cache.get('a'),'result')
        self.assertEqual(cache.remove('a'),True)
        self.assertEqual(cache.get('a'),False)
        
if __name__ == '__main__':
    unittest.main()

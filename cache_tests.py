import cache
import unittest
import time

class SampleResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
    	self.content = content
    

GOOD_RESPONSE = SampleResponse (200, 'result')
BAD_RESPONSE = SampleResponse (400, 'no result')

class CacheTests(unittest.TestCase):

    def testAdding(self):
        self.assertEqual(cache.add("a",GOOD_RESPONSE,10),True)
    def testAdding400Response(self):
        self.assertEqual(cache.add("b",BAD_RESPONSE,10),False)
    def testAddingAndGetting400Response(self):
        self.assertEqual(cache.add("b",BAD_RESPONSE,10),False)
        self.assertEqual(cache.get('b'), False)
    def testRetreving(self):
        self.assertEqual(cache.add("a",GOOD_RESPONSE,10),True)
        self.assertEqual(cache.get('a'),'result')
    def testExpired(self):
        self.assertEqual(cache.add("a",GOOD_RESPONSE,1),True)
        time.sleep(1)
        self.assertEqual(cache.get('a'),False)
    def testClear(self):
        cache.add("a",GOOD_RESPONSE,2)
        self.assertEqual(cache.get('a'),'result')
        self.assertEqual(cache.clear(),True)
        self.assertEqual(cache.get('a'),False)
    def testRemove(self):
        cache.add("a",GOOD_RESPONSE,2)
        self.assertEqual(cache.get('a'),'result')
        self.assertEqual(cache.remove('a'),True)
        self.assertEqual(cache.get('a'),False)
        
if __name__ == '__main__':
    unittest.main()

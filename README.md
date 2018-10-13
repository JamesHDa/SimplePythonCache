# SimplePythonCache
A simple python cacheing dictonary; for use with 3rd party api calls for example; i.e. an weather forecast api.

Configue the number of items you wish to store in the cache at one time by changing MAX_SIZE in config.py

Then reference with import SimplePythonCache.Cache as Cache
Add to the cache by Cache.add('CacheKey','response',Seconds before expired)

You can retrieve from the cache with Cache.get('CacheKey') or remove from the cache with Cache.remove('CacheKey')

You can clear the entire cache with Cache.clear()

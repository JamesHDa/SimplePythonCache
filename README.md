# SimplePythonCache
A simple python cacheing dictonary; for use with own api calls or 3rd party api calls; i.e. a weather forecast api.

Configure the number of items you wish to store in the cache at one time by changing MAX_SIZE in config.py

Then reference with import SimplePythonCache.Cache as Cache

Add to the cache by Cache.add('CacheKey',Response,Seconds until expiration)

You can retrieve from the cache with Cache.get('CacheKey') or remove from the cache with Cache.remove('CacheKey')

You can clear the entire cache with Cache.clear()

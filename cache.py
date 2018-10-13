import random
import config
import datetime as dt



def add(name,response,time):
    if response.status_code < 400: 
        try:
            if len(cache) == maxItems:  
                remove()
            expires = dt.datetime.now() + dt.timedelta(0,time)
            cache[name]=[response.content,expires]
            get(name)
            return True
        except:
            return False
    return False

def get(name):
    try:
        if name in cache:
            if (check(cache[name][1])):
                return cache[name][0]
            else:
                remove(name)
        return False
    except:
        return False

def check(expires):
    if expires > dt.datetime.now():
        return True
    return False

def remove(x =""):
    try:
        if x == "":
            #print("removing cache")
            key = random.choice(cache.keys())
            del cache[key]
            #print ("removed " + key)
        else:
            del cache[x]
        return True
    except:
        return False
def clear():
    cache.clear()
    return True
    
cache = {}
maxItems = config.MAX_SIZE

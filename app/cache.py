import redis
import time
import json

r = redis.Redis(host='localhost', port=6379, db=0)

# def cache_response(key, value, timeout=300):
#     r.setex(key, timeout, value)

# def get_cached_response(key):
#     return r.get(key)
def cache_response(key, value, timeout=300):
    # Convert the list to a JSON string before caching
    r.setex(key, timeout, json.dumps(value))

def get_cached_response(key):
    cached_value = r.get(key)
    if cached_value:
        # Convert the JSON string back to a Python list
        return json.loads(cached_value)
    return None

def log_inference_time(user_id, start_time):
    end_time = time.time()
    r.lpush(f'{user_id}_inference_time', end_time - start_time)

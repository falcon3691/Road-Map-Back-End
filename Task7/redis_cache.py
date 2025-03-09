import redis
import json
# Redis'e bağlanma
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Bağlantıyı test et
def test():
    redis_client.set("message", "Hello Redis!")
    print(redis_client.get("message"))

def getCachedData(key): 
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data)  # JSON string'den Python dict'e çevir
    return None

def setCacheData(key, data, expiration=3600):
     redis_client.setex(key, expiration, json.dumps(data))

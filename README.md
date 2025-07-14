# Caching in Django: Property Listings App — Django + Redis Caching

This project demonstrates efficient data caching in a Django-based property listing application, using Redis as the caching backend and PostgreSQL for persistent storage. Docker is used to containerize all services.

---

## Tech Stack
- Django
- Redis + django-redis
- PostgreSQL
- Docker / Docker Compose

---

## Features Implemented

### Core Goals
- Optimize performance by reducing database hits
- Cache queryset and view responses using Redis
- Auto-invalidate cache on data change (create/update/delete)
- Monitor Redis cache metrics (hit/miss ratio)

---

## Objectives

### Docker Setup
- PostgreSQL for relational data
- Redis for caching
- Django connected to both via environment config

### Property Caching
- Cached `Property.objects.all()` result using Django’s low-level cache API
- Stored in Redis under the key `all_properties`
- TTL set to `3600` seconds (1 hour)

### Cache Invalidation
- Used Django signals (`post_save`, `post_delete`) to clear cache when a `Property` is created, updated, or deleted
- Ensures users always get up-to-date property listings

### View Caching
- Cached the entire `/properties/` endpoint using `@cache_page(60 * 15)`
- Reduces response time for frequently accessed endpoints

### Redis Cache Metrics
- Implemented a utility to pull `keyspace_hits` and `keyspace_misses`
- Calculates and logs real-time cache hit ratio for monitoring

---


## Sample Usage

```bash
# Fetch property list
curl http://localhost:8000/properties/

# View Redis keys
docker exec -it <redis_container> redis-cli
keys *

# Run Redis metrics in Django shell
python manage.py shell
>>> from properties.utils import get_redis_cache_metrics
>>> get_redis_cache_metrics()


---

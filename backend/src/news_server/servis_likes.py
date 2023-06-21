import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def add_like(news_id, user_id):
    r.hincrby('news_likes', news_id, amount=1)
    # Дополнительно можно сохранить информацию о пользователе, поставившем лайк
    r.sadd(f'news_{news_id}_liked_by', user_id)

def remove_like(news_id, user_id):
    r.hincrby('news_likes', news_id, amount=-1)
    # Удалить информацию о пользователе, который удалил свой лайк
    r.srem(f'news_{news_id}_liked_by', user_id)

def get_likes_count(news_id):
    return r.hget('news_likes', news_id)

def is_liked_by_user(news_id, user_id):
    return r.sismember(f'news_{news_id}_liked_by', user_id)
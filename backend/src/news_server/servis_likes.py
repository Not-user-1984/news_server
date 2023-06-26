import redis


r = redis.Redis(host='redis', port=6379, db=0) 


def add_like(news_id=None, comment_id=None, user_id=None):
    """Добавить лайк к новости или комментарию"""
    if news_id is not None:
        r.hincrby('news_likes', news_id, amount=1)
        r.sadd(f'news_{news_id}_liked_by', user_id)

    elif comment_id is not None:
        r.hincrby('comments_likes', comment_id, amount=1)
        r.sadd(f'comments_{comment_id}_liked_by', user_id)


def remove_like(news_id=None, comment_id=None, user_id=None):
    """Удалить лайк у новости или комментария"""
    if news_id is not None:
        r.hincrby('news_likes', news_id, amount=-1)
        r.srem(f'news_{news_id}_liked_by', user_id)

    elif comment_id is not None:
        r.hincrby('comments_likes', comment_id, amount=-1)
        r.srem(f'comments_{comment_id}_liked_by', user_id)


def get_likes_count(news_id=None, comment_id=None):
    """Получить количество лайков у новости или комментария"""
    if news_id is not None:
        return r.hget('news_likes', news_id)

    elif comment_id is not None:
        return r.hget('comments_likes', comment_id)


def is_liked_by_user(news_id=None, comment_id=None, user_id=None):
    """Проверить, поставил ли пользователь лайк к новости или комментарию"""
    if news_id is not None:
        return r.sismember(f'news_{news_id}_liked_by', user_id)

    elif comment_id is not None:
        return r.sismember(f'comments_{comment_id}_liked_by', user_id)
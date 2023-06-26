import pytest

from backend.src.users.models import User
from backend.src.news_server.models import News, Comments


@pytest.fixture
def user():
    return User.objects.create(username='test_user', password='password123')


@pytest.fixture
def news(user):
    return News.objects.create(title='Test Title', text='Test Text', author=user)


@pytest.fixture
def comment(user, news):
    return Comments.objects.create(text='Test Comment', author=user, news=news)


def test_news_str(news):
    assert str(news) == str(news.author)


def test_comments_str(comment):
    assert str(comment) == str(comment.author)


def test_news_creation(news, user):
    assert isinstance(news, News)
    assert news.title == 'Test Title'
    assert news.text == 'Test Text'
    assert news.author == user


def test_comments_creation(comment, user, news):
    assert isinstance(comment, Comments)
    assert comment.text == 'Test Comment'
    assert comment.author == user
    assert comment.news == news

from django.db import migrations
import json


def add_news_and_comments(apps, schema_editor):
    News = apps.get_model('news_server', 'News')
    User = apps.get_model('users', 'User')
    Comments = apps.get_model('news_server', 'Comments')
    with open('static/json_dam_news.json') as json_file:
        data = json.load(json_file)
        for item in data['results']:
            try:
                author = User.objects.get(username=item['author'])
            except User.DoesNotExist:
                username = item['author']
                email = f'{username}@example.com'
                author = User.objects.create_user(
                    username=username,
                    email=email,
                    password='default_password')
            news_item = News(
                id=item['id'],
                date=item['date'],
                title=item['title'],
                text=item['text'],
                author=author
            )
            news_item.save()

            for comment in item['comments']:
                try:
                    comment_author = User.objects.get(
                        username=comment['author'],
                        email__isnull=False)
                except User.DoesNotExist:
                    username = comment['author']
                    email = f'{username}@example.com'
                    comment_author = User.objects.create_user(
                        username=username,
                        email=email,
                        password='default_password')
                comment_item = Comments(
                    id=comment['id'],
                    date=comment['date'],
                    text=comment['text'],
                    author=comment_author,
                    news=news_item
                )
                comment_item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('news_server', '0001_initial'),
        ('users', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_news_and_comments),
    ]

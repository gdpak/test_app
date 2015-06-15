from re          import sub
from django.conf import settings


def add_avatar_to_session(backend, user, response, *args, **kwargs):
    avatar_url   = settings.DEFAULT_AVATAR_URL
    avatar_image = response.get('image')

    if avatar_image:
        avatar_url = avatar_image.get('url', avatar_url)
        avatar_url = sub('\d+$', settings.AVATAR_SIZE, avatar_url)

    backend.strategy.session['avatar_url'] = avatar_url
    backend.strategy.session.save()

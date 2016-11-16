from django.conf import settings
from django.contrib.sites.models import Site

current_site = Site.objects.get_current()


class Meta(type):
    def __init__(cls, *args, **kwargs):
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Meta, cls).__call__(*args, **kwargs)
        return cls.instance


class Settings(object):
    """Django Evercookie Settings Interface."""

    __metaclass__ = Meta

    def __init__(
        self,
        etag_cookie_name=settings.EVERCOOKIE_ETAG_COOKIE_NAME or 'etg',
        etag_path=settings.EVERCOOKIE_ETAG_PATH or 'ecetag',
        png_cookie_name=settings.EVERCOOKIE_PNG_COOKIE_NAME or 'png',
        png_path=settings.EVERCOOKIE_PNG_PATH or 'epng',
        cache_cookie_name=settings.EVERCOOKIE_CACHE_COOKIE_NAME or 'cachec',
        cache_path=settings.EVERCOOKIE_CACHE_PATH or 'ecache',
        history=settings.EVERCOOKIE_HISTORY or 'false',
        java=settings.EVERCOOKIE_JAVA or 'false',
        silverlight=settings.EVERCOOKIE_SILVERLIGHT or 'false',
        domain=settings.EVERCOOKIE_DOMAIN or '.'+current_site.domain,
        tests=settings.EVERCOOKIE_TESTS or 10,
        base_url=settings.EVERCOOKIE_BASE_URL or '',
        auth_path=settings.EVERCOOKIE_AUTH_PATH or 'false',
        static_url=settings.EVERCOOKIE_STATIC_URL or (settings.STATIC_URL + 'django_evercookie/'),
        cookie_value=settings.EVERCOOKIE_COOKIE_VALUE or ''
    ):

        self.etag_cookie_name = etag_cookie_name
        self.etag_path = etag_path
        self.png_cookie_name = png_cookie_name
        self.png_path = png_path
        self.cache_cookie_name = cache_cookie_name
        self.cache_path = cache_path
        """  CSS history knocking or not .. can be network intensive """
        self.history = history
        """ Java applet on/off"""
        self.java = java
        """ Silverlight support """
        self.silverlight = silverlight
        self.domain = domain
        """ Max tries to wait / write / read swf, silverlight, png, db and java"""
        self.tests = tests
        """ Base URL for assets, this is Django's STATIC_URL """
        self.base_url = base_url
        self.auth_path = auth_path
        self.static_url = static_url
        self.cookie_value = cookie_value


settings = Settings()

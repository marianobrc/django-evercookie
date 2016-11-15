try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

"""URLs differ from standart evercookie_<storage_method> to dodge easyprivacy blocking rules"""


urlpatterns = [
    url(r'^ecache', 'evercookie_cache', name='ecache'),
    url(r'^epng', 'evercookie_png', name='epng'),
    url(r'^ecetag', 'evercookie_etag', name='ecetag'),
    url(r'^ecookie', 'evercookie_core', name='ecookie'),
    url(r'^ecauth', 'evercookie_auth', name='ecauth'), )
]

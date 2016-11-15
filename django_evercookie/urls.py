"""URLs differ from standart evercookie_<storage_method> to dodge easyprivacy blocking rules."""

from django.conf.urls import \
    url
from django_evercookie.views import (
    evercookie_cache,
    evercookie_png,
    evercookie_etag,
    evercookie_core,
    evercookie_auth
)


urlpatterns = [
    url(r'^ecache', evercookie_cache, name='ecache'),
    url(r'^epng', evercookie_png, name='epng'),
    url(r'^ecetag', evercookie_etag, name='ecetag'),
    url(r'^ecookie', evercookie_core, name='ecookie'),
    url(r'^ecauth', evercookie_auth, name='ecauth'),
]

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from oscar.app import shop

# These simply need to be imported into this namespace.  Ignore the PEP8
# warning that they aren't used.
from oscar.views import handler500, handler404, handler403

admin.autodiscover()

urlpatterns = patterns('',
    # Include admin as convenience. It's unsupported and you should
    # use the dashboard
    (r'^admin/', include(admin.site.urls)),
    # Custom functionality to allow dashboard users to be created
    (r'', include(shop.urls)),
)

#static pages
urlpatterns += patterns('django.contrib.flatpages.views',
	url(r'^contacts/$', 'flatpage', {'url': '/contacts/'}, name='contacts'),
	url(r'^delivery/$', 'flatpage', {'url': '/delivery/'}, name='delivery'),
	url(r'^faq/$', 'flatpage', {'url': '/faq/'}, name='faq'),
)

# Allow rosetta to be used to add translations
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^rosetta/', include('rosetta.urls')),
    )

if settings.DEBUG:
    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += patterns('',
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500)
    )

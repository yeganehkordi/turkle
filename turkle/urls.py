from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from hits.admin import admin_site
import hits.views
from turkle.settings import TURKLE_EMAIL_ENABLED


admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', hits.views.index, name='index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^hits/', include('hits.urls')),

    url(r'^admin/', admin_site.urls),

    url(r'^login/$',
        auth_views.LoginView.as_view(
            extra_context={'TURKLE_EMAIL_ENABLED': TURKLE_EMAIL_ENABLED}
        ),
        name="login"),
    url(r'^', include('django.contrib.auth.urls')),
]

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from bookings.views import CreateBookingView, BookingListViewCustomer, AllBookingListViewForProvider
from providers.views import ProviderServiceFilterView, ProviderListView, ProviderCreateView, ProviderUpdateView, \
    ProviderServiceListView, ProviderServiceCreateView, ProviderServiceUpdateView, ProviderServiceDeleteView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^search/$', ProviderServiceFilterView.as_view(), name='search'),
    url(r'^providers/(?P<pk>\d+)/services/$', ProviderServiceListView.as_view(), name='providerservice-list'),
    url(r'^providers/(?P<pk>\d+)/services/create/$', ProviderServiceCreateView.as_view(), name='providerservice-create'),
    url(r'^providers/(?P<provider_pk>\d+)/services/(?P<pk>\d+)/update/$', ProviderServiceUpdateView.as_view(), name='providerservice-update'),
    url(r'^providers/(?P<provider_pk>\d+)/services/(?P<pk>\d+)/delete/$', ProviderServiceDeleteView.as_view(), name='providerservice-delete'),

    url(r'^bookings/$', BookingListViewCustomer.as_view(), name='booking-list'),
    url(r'^providers/(?P<pk>\d+)/bookings/$', AllBookingListViewForProvider.as_view(), name='booking-list-provider'),
    url(r'^book/(?P<pk>\d+)/$', CreateBookingView.as_view(), name='booking-create'),

    url(r'^providers/$', ProviderListView.as_view(), name='provider-list-user'),
    # url(r'^providers/(?P<pk>\d+)/$', ProviderDetailView.as_view(), name='provider-detail'),
    url(r'^providers/create/$', ProviderCreateView.as_view(), name='provider-create'),
    url(r'^providers/(?P<pk>\d+)/update/$', ProviderUpdateView.as_view(), name='provider-update'),

    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('bookit.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

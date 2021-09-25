from django.conf.urls import url
from .views import user as user_views
from .views import company as comp_views
from .views import auth as auth_views
from .views import admin as admin_view
from .views import voucher as voucher_view


urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^choice/', admin_view.choice_view, name='choice'),

    url(r'^vouchers/', voucher_view.voucher_list, name='voucher_list'),
    url(r'^voucher/new/$', voucher_view.voucher_new, name='voucher_new'),
    url(r'^voucher/(?P<pk>[0-9]+)/$', voucher_view.voucher_details, name='voucher_details'),
    url(r'^voucher/(?P<pk>[0-9]+)/edit/$', voucher_view.voucher_edit, name='voucher_edit'),
    url(r'^voucher/(?P<pk>[0-9]+)/delete/$', voucher_view.voucher_delete, name='voucher_delete'),
    url(r'^sorted_list/$', voucher_view.voucher_sorted_list, name='voucher_sorted_list'),
    url(r'^download_voucher_list/$', voucher_view.download_voucher_list, name='download_voucher_list'),

    url(r'^companies/', comp_views.company_list, name='company_list'),
    url(r'^company/(?P<pk>[0-9]+)/$', comp_views.company_details, name='company_details'),
    url(r'^company/new/$', comp_views.company_new, name='company_new'),
    url(r'^company/(?P<pk>[0-9]+)/edit/$', comp_views.company_edit, name='company_edit'),
    url(r'^company/(?P<pk>[0-9]+)/delete/$', comp_views.company_delete, name='company_delete'),
    url(r'^download_company_list/$', comp_views.download_company_list, name='download_company_list'),

    url(r'^users/', user_views.user_list, name='user_list'),
    url(r'^user/(?P<pk>[0-9]+)/$', user_views.user_details, name='user_details'),
    url(r'^user/new/$', user_views.user_new, name='user_new'),
    url(r'^user/(?P<pk>[0-9]+)/edit/$', user_views.user_edit, name='user_edit'),
    url(r'^user/(?P<pk>[0-9]+)/delete/$', user_views.user_delete, name='user_delete'),
]

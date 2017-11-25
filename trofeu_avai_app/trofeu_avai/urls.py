# -*- coding: utf-8 -*-

from django.conf.urls import url
# from django.contrib.auth.views import logout

from trofeu_avai.views import inicial  # , login_user, faturas, change_password

urlpatterns = [
    # url(r'^entrar/$', login_user.as_view(), name='entrar'),
    # url(r'^sair/$', logout, {'next_page': '/entrar/'}, name='sair'),
    # url(r'^senha/$', change_password.as_view(), name='change_password'),
    url(r'^$', inicial.as_view(), name='inicial'),
]

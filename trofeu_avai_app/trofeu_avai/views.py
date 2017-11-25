# coding: utf-8

from django.views import View
from django.shortcuts import render


class inicial(View):
    """
    HOME
    """

    def get(self, request):
        return render(request, 'inicial.html', {})

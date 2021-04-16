# -*- coding: utf-8 -*-
"""
create on 2021-04-16 10:57 上午

author @guorui
"""
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):

    def get(self, request):
        print('welcome to my world')
        return Response(data={'st': 1})

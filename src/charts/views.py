# from django.contrib.auth import get_user_model
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.generic import View

# from rest_framework.views import APIView
# from rest_framework.response import Response


# User = get_user_model()


# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         qs_count = User.objects.all().count()
#         labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
#         default_items = [qs_count, 23, 2, 3, 12, 2]
#         data = {
#                 "labels": labels,
#                 "default": default_items,
#         }
#         return Response(data)


from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, "charts.html", {"customers": 10}
        )  # first way of doing it


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)  # second way of doing it


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # usernames = [user.username for user in User.objects.all()]
        data = {
            "sales": 100,
            "customers": 10,
        }
        return Response(data)  # third way of doing it

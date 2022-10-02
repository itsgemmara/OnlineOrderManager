# from rest_framework.response import Response
# from rest_framework import viewsets
# from rest_framework.decorators import action
#
# from .serializers import *
# from .filters import *
#
#
# class FilterApiView(viewsets.GenericViewSet):
#
#     serializer_class = TextSearchFilterSerializer
#
#     @action(detail=False, methods=['post', ])
#     def char_search_filter(self, r, name):
#         response = char_field_search_filter(self.request.data, )
#         return Response(response.name_search_filter(), status=200)
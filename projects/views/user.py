from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import action

from projects.serializers import UserListSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from projects.models import User, Task

class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(deleted_at=None)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserDetailSerializer

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.deleted_at = now()
        user.save()
        return Response({'detail': 'User has been deleted'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get', 'patch'])
    def deactivate(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.is_active:
            obj.is_active = False
            obj.save()
            serializer = self.get_serializer(obj)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data="User is already inactive", status=status.HTTP_400_BAD_REQUEST)

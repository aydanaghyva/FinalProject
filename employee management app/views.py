from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Department, Position, Employee
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer
from .permissions import IsAdminRole

def home(request):
    return HttpResponse("Welcome to the home page!")

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data.get("username")).first()
        if user and user.check_password(request.data.get("password")):
            tokens = get_tokens_for_user(user)
            return Response(tokens)
        return Response({"error": "Invalid credentials"}, status=400)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_permissions(self):
        # Apply IsAdminRole permission only for DELETE requests
        if self.action == 'destroy':  # 'destroy' is the action for delete in viewsets
            self.permission_classes = [IsAuthenticated, IsAdminRole]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_permissions(self):
        # Apply IsAdminRole permission only for DELETE requests
        if self.action == 'destroy':  # 'destroy' is the action for delete in viewsets
            self.permission_classes = [IsAuthenticated, IsAdminRole]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_permissions(self):
        # Apply IsAdminRole permission only for DELETE requests
        if self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsAdminRole]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
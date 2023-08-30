from .models import Account
from .serializers import AccoutSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from drf_spectacular.utils import extend_schema


class LoginView(TokenObtainPairView):
    pass


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccoutSerializer

    @extend_schema(
        operation_id="user_create",
        summary="create users",
        description="route to create all users",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

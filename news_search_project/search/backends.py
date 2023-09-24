from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

class CustomUserModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) and not user.is_blocked:
                return user
            elif user.is_blocked:
                messages.warning(request, "User is been blocked by admin")
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CaseInsensitiveModelBackend(ModelBackend):
    """
    Custom authentication backend that performs case-insensitive username lookup.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is not None:
            try:
                # Perform a case-insensitive query
                user = UserModel.objects.get(username__iexact=username)
            except UserModel.DoesNotExist:
                return None
            else:
                # Check the password as usual
                if user.check_password(password):
                    return user
        return None

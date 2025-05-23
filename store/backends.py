from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(ModelBackend):
    """
    Custom authentication backend to allow users to log in by email instead of username.
    """

    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        print(">>> EmailBackend.authenticate called with:", "username=", username, "email=", email)
        lookup_email = email or username
        if lookup_email is None or password is None:
            return None

        # Look up the user by email
        try:
            user = User.objects.get(email=lookup_email)
            # check given plain-text password
        except User.DoesNotExist:
            # return None to signal "no such user"
            return None

        if user.check_password(password):
            return user
        return None
    
    
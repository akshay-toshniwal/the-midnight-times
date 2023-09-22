from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form.

    This form extends Django's UserCreationForm to customize the user creation process.
    It allows registration with a username and 
    any additional custom fields defined in the CustomUser model.

    Attributes:
        model (type): The custom user model associated with this form.
        fields (tuple): The fields to display in the form.
    """

    class Meta:
        model = CustomUser
        fields = ("username",)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUserCreationForm.Meta.fields + ("age",)

        fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm()):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

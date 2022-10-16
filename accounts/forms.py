from django.contrib.auth.forms import UserCreationForm
from accounts.models import CostumUser


class CostumUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CostumUser
        fields=['username','last_name','first_name','email','age','male','image']
class CostumUserChangeForm(UserCreationForm):
    class Meta:
        model=CostumUser
        fields=['username','last_name','first_name','email','age','male','image']
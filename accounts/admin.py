from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser
from .forms import CustomeUserChangeForm,CustomeUserCreationForm

@admin.register(CustomUser)
class CustomeUserAdmin(UserAdmin):
    model = CustomUser 
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    list_display = ('email','username')
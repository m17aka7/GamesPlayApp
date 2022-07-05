from django import forms

from GamesPlayApp.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'email': 'Email:',
            'age': 'Age:',
            'password': 'Password:',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'email': 'Email:',
            'age': 'Age:',
            'password': 'Password:',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Game.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = "__all__"

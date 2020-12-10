from django import forms 


class login(forms.Form):
    email=forms.EmailField(help_text='enter your email here')
    password=forms.CharField(widget=forms.PasswordInput)
    renter=forms.CharField(help_text="renter password",widget=forms.PasswordInput)
    role=forms.CharField(widget=forms.TextInput)

    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)<4:
            raise forms.ValidationError('password is too short')
        return password
    def con_database(self):
        pass
        

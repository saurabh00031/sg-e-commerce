from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Blog_Post, Mentorinfo,User,Usrinfo
from .models import Comment
from django.forms import ModelForm
########from .models import Comment##########################################################################################################



class CommentForm(forms.ModelForm):
    commenter = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'username'
    }))
    body = forms.CharField(max_length=100, widget = forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Comment here', 'rows': 3
    }))
    class Meta:
        model = Comment
        fields = ['commenter', 'body']




class BlogForm(forms.ModelForm): 
    class Meta:
        model = Blog_Post
        fields = ['id','image','title','body','slug'] 

        
        



class MentorReg(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta(UserCreationForm):
        model = User
        fields = ['id','email','username']

    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_mentor = True
        user.save()
        crt = Mentorinfo.objects.create(user=user)
        return user


class UsrReg(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta(UserCreationForm):
        model  = User
        fields = ['id','email','username']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_user = True
        user.save()
        usr = Usrinfo.objects.create(user=user)
        return user        



class MentorinfoForm(forms.ModelForm):
    full_Name=forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    image=forms.ImageField(label='Profile Image', required=False)
   
    class Meta:
        model = Mentorinfo
        fields = ['full_Name', 'address','phone','country' ,'states','image','email','git_hub','insta_link','linked_in','city','field_of_interest','total_earnings_by','company_name','experience_yrs','description_in_short','future_goals']
        widgets={
            'full_Name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'full_Name':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'field_of_interest':forms.TextInput(attrs={'class':'form-control'}),
            'git_hub':forms.TextInput(attrs={'class':'form-control'}),
            'insta_link':forms.TextInput(attrs={'class':'form-control'}),
            'linked_in':forms.TextInput(attrs={'class':'form-control'}),
            'total_earnings_by':forms.TextInput(attrs={'class':'form-control'}),
            'company_name':forms.TextInput(attrs={'class':'form-control'}),
            'experience_yrs':forms.TextInput(attrs={'class':'form-control'}),
            'description_in_short':forms.TextInput(attrs={'class':'form-control'}),
            'future_goals':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'states':forms.TextInput(attrs={'class':'form-control'}),
        }





##################################################################################################################
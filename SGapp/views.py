
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from SGapp.decorators import user_required,mentor_required
from .models import User as mu,Usrinfo,Mentorinfo, government_Notificationsinfo
from .forms import BlogForm, UsrReg,MentorReg,MentorinfoForm
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog_Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

@user_required
def index(request):
    posts = Blog_Post.objects.all()
    return render(request, 'index.html', {'posts': posts})



@user_required
def blog_detailView(request, slug):
    post = Blog_Post.objects.get(slug = slug)
    comments = post.comments.all()
    new_comment = None
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'User commented successfully!')
            return HttpResponseRedirect(reverse('blog_detail', args = [str(post.slug)]))
            
    else:
        form = CommentForm()
    return render(request, 'blog_detail.html', {'post': post, 'form': form, 'comments':comments, 'new_comment':new_comment})





def indox(request):
    return render(request, 'indox.html')



def about_Pro(request):
    return render(request,'aboutPro.html')



def about_Us(request):
    return render(request,'aboutUS.html')



def services(request):
    return render(request,'servicesPage.html')



class UsrView(CreateView):
    model = User
    form_class = UsrReg
    template_name = 'reg_user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User has been created successfully!')
        login(self.request, user)
        return redirect("sgin_user")




class MentorView(CreateView):
    model = User
    form_class = MentorReg
    template_name = 'reg_mentor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'mentor'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User has been created successfully!')
        login(self.request, user)
        return redirect("sgin_mentor")




def sgin_user(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_user == True:
                login(request, user)
                return redirect("sginpg_user")
            else:
                messages.error(
                    request, 'You are not authorized to access this page!')
        else:
            messages.error(request, 'Invalid Credentials!,plz try again')
            return render(request, 'sgin_user.html')
    return render(request, 'sgin_user.html')



def sgin_mentor(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_mentor == True:
                login(request, user)
                return redirect("sgin_pg_shift")
            else:
                messages.error(
                    request, 'You are not authorized to access this page!')
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid Credentials!,plz try again')
            return render(request, 'sgin_mentor.html')
    return render(request, 'sgin_mentor.html')




@user_required
def sginpg_user(request):
    obj=Mentorinfo.objects.all()
    Mentor_data={
        "obj_ment":obj,
    }
    return render(request,'sginpg_user.html',Mentor_data)




@mentor_required
def shift(request):
    return render(request,'sgin_pg_shift.html')

def sginpg_mentor(request):
    this_usr = request.user
    usr_inf = Mentorinfo.objects.get(user = request.user)
    if request.method == "POST":
        full_Name = request.POST.get('full_Name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        git_hub = request.POST.get('git_hub')
        insta_link = request.POST.get('insta_link')
        linked_in= request.POST.get('linked_in')
        city = request.POST.get('city')
        address = request.POST.get('address')
        states = request.POST.get('states')
        country = request.POST.get('country')
        field_of_interest = request.POST.get('field_of_interest')
        total_earnings_by = request.POST.get('total_earnings_by')
        company_name = request.POST.get('company_name')
        future_goals = request.POST.get('city')
        experience_yrs = request.POST.get('experience_yrs')
        description_in_short=request.POST.get('description_in_short')



        if len(request.FILES) != 0:
            usr_inf.image = request.FILES['img']

        usr_inf.full_Name = full_Name
        usr_inf.country=country
        usr_inf.states=states
        usr_inf.address=address
        usr_inf.phone = phone
        usr_inf.git_hub =git_hub
        usr_inf.insta_link = insta_link
        usr_inf.linked_in= linked_in
        usr_inf.city = city
        usr_inf.field_of_interest = field_of_interest
        usr_inf.total_earnings_by = total_earnings_by
        usr_inf.company_name = company_name
        usr_inf.future_goals = future_goals
        usr_inf.experience_yrs = experience_yrs
        usr_inf.description_in_short=description_in_short
        usr_inf.save()
        this_usr.email = email
        this_usr.save()
        messages.success(request, 'Data Updated Successfully!') 
        
    usr_dat = {
        "usr_info" : usr_inf,
        "my_usr_inf" : this_usr
    }
    return render(request, 'sginpg_mentor.html', usr_dat)



def logout_x(request):
       logout(request)
       return redirect('/')




@mentor_required
def profile_x(request):
     sorrows=Mentorinfo.objects.get(user=request.user.id)
     sp={
         "sorrows":sorrows,
     }
     return render(request,'profile_x.html',sp)





@user_required
def search(request):
    qur = request.GET.get('search')
    ct = Mentorinfo.objects.filter(city__contains=qur)
    return render(request, 'search1.html', {'ct': ct})





@user_required
def search2(request):
    qur = request.GET.get('search')
    ctx = Mentorinfo.objects.filter(field_of_interest__contains=qur,city__contains=qur)
    return render(request, 'search2.html', {'ctx': ctx})





@user_required
def gov_nov_x(request):
    ssp=government_Notificationsinfo.objects.all()
    hang_sp={
        'ssp':ssp,
    }
    return render(request,'notify.html',hang_sp)




@user_required
def request_mentor(request,id):
        fname = request.user
        usr_eml = request.user.email
        king = Mentorinfo.objects.get(pk=id)
        phone=king.phone
        em=king.email
        message=king.description_in_short
        send_mail(fname,
                  "User Phone:-  "+phone+"\n"+"User Email:- "+usr_eml+"\n"+message+"\n"+"\n"+"Request for Mentorship",
                  em,
                  ['ss.blognchat@gmail.com'],
                  fail_silently=True)
        messages.success(
            request, 'You have successfully requested for Mentorship !!')
        return render(request, 'sginpg_user.html')



@user_required
def addPost(request):
    if request.method=='POST':
        title=request.POST.get('title')
        slug=request.POST.get('slug')
        body=request.POST.get('body')
        image=request.FILES['image']
        blog=Blog_Post(title=title,slug=slug,body=body,writer=request.user,image=image)
        blog.save()
        messages.success(request,"post has been updates successfully")
        return redirect('addPost')
    return render(request,'addPost.html')

        
@user_required
def my_posts(request):
     if request.user.is_authenticated:
        blog_data = Blog_Post.objects.filter(writer=request.user.id)
        return render(request , 'blog_data.html' , {'blog_data' : blog_data})
    


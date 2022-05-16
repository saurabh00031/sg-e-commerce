from django.contrib import admin
from .models import User,Usrinfo,Mentorinfo,government_Notificationsinfo
from .models import Blog_Post, Comment

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
 
admin.site.register(Blog_Post, BlogPostAdmin)
admin.site.register(Comment)


admin.site.register(User)
#admin.site.register(government_Notificationsinfo)

@admin.register(Usrinfo)
class UsrDisp(admin.ModelAdmin):
    list_display = ('id','full_Name','phone','email','git_hub','insta_link','linked_in','city','address','field_of_interest','total_earnings_by')

@admin.register(Mentorinfo)
class MentortDisp(admin.ModelAdmin):
    list_display = ('id','image','full_Name','phone','email','git_hub','insta_link','linked_in','city','address','field_of_interest','total_earnings_by','company_name','experience_yrs','description_in_short','future_goals')



@admin.register(government_Notificationsinfo)
class governNotifyDisp(admin.ModelAdmin):
     list_display = ('id','notify_title','notify_body','notify_by_whom','notify_dates')


from django.contrib import admin
from .models import Post , Category , AboutUs


#this is for which contect are uoy want in admin panel  
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    #you can add search option also 
    search_fields = ('title', 'content' )
    #can add also filter option also 
    list_filter = ('category','created_at')




# Register your models here.
admin.site.register(Post,PostAdmin) # add that class name in the (PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
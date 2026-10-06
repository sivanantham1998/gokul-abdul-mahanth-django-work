from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home,footer,users,contact,product_create,stu_create,student_list,stu_delete,update_data,file_upload,set_session,get_session,delete_session,set_cookie,get_cookie,delete_cookie
urlpatterns =[
    path("",home),
    path("footer-page/",footer,name="footer"),
    path("user/",users,name="user"),
    path("contact/",contact,name="contact"),
    path("product/",product_create,name="product"),
    path("stu/",stu_create,name="stu"),
    path("list/",student_list,name="list"),
    path("delete/<int:id>",stu_delete,name='delete_stu'),
    path("edit/<int:id>",update_data,name="edit_stu"),
    path("upload/",file_upload,name="file_upload"),
    path("session/set/",set_session),
    path("session/get/",get_session),
    path("session/delete/",delete_session),
    path("cookie/delete/",delete_cookie),
    path("cookie/set/",set_cookie),
    path("cookie/get/",get_cookie),



]

urlpatterns+=static(
    settings.MEDIA_URL,
    documents_root=settings.MEDIA_ROOT
)
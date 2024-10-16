from django.urls import path

from django.urls.conf import include

from accounts import views


urlpatterns=[
    path('account',views.account),
    path('show',views.show),
    # path('edit',views.edit),
    # path('update',views.update),
    # path('dlt',views.dlt),
    path('edit/<int:id>/', views.edit, name='edit'),  
    path('update/<int:id>/', views.update, name='update'),  
    path('dlt/<int:id>/', views.dlt, name='delete'),
]
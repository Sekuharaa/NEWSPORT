from django.urls import path
from .views import (PostList, PostDetail, NewsSearch, PostCreate, PostUpdate, PostDelete, IndexView, CategoryListView, subscribe
                    )
from allauth.account.views import LogoutView, LoginView
from .views import upgrade_me

urlpatterns = [

   path('', PostList.as_view(), name='posts'),
   path('<int:pk>/', PostDetail.as_view(),name='post'),
   path('search', NewsSearch.as_view(), name='search'),
   path('news/create/', PostCreate.as_view(), name='create'),
   path('news/<int:pk>/edit', PostUpdate.as_view(), name='edit'),
   path('news/<int:pk>/delete', PostDelete.as_view(), name='delete'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit', PostUpdate.as_view(), name='articles_edit'),
   path('articles/<int:pk>/delete', PostDelete.as_view(), name='articles_delete'),
   path('profile/', IndexView.as_view(), name='profile'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('signup/', IndexView.as_view(template_name='signup.html'), name='signup'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
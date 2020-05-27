from django.urls import path

from .views import ArticlesHome,ArticleDetail,ArticleUpdate,ArticleDelete,ArticleCreate
from .views import ArticleWarn

app_name = "article"

urlpatterns = [
    path("",ArticlesHome.as_view(), name = "home"),
    path("<int:pk>/",ArticleDetail.as_view(), name="detail"),
    path("new_article/",ArticleCreate.as_view(), name="new_article"),
    path("<int:pk>/update/",ArticleUpdate.as_view(), name="update"),
    path("<int:pk>/delete/",ArticleDelete.as_view(), name="delete"),
    path("unautherised_permission/",ArticleWarn.as_view(), name="warn")
]

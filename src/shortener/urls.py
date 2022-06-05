from django.urls import path


from .views import ResolverView, ShortenerView


urlpatterns = [
    path('', ShortenerView.as_view()),
    path('<str:alias>', ResolverView.as_view()),
]

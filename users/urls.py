from django.urls import include, path
from users.views import CustomRegistrationView


create = CustomRegistrationView.as_view({
    'post': 'create',
   })

urlpatterns = [
    path('clients/create', create, name='create'),
    path('auth/', include('djoser.urls.jwt'))

]

from django.urls import include, path
from users.views import CustomRegistrationView, UserSet

create = CustomRegistrationView.as_view({
    'post': 'create',
})

match = CustomRegistrationView.as_view({
    'post': 'match',
})

urlpatterns = [
    path('list', UserSet.as_view(), name='list'),
    path('clients/create', create, name='create'),
    path('clients/<int:id>/match', match, name='match'),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
]

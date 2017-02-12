from django.conf.urls import url
from .views import AuthView, CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    url(r'^$', AuthView.as_view(), name='authorization_page'),

    url(r'^message/', CommentListView.as_view(), name='message_page'),

    url(r'^add_comment/(?P<pk>[0-9]+)/$', CommentCreateView.as_view(),
        name='add_comment'),

    url(r'^edit_comment/(?P<pk>[0-9]+)/$', CommentUpdateView.as_view(),
        name='edit_comment'),

    url(r'^del_comment/(?P<pk>[0-9]+)/$', CommentDeleteView.as_view(),
        name='del_comment'),
]

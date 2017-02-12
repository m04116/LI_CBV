from django.shortcuts import get_object_or_404, redirect, render
from . models import Comment
from .forms import CommentForm
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from django.views.generic.edit import DeleteView, FormMixin
from django.urls import reverse_lazy


class AuthView(TemplateView):

    def get(self, request):
        if self.request.user.is_authenticated():
            return redirect('message_page')
        return render(request, 'blog/authorization_page.html')


class CommentListView(FormMixin, ListView):

    template_name = 'blog/message_page.html'
    queryset = Comment.objects.all()
    context_object_name = 'nodes'

    form_class = CommentForm

    def get_success_url(self):
        return reverse('message_page')

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST or None)
        form = self.get_form()
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.published_date = timezone.now()
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def get_success_url(self):
        return reverse('message_page')

    def post(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.parent = get_object_or_404(Comment, pk=pk)
            form.post = comment
            form.published_date = timezone.now()
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit.html'

    def get_success_url(self):
        return reverse('message_page')

    def post(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('message_page')

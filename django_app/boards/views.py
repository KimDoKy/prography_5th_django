from django.views import generic
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post, Comment


class PostList(generic.ListView):
    model = Post


class PostDetail(generic.DetailView):
    model = Post


class PostNew(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields= ['title','content', 'photo']

    def form_valid(self, form):
        print(self.request.user)
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEdit(generic.UpdateView):
    model=Post
    fields='__all__'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("작성자가 아닙니다.")
        return super(PostEdit, self).dispatch(request, *args, **kwargs)


class PostDelete(generic.DeleteView):
    model = Post
    success_url=reverse_lazy('boards:post_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("작성자가 아닙니다.")
        return super(PostDelete, self).dispatch(request, *args, **kwargs)

def comment_create(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get('content')

        if not content:
            return HttpResponse('댓글을 입력하세요.', status=400)

        Comment.objects.create(
                post = post,
                author = request.user,
                message = content
                )
    return redirect('boards:post_list')

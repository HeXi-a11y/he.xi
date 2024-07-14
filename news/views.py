from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/post_details.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/newpost.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    succes_url = ''
    template_name = 'news/delete.html'

def news_main(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/news_main.html', {'news': news})

def newpost(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка!'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/newpost.html', data)


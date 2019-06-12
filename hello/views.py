from django.http import HttpResponse

def hello(req):
  return HttpResponse('Hello, World !!')

def hello_html(req):
    src = []
    src.append('<!doctype html>')
    src.append('<html>')
    src.append('<head>')
    src.append('<meta charset="utf-8">')
    src.append('<title>Hello, World</title>')
    src.append('</head>')
    src.append('<body>')
    src.append('<h1 style="color:#F4A346;">Hello, World!!</h1>')
    src.append('</body>')
    src.append('</html>')
    return HttpResponse('\n'.join(src))
    
from django.shortcuts import render
from django.views.generic import TemplateView

class HelloTemplateView(TemplateView):
    template_name = 'hello.html'    
    def get(self, request, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from .forms import *
from django.views.generic import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.functional import cached_property
from rest_framework import generics, permissions, viewsets
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, detail_route

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def main(request):
	args = {}
	args.update(csrf(request))
	args['term'] = auth.get_user(request).term
	if request.method == 'POST':
	    a = User.objects.get(pk = 1)
	    form = UserProfile(request.POST or None, instance = a)
	    if form.is_valid():
	        args['term'] = auth.get_user(request).term
	        term = auth.get_user(request).term
	        term += 1
	        form.save()
	        return redirect ('/base/main.html')
	    else:
	        args['form'] = form
	return render_to_response('base/main.html', RequestContext(request, args))


class company (TemplateView, LoginRequiredMixin):
    template_name = 'base/company.html'

    def view(self, request):
        return render_to_response(template_name, context_instance=RequestContext(request))


class product (TemplateView, LoginRequiredMixin):
    template_name = 'base/product.html'

    def view(self, request):
        return render_to_response(template_name, context_instance=RequestContext(request))

class finance (TemplateView, LoginRequiredMixin):
    template_name = 'base/finance.html'
    form_class = DataforInvestorForm

    def get(self, request, *args, **kwargs):
        c = {}
        form = self.form_class
        c['form'] = form
        return render (request, self.template_name, c)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(user=self.request.user)
            return HttpResponseRedirect('finance.html')
        return render(request, self.template_name, {'form': form})

    def view(self, request):
        return render_to_response(self.template_name, context_instance=RequestContext(request))

class marketing (TemplateView, LoginRequiredMixin):
    template_name = 'base/marketing.html'

    def view(self, request):
        return render_to_response(template_name, context_instance=RequestContext(request))


class hr (TemplateView, LoginRequiredMixin):
    template_name = 'base/hr.html'

    def view(self, request):
        return render_to_response(template_name, context_instance=RequestContext(request))

class production(TemplateView, LoginRequiredMixin):
    template_name = 'base/production.html'

    def view(self, request):
        return render_to_response(template_name, context_instance=RequestContext(request))


class BusinessProjectSet(viewsets.ModelViewSet):
    queryset = BusinessProject.objects.all()
    serializer_class = BusinessProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return BusinessProject.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'BusinessProject': reverse('BusinessProject-list', request=request, format=format)
    })

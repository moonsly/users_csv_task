# -*- coding: utf-8 -*-
import time
import models

from django.views.generic import ListView, DetailView, UpdateView, CreateView, RedirectView
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import loader
from django.http import HttpResponse

from exos_task.models import MyUser
from exos_task.forms import SaveUserForm


class UserDetailView(DetailView):

    model = models.MyUser
    template_name = "user_details.html"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        return context


class UserListView(ListView):

    model = models.MyUser
    template_name = "user_list.html"
    context_object_name = "user_list"
    paginate_by = 50

    def render_to_response(self, context, **response_kwargs):
        """
        Creates a CSV response if requested, otherwise returns the default template response.
        """
        if 'csv' in self.request.GET.get('export', ''):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="users_{}.csv"'.format(time.time())

            content = loader.render_to_string("export_csv.html", context)

            response.write(content)
            return response
        # Business as usual otherwise
        else:
            return super(UserListView, self).render_to_response(context, **response_kwargs)    


class UserDeleteView(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = get_object_or_404(MyUser, pk=kwargs['pk'])
        user_id = user.id
        user.delete()

        URL = reverse('users-list') + '?deleted={}'.format(user_id)
        return URL


class UserCreateView(CreateView):

    model = MyUser
    fields = ['username', 'email', 'birthday', 'random_number',]
    template_name = 'user_edit.html'

    def get_success_url(self):
        URL = "{}?created=1".format(reverse('user-edit', args=(self.object.id,)))
        return URL

    def form_valid(self, form):
        form.save()
        return super(UserCreateView, self).form_valid(form)


class UserSaveView(UpdateView):

    template_name = 'user_edit.html'
    form_class = SaveUserForm
    model = MyUser

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        if kwargs.get("pk"):
            form = self.form_class(instance=MyUser.objects.get(pk=kwargs["pk"]))

        context = {"form": form}
        if request.GET.get("created"):
            context["created"] = 1
        return render(request, self.template_name, context)

    def form_valid(self, form):
        obj = form.save(commit=False)
        # extra actions
        obj.save()
        context = {"form": form, "saved": True}

        return render(self.request, self.template_name, context)

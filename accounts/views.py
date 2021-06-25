from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import redirect, reverse
from .forms import UserRegistrationForm


class RegistrationView(FormView):
    template_name = "registration/register.html"
    form_class = UserRegistrationForm

    def form_valid(self, form):
        cd = form.cleaned_data
        new_user = form.save(commit=False)
        new_user.set_password(cd["password"])
        new_user.save()
        login(self.request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        try:
            cd['next'] = dict(form.data)["next"][0]
        except (IndexError, KeyError):
            pass
        if cd.get("next"):
            return redirect(cd.get("next"))
        return redirect(reverse_lazy("create_link"))




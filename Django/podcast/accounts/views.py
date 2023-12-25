from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# these two package is for register function
from django.views import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.auth.views import LoginView


class PodcastLoginView(LoginView):
    template_name = "accounts/login.html"

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return redirect("home")
        else:
            return self.form_invalid(form)


# import this function in urls.py to implement function
def logout_view(request):
    logout(request)
    return redirect("home")


# this will be in domain/auth/register route
# because it use django.auth library
class RegisterView(View):
    template_name = "accounts/register.html"

    # get the webpage view
    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, context={"form": form})

    # send user register inputs
    def post(self, request):
        f_dict = {k: v[0] for k, v in dict(request.POST).items()}
        # fields = [request.POST.get(keys) for keys in request.POST.keys()]
        form = UserCreationForm(request.POST)
        print(form.data)
        print(f_dict)

        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

        return render(request, self.template_name, {"form": form})

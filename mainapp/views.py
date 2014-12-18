from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from mainapp import models
from mainapp.forms import UserForm, UserProfileForm, SelectProductForm, PaymentForm


@login_required
def home(request):
    products = models.Product.objects.filter(customer=models.Customer.objects.get(user=request.user))
    if (request.method == 'POST'):
        form = SelectProductForm(products, data=request.POST)
        if form.is_valid():
            products_data = []
            for index, val in enumerate(form.cleaned_data.get("products")):
                products_data.append(form.fields["products"].choices[index][1])
            request.session["products"] = products_data
            return redirect("/payment")
    else:
        form = SelectProductForm(products)
        context = {'form': form}
        return render(request, "home.html", context)


@login_required
def payment(request):
    if request.session.get("products", None) is not None:
        print(request.session["products"])
        context = {"form": PaymentForm()}
        return render(request, "payment.html", context)
    else:
        return redirect("/home")

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
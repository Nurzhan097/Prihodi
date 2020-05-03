from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms


def main(request):
	pass


@login_required
def profile_page(request):
	pass


def register(request):
	if request.method == 'POST':
		user_form = forms.UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Создаем нового пользователя, но пока не сохраняем в базу данных
			new_user = user_form.save(commit=False)
			# Задаем пользователю зашифрованный пароль
			new_user.set_password(user_form.cleaned_data['password'])
			# Сохраняем пользователя в базе данных
			new_user.save()
			# Создания профиля пользователя
			models.Profile.objects.create(user=new_user)
			return render(request, 'account/register_done.html', {'new_user': new_user})
	else:
		user_form = forms.UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form': user_form})

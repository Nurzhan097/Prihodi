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
	context = {}
	user_form = forms.UserRegistrationForm()
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

			context['new_user'] = new_user
			context['next'] = 'profile'
			return render(request, 'account/registration/registration_done.html', context)

	context['user_form'] = user_form
	return render(request, 'account/registration/registration_form.html', {'user_form': user_form})

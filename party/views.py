from django.shortcuts import render


def main(request):
	return render(request, 'party/main_page.html')


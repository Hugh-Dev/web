from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.

class IndexView(View):
	"""docstring for IndexView"""
	template_name = 'template.index.html'
	def get(self, request):
		return render(request, self.template_name)
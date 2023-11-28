from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from . forms import ContactForm
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Skill
		)


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		blogs = Blog.objects.filter()
		portfolio = Portfolio.objects.filter()
		skills = Skill.objects.all()
		
	
	
		context["skills"] = skills
		context["blogs"] = blogs
		context["portfolio"] = portfolio

		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter()


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter()


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"

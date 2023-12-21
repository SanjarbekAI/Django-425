from django.shortcuts import render, redirect

from pages.models import BlogModel, FeedbackModel, EmailModel
from products.models import ProductModel


def home_page_view(request):
    products = ProductModel.objects.all().order_by('-pk')[:5]
    feedbacks = FeedbackModel.objects.all().order_by('-pk')[:10]
    context = {
        "products": products,
        "feedbacks": feedbacks
    }
    return render(request, 'home.html', context)


def contact_page_view(request):
    return render(request, 'contact.html')


def about_page_view(request):
    return render(request, 'about-us.html')


def blog_page_view(request):
    blogs = BlogModel.objects.all().order_by('-created_at')[:6]
    recent_blogs = BlogModel.objects.all().order_by('-updated_at')[:3]
    context = {
        "blogs": blogs,
        "recent_blogs": recent_blogs,
    }
    return render(request, 'blog-list.html', context)


def email_post(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_email = EmailModel(email=email)
        new_email.save()
        return redirect('pages:home')
    else:
        return render(request, 'home.html')

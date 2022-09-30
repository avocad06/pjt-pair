from django.shortcuts import render, redirect
from review.models import Review
from datetime import datetime

# Create your views here.
def index(request):
    review = Review.objects.all()
    context = {
        "reviews": review,
    }
    return render(request, "review/index.html", context)


def new(request):
    return render(request, "review/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Review.objects.create(title=title, content=content)
    return redirect("review:index")


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "review/detail.html", context)


def edit(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "review/edit.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    title = request.GET.get("title")
    content = request.GET.get("content")
    
    review.updated_at = datetime.now()
    review.title = title
    review.content = content
    review.save()

    return redirect("review:detail", review.pk)

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect("review:index")

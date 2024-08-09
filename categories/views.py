from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from categories.models import Category
from categories.forms import CategoryForm


@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user) | Category.objects.filter(created_by_user=False)
    return render(request, 'categories/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            custom_name = form.cleaned_data['custom_name']
            Category.create_custom_category(custom_name, request.user)
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})

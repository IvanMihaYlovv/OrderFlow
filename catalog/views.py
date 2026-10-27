from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Product, Material, Category

from catalog.forms import MaterialForm, CategoryForm, ProductForm


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    category_id = request.GET.get('category')

    if category_id:
        products = products.filter(category_id=category_id)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_id,
    }

    return render(request, 'product/products-list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product/product-detail.html', context)


def product_create(request):
    if request.method == 'POST':

        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('product-list',)

    else:
        form = ProductForm()

    return render(request, 'product/product_form.html', context={'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':

        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():

            form.save()
            return redirect('product-list',)

    else:
        form = ProductForm(instance=product)

    return render(request, 'product/product_form.html', context={'form': form, 'product': product})



def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':

        product.delete()
        return redirect('product-list',)

    return render(request, 'product/product_confirm_delete.html', context={'product': product})


def materials_list(request):
    materials = Material.objects.all()

    context = {'materials': materials}

    return render(request, 'material/material-list.html', context)


def material_detail(request, pk):
    material = get_object_or_404(Material, pk=pk)
    context = {'material': material}
    return render(request, 'material/material-detail.html', context)



def material_create(request):

    if request.method == 'POST':

        form = MaterialForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('material-list',)

    else:
        form = MaterialForm()

    return render(request, 'material/material_form.html', context={'form': form})


def material_update(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)

        if form.is_valid():
            form.save()
            return redirect('material-list',)

    else:
        form = MaterialForm(instance=material)


    return render(request, 'material/material_form.html', context={'form': form, 'material': material})



def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        material.delete()
        return redirect('material-list',)

    return render(request, 'material/material_confirm_delete.html', {
        'material': material
    })



def category_list(request):

    categories = Category.objects.all()
    return render(request, 'category/category_list.html', context={'categories': categories})


def category_detail(request, pk):

    category = get_object_or_404(Category, pk=pk)
    context = {'category': category}
    return render (request, 'category/category-detail.html', context)



def category_create(request):

    if request.method == 'POST':

        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category-list',)

    else:
        form = CategoryForm()

    return render(request, 'category/category_form.html', context={'form': form})


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':

        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():

            form.save()

            return redirect('category-list',)

    else:
        form = CategoryForm(instance=category)

    return render(request, 'category/category_form.html', context={'form': form, 'category': category})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':

        category.delete()
        return redirect('category-list',)

    return render(request, 'category/category_confirm_delete.html', {
        'category': category
    })
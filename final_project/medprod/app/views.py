from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from app.forms import AddProduct, AddConsumer
from .models import Product, Application, Consumer, Consumption, Supplier, Material, Material_costs_1000units, Employee
#from django.views import View
#from itertools import chain
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    return render(request, 'home.html')

def company(request):
    return render(request, 'company.html')

def products(request):

    products = Product.objects.all()
    viewed_products = request.session.get("viewed_products", {})

    return render(request, 'products.html', {"products": products, "viewed_products": viewed_products})

def product(request, id):
    try:
        p = Product.objects.get(id_product=id)
    except:
        return Http404(request)

    viewed_products = request.session.get("viewed_products", {})
    viewed_products[p.id_product] = p.id_product
    request.session["viewed_products"] = viewed_products

    return render(request, 'product.html', {"product": p, "viewed_products": viewed_products})

def add_product(request):

    if request.method == "POST": 
        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            product_ent = Product()
            product_ent.id_product = form.cleaned_data['id_product']
            product_ent.product_name = form.cleaned_data['product_name']
            product_ent.description = form.cleaned_data['description']
            product_ent.image = form.cleaned_data['image']
            product_ent.matrix_type = form.cleaned_data['matrix_type']
            product_ent.ligand = form.cleaned_data['ligand']
            product_ent.economic_stage = form.cleaned_data['economic_stage']
            product_ent.registration = form.cleaned_data['registration']
            product_ent.price = form.cleaned_data['price']

            product_ent.save()

            return redirect('products')


    else: 
        form = AddProduct()

    return render(request, 'add_product.html', {'form': form})

def add_consumer(request):

    if request.method == "POST": 
        form = AddConsumer(request.POST)

        if form.is_valid():
            consumer_ent = Consumer()
            consumer_ent.consumer_name = form.cleaned_data['consumer_name']
            consumer_ent.adress = form.cleaned_data['adress']
            consumer_ent.phone_number = form.cleaned_data['phone_number']
            consumer_ent.postcode = form.cleaned_data['postcode']
            consumer_ent.site = form.cleaned_data['site']
            consumer_ent.transportation = form.cleaned_data['transportation']

            consumer_ent.save()

            return redirect('partners')


    else: 
        form = AddConsumer()

    return render(request, 'add_consumer.html', {'form': form})

def application(request):
    
    applications = Application.objects.all()

    return render(request, 'application.html', {'applications': applications})

def partners(request):

    consumers = Consumer.objects.all()
    suppliers = Supplier.objects.all()
    
    return render(request, 'partners.html', {"consumers": consumers, "suppliers": suppliers})

def contacts(request):
    return render(request, 'contacts.html')

def sales(request):
    return render(request, 'sales.html')

def employes(request):

    employes = Employee.objects.all()

    return render(request, 'employes.html', {"employes": employes})
    
def materials(request):

    materials = Material.objects.all()

    return render(request, 'materials.html', {"materials": materials})

def recipe(request):

    return render(request, 'recipe.html')

# class SearchView(View):
#     template_name = 'search.html'
 
#     def get(self, request, *args, **kwargs):
#         context = {}
 
#         q = request.GET.get('q')
#         if q:
#             query_sets = []  
 
            
#             query_sets.append(Product.objects.search(query=q))
#             query_sets.append(Consumer.objects.search(query=q))
#             query_sets.append(Supplier.objects.search(query=q))
#             query_sets.append(Material.objects.search(query=q))
 
            
#             final_set = list(chain(*query_sets))
 
#             context['last_question'] = '?q=%s' % q  
 
#             current_page = Paginator(final_set, 10)
 
#             page = request.GET.get('page')
#             try:
#                 context['object_list'] = current_page.page(page)
#             except PageNotAnInteger:
#                 context['object_list'] = current_page.page(1)
#             except EmptyPage:
#                 context['object_list'] = current_page.page(current_page.num_pages)
 
#         return render(request=request, template_name=self.template_name, context=context)
from django.shortcuts import render, redirect
from django.views import generic
from .models import Book, Author, Language, Genre
# from books_service.forms import AddBook, AddAuthor
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    """
    Display function for the home page of the site.
    """
    # Generation of "quantities" of main objects
    num_books=Book.objects.all().count()
    num_authors=Author.objects.all().count() 

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Rendering the HTML template index.html with data inside variable context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_authors':num_authors, 'num_visits':num_visits}
    )



class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 20


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book


class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 20


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author


class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__' 


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')




# def add_book(request):

#     if request.method == "POST": 
#         form = AddBook(request.POST, request.FILES)

#         if form.is_valid():
#             book_ent = Book()
#             book_ent.title = form.cleaned_data['title']
#             book_ent.author = form.cleaned_data['author']
#             book_ent.summary = form.cleaned_data['summary']
#             book_ent.isbn = form.cleaned_data['isbn']
#             book_ent.genre = form.cleaned_data['genre']
#             book_ent.language = form.cleaned_data['language']

#             book_ent.save()

#             return redirect('books')

#     else: 
#         form = AddBook()

#     return render(request, 'add_book.html', {'form': form})

# def add_author(request):

#     if request.method == "POST": 
#         form = AddAuthor(request.POST)

#         if form.is_valid():
#             author_ent = Author()
#             author_ent.first_name = form.cleaned_data['first_name']
#             author_ent.last_name = form.cleaned_data['last_name']
#             author_ent.date_of_birth = form.cleaned_data['date_of_birth']
#             author_ent.date_of_death = form.cleaned_data['date_of_death']

#             author_ent.save()

#             return redirect('authors')

#     else: 
#         form = AddAuthor()

#     return render(request, 'add_author.html', {'form': form})

from django.shortcuts import render
from django.views import generic
from .models import Book, Author, Language, Genre

# Create your views here.


def index(request):
    """
    Display function for the home page of the site.
    """
    # Generation of "quantities" of main objects
    num_books=Book.objects.all().count()
    num_authors=Author.objects.all().count() 

    # Rendering the HTML template index.html with data inside variable context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_authors':num_authors},
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
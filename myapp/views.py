from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.models import Book

from myapp.forms import BookForm

# Create your views here.

# listing books

# localhost:8000/books/all

# method:get

class BookListView(View):

    def get(self,request,*args,**kwargs):

        qs=Book.objects.all()

        return render(request,"book_list.html",{"data":qs})
    
class BookCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BookForm()

        return render(request,"book_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=BookForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Book.objects.create(**data)

            return redirect("book-list")
        
        else:

            return render(request,"book_add.html",{"form":form_instance})

class BookDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("mwogli")

        qs=Book.objects.get(id=id)

        return render(request,"book_detail.html",{"data":qs})
    
class BookDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("mwogli")

        Book.objects.filter(id=id).delete()

        return redirect("book-list")
    
class BookUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("mwogli")

        book_obj=Book.objects.get(id=id)

        dictionary={
            "title":book_obj.title,
            "year":book_obj.year,
            "author":book_obj.author,
            "genre":book_obj.genre,
            "language":book_obj.language

            }

        form_instance=BookForm(initial=dictionary)

        return render(request,"book_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("mwogli")

        form_instance=BookForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Book.objects.filter(id=id).update(**data)

            return redirect("book-list")
        
        else:

            return render(request,"book_edit.html",{"form":form_instance})


    

    





            

        

                      
            



    


    

    

    

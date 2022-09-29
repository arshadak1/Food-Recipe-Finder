from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Recipe
from .forms import RecipeForm
# Create your views here.
def home(request):
    return render(request, "foods/home.html")


class RecipesListView(ListView):
    model = Recipe
    template_name = 'foods/recipes_list_view.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-input') or ''

        if search_input:
            context['recipes'] = context['recipes'].filter(title__icontains=search_input)
        context['search_input_text'] = search_input

        return context


class RecipesDetailView(DetailView):
    model = Recipe
    template_name = 'foods/recipe_detail_view.html'
    context_object_name = 'recipe_detail'
    pk_url_kwarg = 'pk'


class UserRecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'foods/user_recipes_list_view.html'
    context_object_name = 'user_recipes'

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_recipes'] = context['user_recipes'].filter(user=self.request.user)

        return context

class RecipesCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'foods/recipe_create_view.html'
    success_url = reverse_lazy('my-recipes')

    def form_valid(self, form):
        form = RecipeForm(self.request.POST, self.request.FILES)
        form.instance.user = self.request.user
        
        return super().form_valid(form)



class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'foods/recipe_create_view.html'
    success_url = reverse_lazy('my-recipes')

    def form_valid(self, form):
        form = RecipeForm(self.request.POST, self.request.FILES)
        form.instance.user = self.request.user
        
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'foods/recipe_delete_view.html'
    success_url = reverse_lazy('my-recipes')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


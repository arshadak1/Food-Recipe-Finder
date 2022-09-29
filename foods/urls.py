from django.contrib import admin
from django.urls import path, include
from .views import UserRecipesListView, RecipesListView, home, RecipesDetailView, RecipesCreateView, RecipeUpdateView, RecipeDeleteView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('recipes', RecipesListView.as_view(), name="recipes"),
    path('recipes/<int:pk>', RecipesDetailView.as_view(), name="recipes-detail"),
    path('my-recipes', UserRecipesListView.as_view(), name="my-recipes"),
    path('create-recipe', RecipesCreateView.as_view(), name="create-recipe"),
    path('my-recipes/edit/<int:pk>', RecipeUpdateView.as_view(), name="recipes-edit"),
    path('my-recipes/delete/<int:pk>', RecipeDeleteView.as_view(), name="recipes-delete"),



]
 
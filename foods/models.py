from email.policy import default
from django.db import models
from django.contrib.auth.models import User

from PIL import Image
# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=30, null=True,
                             blank=False, verbose_name='Recipe Name')
    pic_file = models.ImageField(
        default='default.jpg', verbose_name="Choose a picture", upload_to='recipe_pictures')
    description = models.TextField(verbose_name="How to prepare!")
    ingredients = models.TextField(verbose_name="Ingredients required")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created', 'title']

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if self.pic_file:
    #         image = Image.open(self.pic_file.path)

    #         if image.width > 500:
    #             width, height = image.width, image.height
    #             output_size = (500, 500*(height/width))
    #             image.thumbnail(output_size)

    #             image.save(self.pic_file.path)
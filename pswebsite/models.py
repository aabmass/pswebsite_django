from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    """
        The abstract base class for products in this app
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    user_creator = models.ForeignKey(User,
                                     verbose_name=("the user that created "
                                                   "this product"))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class PosterDimension(models.Model):
    length = models.PositiveSmallIntegerField("length along horizontal",
                                              help_text=("Length along the "
                                                         "bottom of a poster"))
    width = models.PositiveSmallIntegerField("length along vertical",
                                             help_text=("Length along the "
                                                        "vertical side of a "
                                                        "poster"))

class Poster(Product):
    dimension = models.ManyToManyField(PosterDimension)

    def __str__(self):
        return "Poster: {}. Created by {}".format(self.name, self.user)

class PosterImage(models.Model):
    """
        This model contains only an image field. We have to do it this way
        since we are not allowed to have an arbitrary number of image fields
        directly in the products
    """

    image = models.ImageField(upload_to="productimages")
    poster = models.ForeignKey(Poster)

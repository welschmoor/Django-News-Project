from django.db import models

# Create your models here.

class News(models.Model):
    # CharField has a mandatory attribute max_length
    # DateTimeField's attributes auto_now saves time each save.
    # and auto_now_add creates date of creation.
    # 'photos/%Y/%m/%d/' means we break up pics by year, m, d folders
    title = models.CharField(max_length=150, verbose_name="Der Titel")
    content = models.TextField(blank=True, verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Foto", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Published?")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Category", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        # this modifies the word News to Nachrichten
        verbose_name = 'Nachricht'
        verbose_name_plural = 'Nachrichten'
        # choose ordering. Second one is for ties, when
        # creation date is the same. - means descending
        ordering = ['-created_at', 'title' ]


class Category(models.Model):
    #db index indexates the field, making search faster
    title = models.CharField(max_length=150, db_index=True, verbose_name="Category Name")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

        ordering = ['title']

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class main(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('status', default=True)
    create_date = models.DateField('creation date',auto_now=False,auto_now_add=True)
    modify_date = models.DateField('creation date',auto_now=True,auto_now_add=False)
    delete_date =models.DateField('Delete date ',auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True 

class category(main):    
    name =models.CharField('Category name',max_length=100, unique=True)
    image = models.ImageField('Category Image',upload_to='category/')
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name
        ## .modify_date
class author(main):
    firts_name = models.CharField('frits name',max_length=100)
    last_name = models.CharField('last name',max_length=100)
    email = models.EmailField('E-mail',max_length=150)
    Description =models.TextField('Description')
    image = models.ImageField('Author image',null = True, blank=True, upload_to='authores/' )
    facebook = models.URLField('Facebook',null = True,blank=True)
    twitter  = models.URLField('Twitter',null = True,blank=True)
    instagram  = models.URLField('Instagram',null = True,blank=True)
    web  = models.URLField('web',null = True,blank=True)
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __str__(self):
        return '{0}{1}'.format(self.firts_name,self.last_name)

class post(main):
    title = models.CharField('Title',max_length=100, unique=True)
    slug = models.CharField('Slug',max_length=150, unique=True)
    Description =models.TextField('Description')
    id_author = models.ForeignKey(author, on_delete=models.CASCADE)
    id_category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField('Image post',upload_to='imagens/',max_length=150 )
    published =models.BooleanField('published/ no published', default=False)
    published = models.DateField('Publis date')

    content = RichTextField()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'post'
    def __str__(self):
        return self.title


    
    

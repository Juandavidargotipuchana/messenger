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
    webp = models.URLField('web',null = True,blank=True)
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

class web(main):
        about_us = models.TextField('About us ')
        phone = models.EmailField('phone ',max_length=20)
        email = models.CharField('E-mail',max_length=150)
        address = models.CharField('Adress ',max_length=200)
        class Meta:
            verbose_name= 'Web'
            verbose_name_plural = 'Webs' 
        def __str__ (self):
            return self.about_us



class social (main):
        facebook = models.URLField('Facebook',null = True,blank=True)
        twitter  = models.URLField('Twitter',null = True,blank=True)
        instagram  = models.URLField('Instagram',null = True,blank=True)
        webp  = models.URLField('web',null = True,blank=True)
        class Meta:
            verbose_name = 'Social network'
            verbose_name_plural = 'Social networks'
        
        def __str__(self):
            return self.facebook

class contact (main):
        firts_name =models.CharField('Firts name',max_length=100)
        last_name =models.CharField('Last name',max_length=100)
        Email = models.EmailField('Email',max_length=150)
        subject = models.CharField('Subject',max_length=100)
        message = models.TextField('Message')
        class Meta:
            verbose_name = ('Contac')
            verbose_name_plural = ('Contacs')
        def __str__ (self):
            return self.subject

class suscribers (main):       
        Email = models.EmailField('Email',max_length=150)        
        class Meta:
            verbose_name = ('Suscriber')
            verbose_name_plural = ('Suscribers')
        def __str__ (self):
            return self.Email          



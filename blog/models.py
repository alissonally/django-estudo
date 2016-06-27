from django.db import models

class Author(models.Model):
	name = models.CharField('Nome',max_length=150)
	email = models.EmailField('Email', unique=True)
	description = models.TextField('Descrição')

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField('Categoria',max_length=50)
	description = models.CharField('Descrição',max_length=255)
	
	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField('Tag', max_length=50)
	description = models.CharField('Descrição', max_length=255)
	def __str__(self):
		return self.name

class Post(models.Model):
	post_title = models.CharField('Título', max_length=200)
	post_slug = models.SlugField('Slug',unique=True)
	post_content = models.TextField('Conteudo')
	create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_date = models.DateTimeField(auto_now_add=False,auto_now=True)
	post_author = models.ForeignKey(Author)
	categories = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)
	
	def __str__(self):
		return self.post_title
from django.db import models
from ckeditor.fields import RichTextField
class Blog(models.Model):
    author = models.ForeignKey("auth.user",on_delete=models.CASCADE)
    topics = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank = True, null = True, verbose_name = "Import image")

    def __str__(self):
        return self.name
    class Meta():
        ordering = ['-pub_date']

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name="Comments",related_name="comments",null= "True")
    comment_author = models.CharField(max_length=50, verbose_name ="Author", null= "True")
    comment_content = models.CharField(max_length=250, verbose_name ="Comment", null= "True")


    def __str__(self):
        return self.comment_content

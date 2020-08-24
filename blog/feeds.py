from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class BlogRss(Feed):
    title = "Porus - blog"
    description = "Porus - blog"
    link = "/blogrss/"

    def items(self):
        return Post.objects.order_by('-id')[:5]

    def item_title(self,item):
        return item.title

    def item_description(self,item):
        return item.content



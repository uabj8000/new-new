import datetime
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

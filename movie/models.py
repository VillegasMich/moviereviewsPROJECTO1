from django.db import models
from openai.embeddings_utils import get_embedding, cosine_similarity
import numpy as np

# Create your models here.

def get_default_array():
  default_arr = np.random.rand(1536)  # Adjust this to your desired default array
  return default_arr.tobytes()

class Movie(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  emb = models.BinaryField(default=get_default_array())
  image = models.ImageField(upload_to='movie/images/', default = 'movie/images/default.jpg')
  url = models.URLField(blank=True)

  def __str__(self):
    return self.title
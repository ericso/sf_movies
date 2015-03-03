from django.db import models


class Location(models.Model):

  title = models.TextField()
  release_year = models.IntegerField(blank=True, null=True)
  locations = models.TextField(blank=True, null=True)
  fun_facts = models.TextField(blank=True, null=True)
  production_company = models.TextField(blank=True, null=True)
  distributor = models.TextField(blank=True, null=True)
  director = models.TextField(blank=True, null=True)
  writer = models.TextField(blank=True, null=True)
  actor1 = models.TextField(blank=True, null=True)
  actor2 = models.TextField(blank=True, null=True)
  actor3 = models.TextField(blank=True, null=True)
  latitude = models.DecimalField(
    decimal_places=4,
    max_digits=8,
    blank=True,
    null=True
  )
  longitude = models.DecimalField(
    decimal_places=4,
    max_digits=8,
    blank=True,
    null=True
  )

  class Meta:
    ordering = ('id',)
    unique_together = ('title', 'locations')

  def __str__(self):
    return self.title + " at " + self.locations

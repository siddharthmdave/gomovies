from django.db import models
import uuid


class Movie(models.Model):
    movieId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(max_length=60)
    description = models.TextField(max_length=200, blank=True, default="")
    duration = models.IntegerField()
    releaseDate = models.DateField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

class Cinema(models.Model):
    cinemaId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=60)
    totalScreen = models.IntegerField()
    city = models.TextField(max_length=60)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.city)


class Screens(models.Model):
    hallId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=60)
    totalSeat = models.IntegerField()
    cinemaId = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} @ {}'.format(self.name,self.cinemaId)


class Show(models.Model):
    showId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hallId = models.ForeignKey(Screens, on_delete=models.CASCADE)
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showTime = models.DateTimeField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} : {} ({})'.format(self.movieId,self.hallId,self.showTime.strftime("%H:%M"))

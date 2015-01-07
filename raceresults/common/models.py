import datetime
from django.db import models
from django.contrib.auth.models import User

class Org(models.Model):
    name = models.CharField(max_length=100)
    owner=models.ForeignKey(User)

    def __str__(self):
        return self.name

class BoatType(models.Model):
    name = models.CharField(max_length=100)
    length=models.DecimalField(decimal_places=2, max_digits=5)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Boat(models.Model):
    name = models.CharField(max_length=100)
    sail_number= models.CharField(max_length=20)
    type = models.ForeignKey(BoatType, blank=True, null=True)
    #owner=models.ForeignKey(Org)
    perf_rating = models.IntegerField()

    def __str__(self):
        return self.name

class Race(models.Model):
    name=models.CharField(max_length=100)
    start_time=models.DateTimeField(auto_now_add=True)
    length=models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    course=models.CharField(max_length=100, blank=True, null=True)
    #owner=models.ForeignKey(Org)
    start_time = models.DateTimeField()

    def __str__(self):
        return self.start_time.date().isoformat() + " -- " + self.name

    def score(self):
        race_results = self.raceresult_set.all()
        for single_result in race_results :
            single_result.correct_time()
            single_result.save()

        non_finished_results = filter(lambda result: result.finish_time == None, race_results )
        finished_results = filter(lambda result: result.finish_time != None, race_results )
        sorted_results = sorted(finished_results, key=lambda result: result.corrected_finish_time)


        for index, result in enumerate(finished_results):
            result.finish_place = index
            result.save()

        for result in non_finished_results:
            result.finish_place = len(finished_results) + 1
            result.save()

class RaceResult(models.Model):
    class Meta:
        ordering = ['finish_place']

    def __str__(self):
        return ' -- '.join([self.race.name, self.race.start_time.date().isoformat(), self.boat.name])

    boat = models.ForeignKey(Boat)
    finish_time = models.DateTimeField(blank=True, null=True)
    corrected_finish_time = models.DateTimeField(blank=True, null=True, editable=False)
    race = models.ForeignKey(Race)
    finish_place = models.IntegerField(null=True, blank=True)

    def elapsed_time(self):
        return self.finish_time - self.race.start_time

    def correct_time(self):
        if self.finish_time is None: return
        a=695
        b=525
        elapsed_time = self.elapsed_time()
        seconds_elapsed = elapsed_time.days * 3600 * 24 + elapsed_time.seconds
        print seconds_elapsed
        tcf = float(a) / (b+self.boat.perf_rating)
        corrected_seconds = seconds_elapsed * tcf
        print corrected_seconds

        self.corrected_finish_time  = self.race.start_time + datetime.timedelta(seconds=corrected_seconds)
        return self.corrected_finish_time

class Series(models.Model):
    name = models.CharField(max_length=100)
    races = models.ManyToManyField(Race, blank=True)
    #owner=models.ForeignKey(Org)





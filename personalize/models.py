from django.db import models


# Create your models here.
class Tea(models.Model):
    name = models.IntegerField(verbose_name='名前', blank=True, null=True)
    base = models.CharField(verbose_name='ベース', max_length=50, blank=True, null=True)
    symptoms1 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms2 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms3 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms4 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms5 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms6 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms7 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms8 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms9 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms10 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms11 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms12 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms13 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms14 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)
    symptoms15 = models.CharField(verbose_name='症状', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tea'

    def __int__(self):
        return self.name

    def __str__(self):
        return self.base + self.symptoms1 + self.symptoms2 + self.symptoms3 + self.symptoms4 + self.symptoms5 + \
            self.symptoms6 + self.symptoms7 + self.symptoms8 + self.symptoms9 + self.symptoms10 + \
            self.symptoms11 + self.symptoms12 + self.symptoms13 + self.symptoms14 + self.symptoms15


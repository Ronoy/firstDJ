# -*- coding: utf-8 -*-
#models.py
#from __future__ import unicode_literals
#from django.db import models
from django.db import models
# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name
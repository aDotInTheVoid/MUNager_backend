"""api/models.py: django models for the UCSMUN MUNager api"""

# Copyright (C) 2018  Nixon Enraght-Moony

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


# Create your models here.


class CardPage(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "Cardpage: {}".format(self.name)


class Card(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(
            help_text="The main text body to display on the card")
    media = models.URLField(
            help_text="The absolute url to the image for the card")
    page = models.ForeignKey(CardPage, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Committee(models.Model):
    name = models.CharField(max_length=20, help_text="Eg: Polictical 1, Human Rights")
    block = models.CharField(max_length=20, help_text="Eg: North, Science, Main")
    room = models.CharField(max_length=20, help_text="Eg: C1, Lund Theater")

    def __str__(self):
        return "Committee: {}".format(self.name)


class School(models.Model):
    name = models.CharField(max_length=20, help_text="Eg: UCS, Habs, City")

    def __str__(self):
        return "School: {}".format(self.name)


class Delegation(models.Model):
    country = models.CharField(max_length=20, help_text="Eg: China, Egypt, Cuba")
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return "Delegation of {}".format(self.country)


class Delegate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    delegation = models.ForeignKey(Delegation, on_delete=models.CASCADE)

    def __str__(self):
        return "Delegate ".format(self.user.username)


class Clause(models.Model):
    word = models.CharField(max_length=10)
    body = models.TextField(max_length=300)

    def __str__(self):
        return self.word + self.body


class Resolution(models.Model):
    author = models.ForeignKey(Delegate, on_delete=models.CASCADE)
    question_of = models.CharField(max_length=50)

    preamble = JSONField(help_text="The preamble of the resolution in json form")

    body = JSONField(help_text="The body of the resolution in json form")

    def __str__(self):
        return "{} ({})".format(self.question_of, self.author.delegation.country)

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
    name = models.CharField(max_length=30, help_text="Eg: Polictical 1, Human Rights")
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
    delegation = models.ForeignKey(Delegation, on_delete=models.SET_NULL, null=True)
    committee = models.ForeignKey(Committee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.user)


class Resolution(models.Model):
    author = models.ForeignKey(Delegate, on_delete=models.CASCADE)
    question_of = models.CharField(max_length=50)

    preamble = JSONField(help_text="The preamble of the resolution in json form")

    body = JSONField(help_text="The body of the resolution in json form")

    # Status

    NOT_SUBMITED = 0
    SUMBITTED = 1
    REJECTED_FOR_COMMITTEE = 2
    ACCEPTED_FOR_COMMITTED = 3
    LOBBIED = 4
    SELECTED_FOR_COMMITTEE = 5
    FAILED_BY_COMMITTEE = 6
    PASSED_BY_COMMITTEE = 7
    SELECTED_FOR_GA = 8
    FAILED_BY_GA = 9
    PASSED_BY_GA = 10

    STATUS_CHOICES = (
        (NOT_SUBMITED, "Not Submitted"),
        (SUMBITTED, "Submitted"),
        (REJECTED_FOR_COMMITTEE, "Rejected for Committee"),
        (ACCEPTED_FOR_COMMITTED, "Accepted for Committee"),
        (LOBBIED, "Lobbied"),
        (SELECTED_FOR_COMMITTEE, "Selected for Committee"),
        (FAILED_BY_COMMITTEE, "Failed by Committee"),
        (PASSED_BY_COMMITTEE, "Passed by Committee"),
        (SELECTED_FOR_GA, "Selected for GA"),
        (FAILED_BY_GA, "Failed by GA"),
        (PASSED_BY_GA, "Passed by GA"),
    )

    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=NOT_SUBMITED)

    def __str__(self):
        return "{} ({})".format(self.question_of, self.author.delegation.country)



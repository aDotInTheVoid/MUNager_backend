"""api/admin.py: admin site config for the UCSMUN MUNager api"""

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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import CardPage, Card, Delegate, Delegation, School, Committee, Resolution

# Look customistation
admin.site.site_header = "UCSMUNager "


# Register your models here.

# CMS

class CardInLine(admin.StackedInline):
    model = Card


class CardPageAdmin(admin.ModelAdmin):
    inlines = [CardInLine]


admin.site.register(CardPage, CardPageAdmin)


# Users

class DelegateInline(admin.StackedInline):
    model = Delegate
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (DelegateInline,)
    list_display = ()


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'block')


@admin.register(Delegation)
class DelegationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'school')
    list_filter = ('school',)


@admin.register(Resolution)
class ResolutionAdmin(admin.ModelAdmin):

    # Todo: less hacky
    def get_country(self):
        return self.author.delegation.country

    get_country.short_description = 'Country'

    # Todo: less hacky
    def get_committee(self):
        return self.author.committee

    get_committee.short_description = 'Committee'

    # Todo: less hacky
    def get_author(self):
        name = self.author.user.first_name + self.author.user.last_name
        return name if name else self.author.user.username

    get_author.short_description = 'Author'

    list_display = ('question_of', 'status', get_country, get_committee, get_author)
    list_filter = ('status', 'author__delegation__country', 'author__committee')


admin.site.register(School)

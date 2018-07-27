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

from .models import CardPage, Card
# Register your models here.


class CardInLine(admin.StackedInline):
    model = Card


class CardPageAdmin(admin.ModelAdmin):
    inlines = [CardInLine]


admin.site.register(CardPage, CardPageAdmin)

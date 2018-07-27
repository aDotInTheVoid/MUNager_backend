"""api/schema.py: qraphQL schemas for UCSMUN MUNager api"""

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

import graphene

from graphene_django.types import DjangoObjectType

from .models import Card, CardPage


class CardType(DjangoObjectType):
    class Meta:
        model = Card


class CardPageType(DjangoObjectType):
    class Meta:
        model = CardPage


class Query(object):
    all_cardpages = graphene.List(CardPageType)
    all_cards = graphene.List(CardType)

    cardpage = graphene.Field(CardPageType,
                              id=graphene.Int(),
                              name=graphene.String())

    card = graphene.Field(CardType,
                          id=graphene.Int())

    def resolve_all_cardpages(self, info, **kwargs):
        return CardPage.objects.all()

    def resolve_all_cards(self, info, **kwargs):
        return Card.objects.select_related('cardpage').all()

    def resolve_cardpage(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return CardPage.objects.get(pk=id)
        elif name is not None:
            return CardPage.objects.get(name=name)
        else:
            return None

    def resolve_card(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return CardPage.objects.get(pk=id)
        else:
            return None



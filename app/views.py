# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader, Template
from django.http import HttpResponse
from django import template
from iommi import Page, html, Table, Style, Column
from iommi.attrs import render_attrs
from tri_declarative import Namespace

from app.models import Product


@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        try:
            html_template = loader.get_template(load_template)
        except:
            html_template = loader.get_template(load_template+'.html')
            pass

        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        context['message'] = e
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


class MyPage(Page):
    # h1 = html.h1('Welcome!')
    # body_text = 'Welcome to my iommi site...'
    my_table = Table(
        title='Promotions',
        auto__model=Product,
        page_size=10,

        # filters
        columns__name__filter__include=True,
        columns__name__filter__freetext=True,

        cell__url='/products/1',
        cell__url__title='visit product 1',

        columns__select__include=True,
        # columns__name__bulk__include=True,
        # columns__store__bulk__include=True,

        query_from_indexes=True,
    )


class AlbumTable(Table):
    class Meta:
        auto__model = Product
        page_size = 20
        attrs__class = {
            'row': True,
            'row-cols-6': True,
            'row-cols-md-3': True,
            'row-cols-xl-12': True,
            'g-2': True,
            'pb-4': True,
            'pt-0': True,
            'table': False,
            'table-sm': False,
        }

        # columns__name__cell__url = lambda row, **_: row.get_absolute_url()
        # columns__name__filter__include = True
        # columns__year__filter__include = True
        # columns__year__filter__field__include = False
        # columns__artist__filter__include = True
        # columns__edit = Column.edit(
        #     include=lambda request, **_: request.user.is_staff,
        # )
        # columns__delete = Column.delete(
        #     include=lambda request, **_: request.user.is_staff,
        # )
        # actions__create_album = Action(attrs__href='/supernaut/albums/create/', display_name=_('Create album'))


class IndexPage(Page):
    albums = AlbumTable(
        title='Products',
        auto__model=Product,
        page_size=10,
        tag='div',
        header__template=None,
        cell__tag=None,
        row__template=Template(
            """{% include 'includes/components/product_row.html' %}"""
        ),
        container__attrs__class={
            'iommi-table-container': False,
            'container-': False
        },
    )

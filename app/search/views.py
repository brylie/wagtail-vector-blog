from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from wagtail.models import Page
from blog.models import BlogPage


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Default Search
    if search_query:
        default_results = Page.objects.live().search(search_query)
    else:
        default_results = Page.objects.none()

    # Vector Search
    if search_query:
        vector_results = BlogPage.vector_index.search(
            search_query,
        )
    else:
        vector_results = BlogPage.objects.none()

    # Pagination for default results
    default_paginator = Paginator(default_results, 5)
    try:
        default_results = default_paginator.page(page)
    except PageNotAnInteger:
        default_results = default_paginator.page(1)
    except EmptyPage:
        default_results = default_paginator.page(default_paginator.num_pages)

    # Pagination for vector results
    vector_paginator = Paginator(vector_results, 5)
    try:
        vector_results = vector_paginator.page(page)
    except PageNotAnInteger:
        vector_results = vector_paginator.page(1)
    except EmptyPage:
        vector_results = vector_paginator.page(vector_paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "default_results": default_results,
            "vector_results": vector_results,
        },
    )

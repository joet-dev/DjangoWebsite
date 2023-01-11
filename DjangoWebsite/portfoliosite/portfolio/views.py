from django.http import HttpResponse
from django.template import loader

from .models import PortfolioItem


# Create your views here.

def index(request):
    latest_portfolio_list = PortfolioItem.objects.order_by('-item_date')[:5]
    template = loader.get_template('portfolio/index.html')
    context = {
        'latest_portfolio_list': latest_portfolio_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, item_id):
    return HttpResponse("DETAIL SCREEN. ITEM %s." % item_id)



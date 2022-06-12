import datetime
from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf 

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(), 
            'proposal_id': 1233434,
            'company_personal': 'Cooper Mann',
            'Position': 'Preident',
            'landscape_company_name': 'Forever Green Landscape Services, Inc.'
        }
        pdf = render_to_pdf('pdf/proposal.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
        # return HttpResponse(pdf)

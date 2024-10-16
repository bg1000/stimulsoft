import json
import logging
import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
from .models import ReportTemplate


def report_view(request):
    """ View for rendering stimulsoft report """
    logger.debug(f"Running view 'report_view' for {request.method} {request.path} with params {request.GET}")
    from stimulsoft_reports.report import StiReport
    from stimulsoft_reports.viewer import StiViewer
    from stimulsoft_reports.viewer.enums import StiToolbarDisplayMode
    viewer = StiViewer()
    viewer.options.appearance.fullScreenMode = True
    viewer.options.toolbar.displayMode = StiToolbarDisplayMode.SEPARATED
    viewer.onPrepareVariables += 'prepareVariables'
    viewer.onPrepareVariables += prepare_variables
    if viewer.processRequest(request):
        logger.info("Stimulsoft server Framework responding.")
        return viewer.getFrameworkResponse()
    template_url = ReportTemplate.objects.get(name='test-report').template.url
    logger.info(f"Loading report template from {template_url}")
    report = StiReport()
    report.loadFile(template_url) 
    viewer.report = report
    js = viewer.javascript.getHtml()
    logger.debug(f"Viewer JavaScript: {js}")
    html = viewer.getHtml()
    logger.debug(f"Viewer HTML: {html}")
    return render(request, 'reports/report_viewer.html', {'viewerJavaScript': js, 'viewerHtml': html})


def report_data(request, record_id):
    """ View for providing report data """
    logger.info(f"Running view 'report_data' with record_id: {record_id}")
    file_path = os.path.join(os.path.dirname(__file__), 'report_data.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return JsonResponse(data)

def prepare_variables(args):
    """ Callback function to adjust variable for this instance of the report."""
    logger.info("Preparing variables for report")
    logger.info(f"args.variables['record_id'].value: {args.variables['record_id'].value}")
    args.variables['record_id'].value = "5678"
    logger.info(f"args.variables['record_id'].value: {args.variables['record_id'].value}")
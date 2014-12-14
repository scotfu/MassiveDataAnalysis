#coding=utf8
import os
import json

from bson import json_util

from flask.views import View, MethodView
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash


from . import app
from .utils import get_trip, get_tip, get_temperature,get_area

class ListView(View):

    def get_template_name(self):

        raise NotImplementedError()
        
    def render_template(self, context):

        return render_template(self.get_template_name(), **context)

    def dispatch_request(self,**kwargs):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

        
class RenderTemplateView(View):
    
    def __init__(self, template_name):
        self.template_name = template_name
        
    def dispatch_request(self):
        return render_template(self.template_name)
        
        
        
class IndexView(ListView):

    def get_template_name(self):
        return 'index.html'

    def get_objects(self):
        return get_collections()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = obj.strftime('%m-%d-%Y-%H')
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object
            
class Temperature_Hour(MethodView):

    def get(self):
        start_date = request.args.get('start','2013-01-01')
        end_date = request.args.get('end','2013-01-31')        
        result = get_temperature(start_date, end_date)
        return json.dumps(result)        

class Area_Hour(MethodView):

    def get(self):
        start_date = request.args.get('start','2013-01-01')
        end_date = request.args.get('end','2013-01-31')        
        result = get_area(start_date, end_date)
        return json.dumps(result)        


class Trip_Count(MethodView):

    def get(self):
        start_date = request.args.get('start','2013-01-01')
        end_date = request.args.get('end','2013-01-31')        
        result = get_trip(start_date, end_date)
        return json.dumps(result)

class Tip_Count(MethodView):

    def get(self):
        start_date = request.args.get('start','2013-01-01')
        end_date = request.args.get('end','2013-01-31')        
        result = get_tip(start_date, end_date)
        return json.dumps(result)
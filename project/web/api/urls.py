from . import app
from .views import RenderTemplateView, Trip_Count, Tip_Count, Temperature_Hour, Area_Hour

app.add_url_rule('/chart/', view_func=RenderTemplateView.as_view('chart', template_name='chart.html'))
app.add_url_rule('/api/tip/', view_func=Tip_Count.as_view('tip'))
app.add_url_rule('/api/area/', view_func=Area_Hour.as_view('area'))
app.add_url_rule('/api/trip/', view_func=Trip_Count.as_view('trip'))
app.add_url_rule('/api/temperature/', view_func=Temperature_Hour.as_view('temperatue'))
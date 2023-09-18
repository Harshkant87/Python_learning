import justpy as jp
import pandas
from datetime import datetime
from pytz import utc


data = pandas.read_csv(r"C:\python_learning\16.Data_analysis_and_visualization\course_reviews.csv", parse_dates=['Timestamp'])
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_avg = data.groupby(['Week']).mean(numeric_only = True)

chart_def = '''
{
    chart: {
        type: 'column'
    },
    title: {
        text: 'Week vs rating avg',
        align: 'center'
    },
    subtitle: {
        text:'Source: <a target = "_blank", href="https://www.indexmundi.com/agriculture/?commodity=corn">indexmundi</a>',
        align: 'left'
    },
    xAxis: {
        title: {
            text: 'Week'
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Ratings'
        }
    },
    tooltip: {
        valueSuffix: '/5'
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: [
        {
            name: 'Rating',
            data: [406292, 260000, 107000, 68300, 27500, 14500]
        }
    ]
}
'''

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of course reviews", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis")
    hc = jp.HighCharts(a = wp, options = chart_def)
    hc.options.xAxis.categories = list(week_avg.index)
    hc.options.series[0].data = list(week_avg['Rating'])

    return wp

jp.justpy(app)

import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv(r"C:\python_learning\16.Data_analysis_and_visualization\course_reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_avg = data.groupby(['Day']).mean(numeric_only = True)

chart_def = '''
{
    chart: {
        type: 'column'
    },
    title: {
        text: 'Day vs rating avg',
        align: 'center'
    },
    subtitle: {
        text:'Source: <a target = "_blank", href="https://www.indexmundi.com/agriculture/?commodity=corn">indexmundi</a>',
        align: 'left'
    },
    xAxis: {
        title: {
            text: 'Date'
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
            name: 'Corn',
            data: [406292, 260000, 107000, 68300, 27500, 14500]
        }
    ]
}
'''

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of course reviews", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis", classes = "text-center")
    hc = jp.HighCharts(a = wp, options = chart_def)

    # print(hc.options.series)
    hc.options.series[0].name = 'Avg-day-rating'
    hc.options.series[0].data = list(zip(day_avg.index, day_avg['Rating']))

    return wp

jp.justpy(app)
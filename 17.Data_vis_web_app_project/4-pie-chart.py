import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

chart_def = '''
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Percentages of courses with reviews',
        align: 'left'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Courses',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 70.67,
            sliced: true,
            selected: true
        }, {
            name: 'Edge',
            y: 14.77
        },  {
            name: 'Firefox',
            y: 4.86
        }, {
            name: 'Safari',
            y: 2.63
        }, {
            name: 'Internet Explorer',
            y: 1.53
        },  {
            name: 'Opera',
            y: 1.40
        }, {
            name: 'Sogou Explorer',
            y: 0.84
        }, {
            name: 'QQ',
            y: 0.51
        }, {
            name: 'Other',
            y: 2.6
        }]
    }]
}
'''

data = pandas.read_csv(r"C:\python_learning\16.Data_analysis_and_visualization\course_reviews.csv", parse_dates=['Timestamp'])
rat_count = data.groupby(['Rating']).count()
# for v1, v2 in zip(rat_count.index, rat_count['Progress']):
#     print(v1, v2)

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of course reviews with ratings", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis", classes = "text-center")
    hc = jp.HighCharts(a = wp, options = chart_def)

    # print(hc.options.series)
    hc_data = [{"name": "Rating: " + str(v1), "y": v2} for v1, v2 in zip(rat_count.index, rat_count['Progress'])]
    hc.options.series[0].data = hc_data
    # hc.options.series[0].data = list(zip(day_avg.index, day_avg['Rating']))

    return wp

jp.justpy(app)
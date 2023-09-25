import justpy as jp
import pandas
from datetime import datetime
from pytz import utc


data = pandas.read_csv(r"C:\python_learning\16.Data_analysis_and_visualization\course_reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_avg = data.groupby(['Month', 'Progress'])['Rating'].mean(numeric_only = True)
dates = []
progress = []

for i in range(0, len(month_avg.index)):
    # time = float(month_avg.index[i][0].replace("-",""))
    dates.append(month_avg.index[i][0])
    progress.append(month_avg.index[i][1])
# print(dates)
# print(progress)

chart_def = '''
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Moose and deer hunting in Norway, 2000 - 2021',
        align: 'left'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048
            ]
    }]
}
'''

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of course reviews", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis")
    hc = jp.HighCharts(a = wp, options = chart_def)
    hc.options.xAxis.categories = dates
    # hc.options.series[0].data = list(week_avg['Rating'])
    # print(progress)

    return wp

jp.justpy(app)

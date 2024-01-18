# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from .models import Sales
from django.contrib.auth.decorators import login_required
import plotly.express as px
from django.utils import timezone



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            # Add an error message or handle invalid login here
            pass
    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required
def user_dashboard(request):
    user_sales = Sales.objects.filter(user=request.user)
    user_sales = user_sales.order_by('-date')

    current_month = timezone.now().month
    user_sales_current_month = user_sales.filter(date__month=current_month)
    
    total_sales_amount = user_sales_current_month.aggregate(total_sales=Sum('total_sale'))['total_sales'] or 0
    num_sales = user_sales_current_month.count()
    total_items_sold = user_sales_current_month.aggregate(total_items=Sum('quantity'))['total_items'] or 0

    sales_data = list(user_sales_current_month.values('date').annotate(total_per_day=Sum('total_sale')))

    # Create a line chart
    fig = px.line(sales_data, x='date', y='total_per_day', title='Total Sales per Day', labels={'total_per_day': 'Total Sales'})
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Total Sales')

    graph_json = fig.to_json()

    context = {
        'user_sales': user_sales,
        'total_sales_amount': total_sales_amount,
        'num_sales': num_sales,
        'total_items_sold': total_items_sold,
        'graph_json': graph_json,
    }

    return render(request, 'user_dashboard.html', context)
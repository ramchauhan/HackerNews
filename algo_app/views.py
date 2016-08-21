import time
from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import FibonacciInputForm
from .fib_calculation import FibCalculator


def algo_view(request):
    """
    Handles the Post and Get request of the Form which is requested by User
    :param request:
    :return:
    """
    context = RequestContext(request)
    if request.method == 'POST':
        start = time.time()
        form = FibonacciInputForm(data=request.POST)
        # check whether from is valid:
        if form.is_valid():
            input_num = form.cleaned_data['input_number']
            fin_calculator = FibCalculator(input_num)
            res = fin_calculator.get_nth_number()
            return render_to_response('algo_app/fib_result.html', {'res': res, 'time': time.time() - start},
                                      context)
    else:
        form = FibonacciInputForm()
    return render_to_response('algo_app/fib_input.html', {'form': form}, context)

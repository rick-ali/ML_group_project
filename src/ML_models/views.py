from django.shortcuts import render
from django.http import HttpResponse
from ML_models.ml_scripts.polynomial_regression import runPolyRegression

# Create your views here.
def polynomial_regression_view(request):
    context = {
        'meanAbsoluteError'    : "",
        'residualSumOfSquares' : "",
        'R2score'              : ""
    }
    if request.method == "POST":
        try:
            # Load data from form
            degree = int(request.POST.get('degree'))
            test_size = float(request.POST.get('test_size'))
            interaction_only = bool(request.POST.get('interaction_only'))
            include_bias = bool(request.POST.get('include_bias'))
            normalize = bool(request.POST.get('normalize'))

            #Run ML model and get metrics
            results = runPolyRegression(test_size,degree,interaction_only,include_bias,normalize)
            context = {
            'meanAbsoluteError'    : results[0],
            'residualSumOfSquares' : results[1],
            'R2score'              : results[2]
            }
        except:
            print("AN ERROR OCCURRED")
            pass
    return render(request, "polynomialRegressionForm.html", context)
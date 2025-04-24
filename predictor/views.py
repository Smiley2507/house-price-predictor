import os
import joblib
import numpy as np
from django.conf import settings
from django.shortcuts import render
from .forms import PredictionForm
from .models import PredictionResult

# Load the model
model_path = os.path.join(settings.BASE_DIR, 'house_price_model.joblib')
model = joblib.load(model_path)

def home(request):
    form = PredictionForm()
    prediction = None
    
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['house_size']
            price = predict_price(size)
            
            # Save prediction to database
            result = PredictionResult(house_size=size, predicted_price=price)
            result.save()
            
            prediction = {'size': size, 'price': price}
    
    return render(request, 'predictor/home.html', {
        'form': form,
        'prediction': prediction
    })

def predict_price(size):
    """Make a prediction using the loaded model"""
    size_reshaped = np.array([[float(size)]])
    price = model.predict(size_reshaped)[0]
    return round(price, 2)
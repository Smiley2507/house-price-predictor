# house-price-predictor
# House Price Predictor

A Django web application that predicts house prices based on house size using a linear regression model.

## Features

- Simple form interface for entering house size
- Real-time price prediction
- Stores prediction history in a database

## Technologies Used

- Django 5.2
- scikit-learn
- pandas
- numpy
- Bootstrap 5

## Installation

1. Clone the repository
`git clone https://github.com/YOUR-USERNAME/house-price-predictor.git`
`cd house-price-predictor`

2. Install dependencies
`pip install -r requirements.txt`
3. Run migrations
`python manage.py makemigrations`
`python manage.py migrate`

4. Start the development server
`python manage.py runserver`

5. Visit http://127.0.0.1:8000/ in your browser

## Model Information

The linear regression model was trained on housing data with the following features:
- House size (square feet)

## Screenshot

<table>
  <tr>
    <td><img src="house_price_predictor.png" width="800"/></td>
  </tr>
</table>


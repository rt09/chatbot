from django.shortcuts import render
from .models import customer, product
from django.http import JsonResponse
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



# Create a ChatterBot instance
chatbot = ChatBot('ChatterBot')

# Train the bot with some example conversation data
trainer = ListTrainer(chatbot)
trainer.train([
    'How long have I been a customer of your bank?',
    'I am sorry, I am not authorized to share that information. Please provide your name and account number to verify your identity.',
    'What other products should I invest in with you?',
    'We offer a variety of investment options, including mutual funds, stocks, and bonds. Please visit our website for more information.',
    'How many planets are there?',
    'There are eight planets in our solar system.',
    'How far is the moon from the Earth?',
    'The average distance between the moon and the Earth is about 238,855 miles.',
])

@csrf_exempt
def get_response(request):
    message=''
    if request.method == 'POST':
        message = request.POST.get('input', '').strip()
        print(message)
        if 'account balance' in message.lower():
            # Retrieve the customer's account balance from the database
            try:
                Customer = customer.objects.get(cust_fname='Carlos')
            except Customer.DoesNotExist:
                import traceback
                traceback.print_exc()
                response = 'I am sorry, I could not find your account information. Please provide your name and account number to verify your identity.'
            else:
                balance = Customer.ac_balance
                response = 'Your account balance is {}.'.format(balance)
        elif 'customer' in message.lower() and 'long' in message.lower() and 'been' in message.lower():
            # Retrieve the customer's account open date from the database
            try:
                Customer = customer.objects.get(cust_fname='Carlos')
            except Customer.DoesNotExist:
                import traceback
                traceback.print_exc()
                response = 'I am sorry, I could not find your account information. Please provide your name and account number to verify your identity.'
            else:
                open_date = Customer.ac_opening_date
                response = 'You have been a customer of our bank since {}.'.format(open_date)
        # elif 'products' in message.lower() and 'invest' in message.lower():
        #     # Retrieve the cross-sell products from the database
        #     try:
        #         product = Product.objects.get(name='Investment')
        #     except Product.DoesNotExist:
        #         response = 'I am sorry, I could not find any investment products at this time. Please check back later.'
        #     else:
        #         cross_sell = product.cross_sell
        #         response = 'We recommend investing in the following products: {}.'.format(cross_sell)
        else:
            # Use the ChatterBot to generate a generic response
            response = chatbot.get_response(message).text

        # Return the response to the user as a JSON object
        return JsonResponse({'status': 'OK', 'output': response},safe=False)
    else:
        return(request,'index.html')

def index(request):
    return render(request,'index.html')

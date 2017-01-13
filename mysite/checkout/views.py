from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
	if request.method == 'POST':
		publishKey = settings.STRIPE_PUBLISHABLE_KEY 
		token = request.POST['stripeToken']
		# Create a charge: this will charge the user's card
		try:
		  charge = stripe.Charge.create(
			  amount=1000, # Amount in cents
			  currency="usd",
			  source=token,
			  description="Example charge"
		  )
		except stripe.error.CardError as e:
		  # The card has been declined
		  pass
	context = { 'publishKey': publishKey}
	template = 'checkout.html'
	return render(request,template,context)


	
	
	
# Create your views here.

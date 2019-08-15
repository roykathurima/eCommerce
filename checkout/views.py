from django.shortcuts import render

# Daraja requirement imports
import requests
from requests.auth import HTTPBasicAuth
from M2Crypto import RSA, X509
from base64 import b64encode
# Personal Notes and perspective on the matter
# the app should be able to interact with Safaricom Daraja; Hopefully :)
# the methods have been written from how they were copied from the documentation,
# they can however been combined based on the logic of the program or as necessary
# some of the methods defined initially might only need to be run once maybe by the admin
# some functionality such as mpesa balance is irrelevant as all we need to do is implement
# a payment system for the customers

# Also, make global variables of parameters that are re_used, maybe even define them in settings.py
# beware however some change depending on the request type even if the name is similar
# To authenticate my app and get an Oauth access token, use the auth code copied

# Consider making the keys global variables as they are static

def get_token(request):
	consumer_key = "FsYY44Y1JE3zRlQqnYDvkmBqcNh3DusA"
	consumer_secret = "0vnVjCfXWfmsNzy0"
	api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
	r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
	print (r.text)

def get_security_creds(request):
	INITIATOR_PASS = "YOUR_PASSWORD"
	CERTIFICATE_FILE = "PATH_TO_CERTIFICATE_FILE"
	def encryptInitiatorPassword():
		cert_file = open(CERTIFICATE_FILE, 'r')
		cert_data = cert_file.read() #read certificate file
		cert_file.close()
		cert = X509.load_cert_string(cert_data) #pub_key = X509.load_cert_string(cert_data)
		pub_key = cert.get_pubkey()
		rsa_key = pub_key.get_rsa()
		cipher = rsa_key.public_encrypt(INITIATOR_PASS, RSA.pkcs1_padding)
		return b64encode(cipher)
	print encryptInitiatorPassword()

def register(request):
	# import requests
	access_token = "Access-Token"
	api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
	headers = {"Authorization": "Bearer %s" % access_token}
	request = { "ShortCode": " ", 
		"ResponseType": " ", 
		"ConfirmationURL": "http://ip_address:port/confirmation", 
		"ValidationURL": "http://ip_address:port/validation_url"}
	response = requests.post(api_url, json = request, headers=headers)
	print (response.text) 

# c2b simulation
def simulation(request):
	# import requests
	access_token = "ACCESS_TOKEN"
	api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
	headers = {"Authorization": "Bearer %s" % access_token}
	request = { "ShortCode":" ", 
		"CommandID":"CustomerPayBillOnline",
		"Amount":" ", "Msisdn":" ",
		"BillRefNumber":" " }
	response = requests.post(api_url, json = request, headers=headers)
	print (response.text)



# stkPush
# Recommended payment mechanism by safaricom
# Extend it as required
# consider changing the names of functions accordingly for abstraction
# This is probably the only function the user will ever need to call after setup is done
def stk_push(request):
	# import requests
	access_token = "Access-Token"
	api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
	headers = { "Authorization": "Bearer %s" % access_token }
	request = { "BusinessShortCode": " ",
		"BusinessShortCode": " ",
		"Timestamp": " ",
		"TransactionType": "CustomerPayBillOnline",
		"Amount": " ",
		"PartyA": " ",
		"PartyB": " ",
		"PhoneNumber": " ",
		"CallBackURL": "https://ip_address:port/callback",
		"AccountReference": " ",
		"TransactionDesc": " " }
	response = requests.post(api_url, json = request, headers=headers)
	print (response.text)

def confirmation(request):
	# will be called by the mpesa API to confirm details of the transaction
	# Return error code if it did not go well
	pass


def call_back(request):
	# This will be called by the API when they finalize the transaction on their end
	# print whether the transaction went well or otherwise
	# probably store the details of the transaction on the data-base
	pass





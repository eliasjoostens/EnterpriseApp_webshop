from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from VentilatorShop.models.customer import Customer
from django.views import View
import re

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        regexp = re.compile('[$#@!*]')
        if (not customer.first_name):
            error_message = "Gelieve uw voornaam in te vullen!"
        elif len(customer.first_name) < 3:
            error_message = 'Voornaam moet uit minstens 3 karakters bestaan.'
        elif not customer.last_name:
            error_message = 'Gelieve uw familienaam in te vullen!'
        elif len(customer.last_name) < 3:
            error_message = 'Familienaam moet uit minstens 3 karakters bestaan.'
        elif not customer.phone:
            error_message = 'Voer uw telefoonnummer in aub'
        elif len(customer.phone) < 10:
            error_message = 'Telefoonnummer moet bestaan uit 10 cijfers'
        elif len(customer.password) < 9:
            error_message = 'Wachtwoord moet uit minstens 9 karakters bestaan'
        elif not (any(i.isdigit() for i in customer.password)):
            error_message = 'Wachtwoord moet minstens 1 cijfer bevatten'
        elif not (any(i.isupper() for i in customer.password)):
            error_message = 'Wachtwoord moet minstens 1 hoofdletter bevatten'
        elif not (regexp.search(customer.password)):
            error_message = 'Wachtwoord moet minstens 1 speciaal karakter bevatten ($, #, @, !, *)'
        elif len(customer.email) < 5:
            error_message = 'E-mail moet uit minstens 5 karakters bestaan'
        elif customer.isExists():
            error_message = 'E-mail adres reeds geregistreerd als gebruiker!'
        # saving

        return error_message

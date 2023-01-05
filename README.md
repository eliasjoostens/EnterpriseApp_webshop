# Enterprise Applications Assignment Jan '23

De stappen die je dient te ondernemen om uit dit project een werkende webshop te krijgen zijn als volgt:
1. Download Zip
2. Unzip naar gewenste plek
3. Open deze file met jouw favoriete Python IDE (ik gebruik PyCharm)
4. Open Terminal
5. Maak de migratie file aan
-> py manage.py makemigrations
6. Creëer de tabellen in de database
-> py manage.py migrate
7. Laad de voorziene seeding data in (2 bestanden in dit geval, voer deze apart uit)
-> py manage.py loaddata VentilatorShop/seed/0002_category.json
-> py manage.py loaddata VentilatorShop/seed/0003_product.json
8. Maak een superuser aan om de admin functionaliteiten te gebruiken
-> py manage.py createsuperuser
9. Activeer de server, die rekening houdt met de nodige sleutel voor HTTPS verbinding
-> py manage.py runserver_plus --cert-file cert.pem --key-file key.pem
10. Open website door te klikken op het voorziene adres of op je browser te surfen naar
-> https://127.0.0.1:8000/store

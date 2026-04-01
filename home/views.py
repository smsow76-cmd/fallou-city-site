from django.shortcuts import render

from home.models import Bien

# Liste des biens
biens = [
    {'id': 1, 'titre': 'Villa Dakar', 'prix': '150M FCFA', 'details': '5 chambres • Piscine', 'image': 'house1.jpeg'},
    {'id': 2, 'titre': 'Appartement Plateau', 'prix': '80M FCFA', 'details': '3 chambres • Terrasse', 'image': 'house2.jpeg'},
    {'id': 3, 'titre': 'Maison Familiale', 'prix': '95M FCFA', 'details': '4 chambres • Garage', 'image': 'house3.jpeg'},
    {'id': 4, 'titre': 'Villa Liberté', 'prix': '200M FCFA', 'details': '6 chambres • Jardin', 'image': 'house4.jpeg'},
    {'id': 5, 'titre': 'Appartement Moderne', 'prix': '85M FCFA', 'details': '2 chambres • Balcon', 'image': 'house5.jpeg'},
    {'id': 6, 'titre': 'Maison Confort', 'prix': '120M FCFA', 'details': '4 chambres • Piscine', 'image': 'house6.jpeg'},
    {'id': 7, 'titre': 'Villa Prestige', 'prix': '250M FCFA', 'details': '7 chambres • Jardin et Piscine', 'image': 'house7.jpeg'},
    {'id': 8, 'titre': 'Maison Élite', 'prix': '180M FCFA', 'details': '5 chambres • Garage et Jardin', 'image': 'house8.jpeg'},
]

def index(request):
    return render(request, 'index.html', {'biens': biens})

def proprietes(request):
    return render(request, 'proprietes.html', {'biens': biens})

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def detail_propriete(request, id):
    # Trouve le bien correspondant
    bien = next((b for b in biens if biens.index(b) + 1 == id), None)
    if not bien:
        return render(request, '404.html')  # ou renvoyer HttpResponseNotFound()
    return render(request, 'detail.html', {'bien': bien})

def proprietes(request):
    biens = Bien.objects.all()
    q = request.GET.get('q')
    if q:
        biens = biens.filter(titre__icontains=q)
    return render(request, 'proprietes.html', {'biens': biens})




def proprietes(request):
    # Exemple de biens pour tests
    biens = [
        {'id': 1, 'titre': 'Villa Dakar', 'prix': '150M FCFA', 'details': '5 chambres • Piscine', 'image': 'house1.jpeg'},
        {'id': 2, 'titre': 'Appartement Plateau', 'prix': '80M FCFA', 'details': '3 chambres • Terrasse', 'image': 'house2.jpeg'},
        {'id': 3, 'titre': 'Maison Familiale', 'prix': '95M FCFA', 'details': '4 chambres • Garage', 'image': 'house3.jpeg'},
    ]
    return render(request, 'proprietes.html', {'biens': biens})  # Tous les biens depuis la DB

    # Récupère les filtres depuis le formulaire GET
    q = request.GET.get('q')
    prix = request.GET.get('prix')
    type_bien = request.GET.get('type')

    if q:
        biens = biens.filter(titre__icontains=q)

    if prix:
        biens = biens.filter(prix__lte=prix)

    if type_bien:
        biens = biens.filter(type_bien=type_bien)

    return render(request, 'proprietes.html', {'biens': biens})

from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ReclamatiiForm, FacturaForm
from .models import Apartament, FacturiIntretinere, Aviz,  Payment, Locatari, Reclamatii
from weasyprint import HTML
from .forms import WaterMeterReadingForm


def add_water_meter_reading(request):
    if request.method == 'POST':
        form = WaterMeterReadingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_water_meter_reading')
    else:
        form = WaterMeterReadingForm()
    return render(request, 'locatari/add_water_meter_reading.html', {'form': form})


def list_water_meter_reading(request):
    return render(request, 'locatari/list_water_meter_reading.html')


def generate_pdf_response(html_content, filename):
    html = HTML(string=html_content)
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{filename}"'
    return response


def generate_aviz(request, factura_id):
    factura = get_object_or_404(FacturiIntretinere, id=factura_id)
    context = {
        'luna': factura.luna.strftime("%B %Y"),
        'meter_value': factura.contoar_valoare,
        'total_payment': factura.suma_plata,
    }
    html_string = render_to_string('locatari/adauga_aviz.html', context=context).replace('\n', '')
    return generate_pdf_response(html_string, f'aviz_{factura_id}.pdf')


def lista_aviz(request):
    avize = Aviz.objects.all()
    return render(request, 'locatari/lista_avize.html', {'avize': avize})




def reclamatii_list(request):
    reclamatii = Reclamatii.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'locatari/reclamatii_list.html', {'reclamatii': reclamatii})



def submit_reclamatii(request):
    if request.method == 'POST':
        form = ReclamatiiForm(request.POST)
        if form.is_valid():
            reclamatie = form.save(commit=False)
            reclamatie.user = request.user
            reclamatie.save()
            return redirect('reclamatii_list')
    else:
        form = ReclamatiiForm()
    return render(request, 'locatari/submit_reclamatii.html', {'form': form})






def plata_card(request):
    return render(request, 'locatari/plata_card.html')




def about(request):
    return render(request, 'locatari/about.html')


class HomeTemplateView(TemplateView):
    template_name = 'locatari/home.html'


def home(request):
    return render(request, 'locatari/home.html')


class HomeView(TemplateView):
    template_name = 'locatari/home.html'


from django.core.exceptions import ObjectDoesNotExist


def lista_apartamente(request):
    try:
        apartamente = Apartament.objects.all()
    except ObjectDoesNotExist:
        apartamente = None

    context = {
        'apartamente': apartamente
    }

    return render(request, 'locatari/lista_apartamente.html', context)



@staff_member_required
def adauga_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('istoric_facturi')
    else:
        form = FacturaForm()
    return render(request, 'locatari/adauga_facturi.html', {'form': form})


def lista_facturi(request):
    facturi = FacturiIntretinere.objects.all().order_by('-luna')
    return render(request, 'locatari/lista_facturi.html', {'facturi': facturi})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'locatari/signup.html', {'form': form})



def sterge_apartament(request, pk):
    apartament = get_object_or_404(Apartament, id=pk)
    apartament.delete()
    return redirect('lista_apartamente')


def sterge_factura(request, pk):
    factura = get_object_or_404(FacturiIntretinere, id=pk)
    factura.delete()
    return redirect('lista_facturi')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, "locatari/logout.html", {})

def istoric_plati(request):
    user_payments = Payment.objects.filter(user=request.user)


    sorted_payments = user_payments.order_by('-payment_date')

    return render(request, 'locatari/istoric_plati.html', {'payments': sorted_payments})


def list_locatari(request):
    locators = Locatari.objects.all()
    return render(request, 'locatari/locatari_list.html', {'locators': locators})


def lista_apartmente(request):
    apartament = Apartament.objects.all()
    return render(request, 'locatari/lista_apartamente.html', {'apartamente': apartament})
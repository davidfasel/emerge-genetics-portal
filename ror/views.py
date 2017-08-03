from django.shortcuts import render, redirect
from django.http import HttpResponse
from ror.models import Person, Variant
import re, csv

# Create your views here.
def login_page(request):

    if request.method == 'POST':
        return redirect('/home')
        
    return render(request, 'login.html')

    
def refresh_database(request):

    Person.objects.all().delete()
    Variant.objects.all().delete()
    with open('data_files/people.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            Person.objects.create(
                MRN    = row[0],
                name   = row[1],
                DOB    = row[2],
                status = row[3],
                assigned = row[4],
            )
    with open('data_files/variants.csv') as f:
        reader = csv.reader(f)
        for row in reader:
             Variant.objects.create(
                 chromosome   = row[0],
                 position     = row[1],
                 rs_id        = row[2],
                 ref          = row[3],
                 alt          = row[4],
                 gene         = row[5],
                 func_type    = row[6]
             )

    return redirect('/home')
        
     
def home_page(request):
    people = Person.objects.all()#.order_by('status')
    return render(request, 'home.html', {'people' : people})


def patient_summary_page(request):
    mrn = getPatientFromURL(request.path)
    person = Person.objects.filter(MRN = mrn)
    return render(request, 'patient_summary.html', {'person' : person.first()})
    

def patient_report_page(request):
    mrn = getPatientFromURL(request.path)
    person = Person.objects.filter(MRN = mrn)
    return render(request, 'patient_report.html', {'person' : person.first()})

def patient_notes_page(request):
    mrn = getPatientFromURL(request.path)
    person = Person.objects.filter(MRN = mrn)
    return render(request, 'patient_notes.html', {'patient': patient})

def patient_research_page(request):
    mrn = getPatientFromURL(request.path)
    person = Person.objects.filter(MRN = mrn)

    variants = Variant.objects.all()
    if request.method == 'POST' and request.POST['gene']:
        variants = Variant.objects.all().filter(gene__icontains = request.POST['gene'])
        
    return render(request, 'patient_research.html', {'person' : person.first(), 'variants' : variants})

def patient_phenolyzer_page(request):
    mrn = getPatientFromURL(request.path)
    person = Person.objects.filter(MRN = mrn)
    return render(request, 'patient_phenolyzer.html', {'person' : person.first()})
    
    
    
    
def getPatientFromURL(path):
    patient = re.search('/(\d+)/?', path)
    if patient: 
        return patient.group(1)
    else:
        return '999999'
    

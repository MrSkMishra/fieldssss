from django.shortcuts import render
from django.views import View
from .models import *



class HomeView(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        name = request.POST.get('name')
        address = request.POST.get('address')
        age = request.POST.get('age')
        experience = request.POST.get('experience')
        qualification = request.POST.get('qualification')
        user = User.objects.create(
            name=name,
            address=address,
            age=age,
            experience=experience,
            qualification=qualification
        )
        print(name,address,age,experience,qualification)

        company_names = request.POST.getlist('companyName')
        from_dates = request.POST.getlist('fromDate')
        to_dates = request.POST.getlist('toDate')
        
        for i in range(len(company_names)):
            company_data = {
                'user': user,
                'company_name': company_names[i],
                'from_date': from_dates[i],
                'to_date': to_dates[i]
            }
            company = Company(**company_data)
            company.save()

        for i in range(len(company_names)):
            print(f"\nCompany {i+1}:")
            print("Company Name:", company_names[i])
            print("From Date:", from_dates[i])
            print("To Date:", to_dates[i])

        return render(request, "success.html")
def atul(request):
    return render(request,"index_2.html")
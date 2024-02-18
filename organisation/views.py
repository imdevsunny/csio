from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic import View
from organisation.models import FamilyMember, Vehicles, Pets, Harper
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

User = get_user_model()
# Create your views here.


class Home(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        context = {
            "user": request.user,
            "family_member": FamilyMember.objects.filter(resident=request.user),
            "vehicles": Vehicles.objects.filter(resident=request.user),
            "pets": Pets.objects.filter(resident=request.user),
            "harpers": Harper.objects.filter(resident=request.user),
        }
        return render(request, "index.html", context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        if request.POST.get("resident") == "resident":
            house_number = request.POST.get("house_number").rstrip()
            allottee_name = request.POST.get("allottee_name").rstrip()

            user = User.objects.get(id=request.user.id)
            user.house_number = house_number
            user.allottee_name = allottee_name
            user.save()
            messages.info(request, "Resident Updated Successfully!")
            return redirect("home")


        if request.POST.get("family-member") == "family-member":
            name = request.POST.get("name",'').rstrip()
            relation = request.POST.get("relation",'').rstrip()
            age = request.POST.get("age",'').rstrip()
            occupation = request.POST.get("occupation",'').rstrip()
            phone = request.POST.get("phone",'').rstrip()

            if not name or not relation or not age or not occupation or not phone:
                messages.error(request,"All Fields are Mendatory For Family Member!")
                return redirect('home')

            FamilyMember.objects.create(
                name=name,
                relation=relation,
                age=age,
                occupation=occupation,
                phone=phone,
                resident=request.user,
            )
            messages.info(request, "Family Member Added Successfully!")
            return redirect("home")
        
        
        if request.POST.get("vehicle") == "vehicle":
            vehicle = request.POST.get("name",'').rstrip()
            make = request.POST.get("make",'').rstrip()
            registration_no = request.POST.get("registration_no",'').rstrip()
            use = request.POST.get("use",'').rstrip()
            sticker = request.POST.get("sticker",'').rstrip()

            if not vehicle or not make or not registration_no or not use or not sticker:
                messages.error(request,"All Fields are Mendatory For Vehicle!")
                return redirect('home')

            if sticker.lower()=='yes':
                sticker=True
            else:
                sticker=False

            Vehicles.objects.create(
                vehicle=vehicle,
                make=make,
                registration_no=registration_no,
                use=use,
                sticker=sticker,
                resident=request.user,
            )
            messages.info(request, "Vehicle Added Successfully!")
            return redirect("home")
        
        
        if request.POST.get("pet") == "pet":
            name = request.POST.get("name",'').rstrip()
            registered = request.POST.get("registered",'').rstrip()
            registration_no = request.POST.get("registration_no",'').rstrip()

            if not name or not registered or not registration_no:
                messages.error(request,"All Fields are Mendatory For Pet!")
                return redirect('home')

            if registered.lower()=='yes':
                registered=True
            else:
                registered=False

            Pets.objects.create(
                name=name,
                registered=registered,
                registration_no=registration_no,
                resident=request.user,
            )
            messages.info(request, "Pet Added Successfully!")
            return redirect("home")
        

        if request.POST.get("harper") == "harper":
            name = request.POST.get("name",'').rstrip()
            address = request.POST.get("address",'').rstrip()
            police_verification = request.POST.get("police_verification",'').rstrip()
            contact = request.POST.get("contact",'').rstrip()

            if not name or not address or not police_verification or not contact:
                messages.error(request,"All Fields are Mendatory For Harper!")
                return redirect('home')

            if police_verification.lower()=='yes':
                police_verification=True
            else:
                police_verification=False

            Harper.objects.create(
                name=name,
                address=address,
                police_verification=police_verification,
                contact=contact,
                resident=request.user,
            )
            messages.info(request, "Harper Added Successfully!")
            return redirect("home")

        return render(request, "index.html", {})


class DeleteMember(View):
    @method_decorator(login_required)
    def get(self, request, pk):

        FamilyMember.objects.get(pk = pk).delete()

        messages.info(request,"Member Deleted Successfully!")

        return redirect('home')
    
    
class DeleteVehicle(View):
    @method_decorator(login_required)
    def get(self, request, pk):

        Vehicles.objects.get(pk = pk).delete()

        messages.info(request,"Vehicle Deleted Successfully!")

        return redirect('home')
    
    
class DeletePet(View):
    @method_decorator(login_required)
    def get(self, request, pk):

        Pets.objects.get(pk = pk).delete()

        messages.info(request,"Pet Deleted Successfully!")

        return redirect('home')
    

class DeleteHarper(View):
    @method_decorator(login_required)
    def get(self, request, pk):

        Harper.objects.get(pk = pk).delete()

        messages.info(request,"Harper Deleted Successfully!")

        return redirect('home')
    

class CancelView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        messages.info(request,"Operation Cancelled Successfully!")

        return redirect('home')
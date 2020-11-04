from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CitasMedicas.models import Persona, Consultorio, Estado
from CitasMedicas.serializers import PersonaSerializer, ConsultorioSerializer, EstadoSerializer 



# Create your views here.
@csrf_exempt
def personaApi(request,id=0):
    if request.method=='GET':
        persona = Persona.objects.all()
        persona_serializer = PersonaSerializer(persona, many=True)
        return JsonResponse(persona_serializer.data, safe=False)

    elif request.method=='POST':
        persona_data=JSONParser().parse(request)
        persona_serializer = PersonaSerializer(data=persona_data)
        if persona_serializer.is_valid():
            persona_serializer.save()
            return JsonResponse("Agregó Exitosamente!!" , safe=False)
        return JsonResponse("Falló al agregar.",safe=False)
    
    elif request.method=='PUT':
        persona_data = JSONParser().parse(request)
        persona=Persona.objects.get(cod_per=persona_data['cod_per'])
        persona_serializer=PersonaSerializer(persona,data=persona_data)
        if persona_serializer.is_valid():
            persona_serializer.save()
            return JsonResponse("Actualización Exitosa!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        persona=Persona.objects.get(cod_per=id)
        persona.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def consultorioApi(request,id=0):
    if request.method=='GET':
        consultorio = Consultorio.objects.all()
        consultorio_serializer = ConsultorioSerializer(consultorio, many=True)
        return JsonResponse(consultorio_serializer.data, safe=False)

    elif request.method=='POST':
        consultorio_data=JSONParser().parse(request)
        consultorio_serializer = ConsultorioSerializer(data=consultorio_data)
        if consultorio_serializer.is_valid():
            consultorio_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        consultorio_data = JSONParser().parse(request)
        consultorio=Consultorio.objects.get(cod_con=consultorio_data['cod_con'])
        consultorio_serializer=ConsultorioSerializer(consultorio,data=consultorio_data)
        if consultorio_serializer.is_valid():
            consultorio_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        consultorio=Consultorio.objects.get(cod_con=id)
        consultorio.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
from django.shortcuts import render
from rest_framework.views import APIView
from eaf_app.serilizers import (
    ChemicalCompositonSerilizer,
    ChemicalElementSerilizer,
    CommodityPropertiesSerilizer,
)
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from eaf_app.models import ChemicalElement, ChemicalCompositon, CommodityProperties
from rest_framework.response import Response
from rest_framework import status, generics
import json


def update_percentage(pk):
    SomeModel_json = ChemicalCompositon.objects.filter(commodity=pk)
    if SomeModel_json is not None:
        current_value = {}
        new_json = {}
        for i in SomeModel_json:
            element_name = ChemicalElement.objects.get(pk=i.element.id)
            percentage = i.percentage
            current_value[element_name.name] = percentage
        if "unknown" not in current_value.keys():
            create_unknown = ChemicalElement.objects.get_or_create(name="unknown")
            unknown_id = create_unknown[0].id
            total_value = 0
            for value in current_value.values():
                print(value)
                total_value = total_value + value
            new_json["percentage"] = 100 - total_value
            new_json["commodity"] = pk
            new_json["element"] = unknown_id
            chem_com_serializer = ChemicalCompositonSerilizer(data=new_json)
            if chem_com_serializer.is_valid():
                chem_com_serializer.save()
        else:
            total_value = 0
            unknown_id = ChemicalElement.objects.get(name="unknown")
            chemical_composition_id = ChemicalCompositon.objects.get(
                element=unknown_id, commodity=pk
            )
            for key, value in current_value.items():
                if key != "unknown":
                    total_value = total_value + value
            chemical_composition_id.percentage = 100 - total_value
            chemical_composition_id.save()
    return True

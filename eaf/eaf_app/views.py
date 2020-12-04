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
from .utils import update_percentage

# Create your views here.
class chemicalElement(APIView):
    def get(self, request, format=None):
        chem_element = ChemicalElement.objects.all()
        serializer = ChemicalElementSerilizer(chem_element, many=True)
        return Response(serializer.data)


# class ChemicalCompositonView(APIView):
#     def get(self, request, format=None):
#         chem_element1 = ChemicalCompositon.objects.all()
#         serializer = ChemicalCompositonSerilizer(chem_element1, many=True)
#         return Response(serializer.data)


class commodityPropertiesView(APIView):
    def get(self, request, format=None):
        chem_element = CommodityProperties.objects.all()
        serializer = CommodityPropertiesSerilizer(chem_element, many=True)
        return Response(serializer.data)


class commodityPropertiesDetails(APIView):
    """
    Retrieve, update a commodity instance.
    """

    def get_object(self, pk):
        try:
            return CommodityProperties.objects.get(pk=pk)
        except CommodityProperties.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        commodity = self.get_object(pk)
        serializer = CommodityPropertiesSerilizer(commodity)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = CommodityPropertiesSerilizer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return JsonResponse(serializer.data, safe=False)


class chemicalCompositionView(APIView):
    def post(self, request):
        commodity_id = request.data["commodity"]
        element_id = request.data["element"]
        composition_id = ChemicalCompositon.objects.filter(
            element=element_id, commodity=commodity_id
        )
        if composition_id:
            for composition in composition_id:
                composition.percentage = request.data["percentage"]
                composition.save()
            output_status = {
                "Status": status.HTTP_200_OK,
                "Message": "Updated existing composition",
            }
        else:
            chem_com_serializer = ChemicalCompositonSerilizer(data=request.data)
            if chem_com_serializer.is_valid():
                chem_com_serializer.save()
            else:
                print(chem_com_serializer.errors)
            output_status = {
                "Status": status.HTTP_200_OK,
                "Message": "New composition created",
            }
        percentage_change = update_percentage(commodity_id)
        return JsonResponse({"Status": "Ok", "Percentage_Updated": percentage_change})

    def put(self, request):
        commodity_id = request.data["commodity"]
        element_id = request.data["element"]
        chemical_composition_id = ChemicalCompositon.objects.filter(
            element=element_id, commodity=commodity_id
        )
        if chemical_composition_id:
            chemical_composition_id.delete()
            percentage_change = update_percentage(commodity_id)
            output_status = {
                "Status": status.HTTP_200_OK,
                "Message": "Deleted composition",
            }
        else:
            output_status = {
                "Status": status.HTTP_404_NOT_FOUND,
                "Message": "Composition not Found",
            }
        return Response({"Status": output_status})

from rest_framework import serializers
from eaf_app.models import ChemicalCompositon, ChemicalElement, CommodityProperties


class ChemicalElementSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalElement
        fields = "__all__"


class ChemicalCompositonSerilizer(serializers.ModelSerializer):
    elements = ChemicalElementSerilizer(read_only=True)

    class Meta:
        model = ChemicalCompositon
        fields = ["percentage", "elements", "commodity", "element"]

    # def create(self, validated_data):


class CommodityPropertiesSerilizer(serializers.ModelSerializer):
    chemical_composition = ChemicalCompositonSerilizer(many=True, read_only=True)

    class Meta:
        model = CommodityProperties
        fields = ["id", "name", "price", "inventory", "chemical_composition"]

        def update(self, instance, validated_data):
            instance.name = validated_data.get("name", instance.name)
            instance.price = validated_data.get("price", instance.price)
            return instance


# class ChecmicalElementSerilizer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)

#     class Meta:
#         model = ChemicalElement
#         fields = '__all__'


# class ChemicalCompositonSerilizer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)

#     class Meta:
#         model = ChemicalCompositon
#         fields = "__all__"

# class CommodityPropertiesSerilizer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False,read_only=True)
#     chemical_composition = ChemicalCompositonSerilizer(many=True)

#     class Meta:
#         model = CommodityProperties
#         fields = ['id','name', 'price', 'inventory','chemical_composition']
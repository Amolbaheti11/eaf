from django.urls import path
from eaf_app.views import (
    chemicalElement,
    commodityPropertiesDetails,
    # ChemicalCompositonView,
    commodityPropertiesView,
    chemicalCompositionView,
)


urlpatterns = [
    path("chemicalElements", chemicalElement.as_view()),
    path("commodityProperties/<int:pk>", commodityPropertiesDetails.as_view()),
    path("chemicalcomposition/<int:pk>/", chemicalCompositionView.as_view()),
    # path("chemicalElementst", ChemicalCompositonView.as_view()),
    path("commodityproperty", commodityPropertiesDetails.as_view()),
    path("chemicalcomposition", chemicalCompositionView.as_view()),
]

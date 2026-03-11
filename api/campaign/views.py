from rest_framework import status, viewsets,permissions
from .models import MstCampaignTypes, MstCampaignTeamRole,MstThirdPartyTypes,MstThirdParties,CmpCampaigns,CmpCampaignUserGeoCoverage,CmpWaves,MstQAReviewProcedure,CmpTeam,SysPersonalizationTags,CmpCampaignScripts,CmpCampaignGeoCoverage,CmpSegment,CmpSegmentSize,CmpCampaignXChannels,CmpCallerCredentials,CmpEmail
from .serializer import MstCampaignTypesSerializer, MstCampaignTeamRoleSerializer,MstThirdPartyTypesCreateUpdateSerializer,MstThirdPartyTypesSerializer,MstThirdPartiesSerializer,CmpCampaignsSerializer,CmpCampaignUserGeoCoverageSerializer,CmpWavesSerializer,QAReviewProcedureSerializer,CmpTeamSerializer,SysPersonalizationTagsSerializer,CmpCampaignScriptsSerializer,MstActiveCampaignTypesSerializer,MstActiveThirdPartyTypesSerializer,MstActiveThirdPartiesSerializer,ActiveCmpCampaignsSerializer,ActiveCmpWavesSerializer,CmpCampaignGeoCoverageSerializer,CmpSegmentsSerializer,CmpSegmentSizeSerializer,CmpCampaignXChannelsSerializer,MstActiveCampaignTeamRoleSerializer,CmpCallerCredentialsSerializer,CmpEmailSerializer,CmpTeamsSerializer

from utils.services.responses import success_response,error_response  # adjust path if needed
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status


class MstCampaignTypesViewSet(viewsets.ModelViewSet):
    menu_id = 18
    queryset = MstCampaignTypes.objects.all()
    serializer_class = MstCampaignTypesSerializer
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        data = self.get_serializer(self.get_queryset(), many=True).data
        return success_response(
            message="Campaign types fetched successfully",
            data=data,
            status_code=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(
            message="Campaign type created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.get_serializer(instance).data
        return success_response(
            message="Campaign type retrieved successfully",
            data=data,
            status_code=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(
            message="Campaign type updated successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return success_response(
            message="Campaign type deleted successfully",
            data=None,
            status_code=status.HTTP_204_NO_CONTENT
        )
    @action(detail=False,methods=["get"],url_path="active-campaigntypes")
    def activecampaignType(self,request):
        try:
          queryset=MstCampaignTypes.objects.filter(cod_rec_status='A')
          serializer=MstActiveCampaignTypesSerializer(queryset,many=True)
          return success_response("active campaigntypes retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstCampaignTypesSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



class MstCampaignTeamRoleViewSet(viewsets.ModelViewSet):
    menu_id = 19
    queryset = MstCampaignTeamRole.objects.all()
    serializer_class = MstCampaignTeamRoleSerializer
    # permission_classes = [IsAuthenticated]
    

    def list(self, request, *args, **kwargs):
        data = self.get_serializer(self.get_queryset(), many=True).data
        return success_response(
            message="Campaign team roles fetched successfully",
            data=data,
            status_code=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(
            message="Campaign team role created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.get_serializer(instance).data
        return success_response(
            message="Campaign team role retrieved successfully",
            data=data,
            status_code=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(
            message="Campaign team role updated successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return success_response(
            message="Campaign team role deleted successfully",
            data=None,
            status_code=status.HTTP_204_NO_CONTENT
        )
    @action(detail=False,methods=["get"],url_path="active-campaign-team-role")
    def activeCampaignTeamRole(self,request):
        try:
          queryset= MstCampaignTeamRole.objects.filter(cod_rec_status='A')
          serializer=MstActiveCampaignTeamRoleSerializer(queryset,many=True)
          return success_response("active campaign-team-role retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class MstThirdPartyTypesViewSet(BaseModelViewSet):
    menu_id = 14
    queryset = MstThirdPartyTypes.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return MstThirdPartyTypesCreateUpdateSerializer
        return MstThirdPartyTypesSerializer
    
    @action(detail=False,methods=["get"],url_path="active-thirtpartytypes")
    def activeThirdPartyType(self,request):
        try:
          queryset=MstThirdPartyTypes.objects.filter(cod_rec_status='A')
          serializer=MstActiveThirdPartyTypesSerializer(queryset,many=True)
          return success_response("active thirdpartytypes retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstThirdPartyTypesCreateUpdateSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class MstThirdPartiesViewSet(BaseModelViewSet):
    menu_id = 15
    queryset = MstThirdParties.objects.prefetch_related('departments')
    serializer_class = MstThirdPartiesSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-thirtparty")
    def activeThirdParty(self,request):
        try:
          queryset=MstThirdParties.objects.filter(cod_rec_status='A')
          serializer=MstActiveThirdPartiesSerializer(queryset,many=True)
          return success_response("active thirdparty retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @swagger_auto_schema(
        consumes=["application/json", "multipart/form-data"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        consumes=["application/json", "multipart/form-data"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        consumes=["application/json", "multipart/form-data"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstThirdPartiesSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CmpCampaignsViewSet(BaseModelViewSet):
    menu_id = 35
    queryset = CmpCampaigns.objects.all()
    serializer_class = CmpCampaignsSerializer
    # permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    @action(detail=False,methods=["get"],url_path="active-campaigns")
    def activeCampaigns(self,request):
        try:
          queryset=CmpCampaigns.objects.filter(cod_rec_status='A')
          serializer=ActiveCmpCampaignsSerializer(queryset,many=True)
          return success_response("active campaigns retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        consumes=["application/json", "multipart/form-data"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        consumes=["application/json", "multipart/form-data"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        consumes=["application/json", "multipart/form-data"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = CmpCampaignsSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CmpCampaignUserGeoCoverageViewSet(BaseModelViewSet):
    menu_id = 45
    queryset=CmpCampaignUserGeoCoverage.objects.all()
    serializer_class=CmpCampaignUserGeoCoverageSerializer
    # permission_classes=[IsAuthenticated]

class CmpWavesViewSet(BaseModelViewSet):
    menu_id = 58
    # permission_classes=[IsAuthenticated]
    queryset=CmpWaves.objects.all()
    serializer_class=CmpWavesSerializer

    @swagger_auto_schema(
        method="get",
        operation_summary="Fetch Waves by campaign ID",
        operation_description="Returns Waves records using integer id_campaign.",
        manual_parameters=[
            openapi.Parameter(
                name="id_campaign",
                in_=openapi.IN_PATH,
                description="Campaign ID (integer)",
                type=openapi.TYPE_INTEGER,
                required=True,
                example=5
            )
        ],
        responses={
            200: CmpWavesSerializer(many=True),
            404: "No records found"
        },
        tags=["SecUserRoleMenus"]
    )
    @action(
        methods=["get"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path=r"fetch-by-id_campaign/(?P<id_campaign>\d+)"
    )
    def fetch_by_campaign_id(self, request, id_campaign=None):

        try:
            queryset = CmpWaves.objects.filter(
                id_campaign=id_campaign,
                cod_rec_status="A"
            )

            if not queryset.exists():
                return error_response(
                    "No records found for this campaign id",
                    status_code=status.HTTP_404_NOT_FOUND
                )

            serializer = self.get_serializer(queryset,many=True)

            return success_response(
                message="Records fetched successfully",
                data=serializer.data,
                status_code=status.HTTP_200_OK
            )

        except Exception as e:
            return error_response(
                "Internal server error",
                errors=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False,methods=["get"],url_path="active-waves")
    def activeWaves(self,request):
        try:
          queryset=CmpWaves.objects.filter(cod_rec_status='A')
          serializer=ActiveCmpWavesSerializer(queryset,many=True)
          return success_response("active waves retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = CmpWavesSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class QAReviewProcedureListView(generics.GenericAPIView):
    serializer_class = QAReviewProcedureSerializer

    qa_review_procedure_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "status": openapi.Schema(type=openapi.TYPE_STRING, example="success"),
        "message": openapi.Schema(
            type=openapi.TYPE_STRING,
            example="QA Review procedures fetched successfully"
        ),
        "status_code": openapi.Schema(type=openapi.TYPE_INTEGER, example=200),
        "data": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "id_proc": openapi.Schema(
                        type=openapi.TYPE_INTEGER, example=1
                    ),
                    "txt_proc_name": openapi.Schema(
                        type=openapi.TYPE_STRING, example="proc_validate_lead"
                    )
                }
            )
        )
    }
)


    @swagger_auto_schema(
        operation_summary="List QA Review Procedures",
        operation_description=(
            "Returns a list of QA review stored procedures "
            "eligible for QA execution."
        ),
        responses={
            200: qa_review_procedure_response,
            500: openapi.Response(
                description="Internal Server Error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "status": openapi.Schema(
                            type=openapi.TYPE_STRING, example="error"
                        ),
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            example="Failed to fetch QA Review procedures"
                        ),
                        "status_code": openapi.Schema(
                            type=openapi.TYPE_INTEGER, example=500
                        ),
                        "errors": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            example="Database error"
                        )
                    }
                )
            )
        },
        tags=["QA Review"]
    )

    def get(self, request):
        try:
            queryset = MstQAReviewProcedure.objects.order_by("txt_proc_name")
            serializer = self.get_serializer(queryset, many=True)

            return success_response(
                message="QA Review procedures fetched successfully",
                data=serializer.data,
                status_code=status.HTTP_200_OK
            )

        except Exception as e:
            return error_response(
                message="Failed to fetch QA Review procedures",
                errors=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class CmpTeamViewSet(BaseModelViewSet):
    menu_id = 41
    queryset = CmpTeam.objects.all()
    serializer_class = CmpTeamSerializer

    @swagger_auto_schema(
        method="get",
        operation_summary="Fetch Teams by campaign ID",
        operation_description="Returns Teams records using integer id_campaign.",
        manual_parameters=[
            openapi.Parameter(
                name="id_campaign",
                in_=openapi.IN_PATH,
                description="Campaign ID (integer)",
                type=openapi.TYPE_INTEGER,
                required=True,
                example=5
            )
        ],
        responses={
            200: CmpTeamsSerializer(many=True),
            404: "No records found"
        },
        tags=["CmpTeam"]
    )
    @action(
        methods=["get"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path=r"fetch-by-id_campaign/(?P<id_campaign>\d+)"
    )
    def fetch_by_campaign_id(self, request, id_campaign=None):

        try:
            queryset = CmpTeam.objects.filter(
                id_campaign=id_campaign,
                cod_rec_status="A"
            )

            if not queryset.exists():
                return error_response(
                    "No records found for this campaign id",
                    status_code=status.HTTP_404_NOT_FOUND
                )

            serializer = CmpTeamsSerializer(queryset,many=True)

            return success_response(
                message="Records fetched successfully",
                data=serializer.data,
                status_code=status.HTTP_200_OK
            )

        except Exception as e:
            return error_response(
                "Internal server error",
                errors=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    # permission_classes = [IsAuthenticated]

class SysPersonalizationTagsViewSet(BaseModelViewSet):
    menu_id = 42
    serializer_class = SysPersonalizationTagsSerializer
    queryset =SysPersonalizationTags.objects.all()
    # permission_classes = [IsAuthenticated]

class CmpCampaignScriptsViewSet(BaseModelViewSet):
    menu_id = 43
    serializer_class = CmpCampaignScriptsSerializer
    queryset=CmpCampaignScripts.objects.all()
    # permission_classes = [IsAuthenticated]

class CmpCampaignGeoCoverageViewSet(BaseModelViewSet):
    menu_id = 59
    serializer_class=CmpCampaignGeoCoverageSerializer
    queryset=CmpCampaignGeoCoverage.objects.all()
    # permission_classes=[IsAuthenticated]

class CmpSegmentViewSet(BaseModelViewSet):
    # menu_id = 7
    serializer_class=CmpSegmentsSerializer
    queryset=CmpSegment.objects.all()
    # permission_classes=[IsAuthenticated]

class CmpSegmentSizeViewSet(BaseModelViewSet):
    # menu_id = 7
    serializer_class=CmpSegmentSizeSerializer
    queryset=CmpSegmentSize.objects.all()
    # permission_classes=[IsAuthenticated]

class CmpCampaignXChannelsViewSet(BaseModelViewSet):
    # menu_id = 7
    serializer_class=CmpCampaignXChannelsSerializer
    queryset=CmpCampaignXChannels.objects.all()
    # permission_classes=[IsAuthenticated]

class CmpCallerCredentialsViewSet(BaseModelViewSet):
    # menu_id = 7
    queryset = CmpCallerCredentials.objects.all()
    serializer_class = CmpCallerCredentialsSerializer
    # permission_classes=[IsAuthenticated]
class CmpEmailViewSet(BaseModelViewSet):
    queryset = CmpEmail.objects.all()
    serializer_class = CmpEmailSerializer
    permission_classes = [IsAuthenticated]
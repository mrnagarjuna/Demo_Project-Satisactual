from rest_framework import serializers
from .models import MstCampaignTypes,MstCampaignTeamRole,MstThirdPartyTypes,MstThirdParties,CmpCampaigns,CmpCampaignUserGeoCoverage,CmpWaves,MstQAReviewProcedure,CmpTeam,SysPersonalizationTags,CmpCampaignScripts,CmpCampaignGeoCoverage,CmpSegment,CmpSegmentSize,CmpCampaignXChannels,CmpEmail
from ..masters.serializers.mstdepartment_serializer import MstDepartmentsSerializer

class MstCampaignTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCampaignTypes
        fields = "__all__"

class MstActiveCampaignTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCampaignTypes
        fields=["id",'cod_campaign_type','txt_campaign_type_desc']
        read_only_fields = ["id",'cod_campaign_type','txt_campaign_type_desc']

class MstCampaignTeamRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCampaignTeamRole
        fields = '__all__'

class MstThirdPartyTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstThirdPartyTypes
        fields = '__all__'

class MstActiveThirdPartyTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstThirdPartyTypes
        fields=["id",'cod_third_party_type','txt_third_party_type_desc']
        read_only_fields = ["id",'cod_third_party_type','txt_third_party_type_desc']
    
class MstThirdPartyTypesCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstThirdPartyTypes
        exclude = ('dat_last_maker', 'dat_last_checker')

class MstThirdPartiesSerializer(serializers.ModelSerializer):
    departments = MstDepartmentsSerializer(many=True, read_only=True)
    class Meta:
        model = MstThirdParties
        fields = '__all__'

class MstActiveThirdPartiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstThirdParties
        fields=['id_third_party','txt_third_party_name','txt_third_party_short_name']
        read_only_fields = ['id_third_party','txt_third_party_name','txt_third_party_short_name']

class CmpCampaignsSerializer(serializers.ModelSerializer):
    bin_logo_to_display = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = CmpCampaigns
        fields = "__all__"

class ActiveCmpCampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpCampaigns
        fields=['txt_campaign_name','txt_campaign_short_code','id']
        read_only_fields = ['txt_campaign_name','txt_campaign_short_code','id']

        
        
class CmpCampaignUserGeoCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model=CmpCampaignUserGeoCoverage
        fields="__all__"

class CmpWavesSerializer(serializers.ModelSerializer):
    class Meta:
        model=CmpWaves
        fields="__all__"

class ActiveCmpWavesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpWaves
        fields=['txt_campaign_wave_name','id']
        read_only_fields = ['txt_campaign_wave_name','id']

class QAReviewProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstQAReviewProcedure
        fields = ["id_proc", "txt_proc_name"]

class CmpTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=CmpTeam
        fields="__all__"

class CmpTeamsSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="txt_login_id.txt_login_id",
        read_only=True
    )

    name = serializers.CharField(
        source="txt_login_id.txt_user_fname",
        read_only=True
    )

    parent_company = serializers.CharField(
        source="txt_login_id.txt_parent_company_name",
        read_only=True
    )

    class Meta:
        model = CmpTeam
        fields = [
            "id",
            "id_campaign",
            "txt_login_id",
            "username",
            "name",
            "parent_company",
            "cod_campaign_role",
            "txt_campaign_role",
            "dat_joined_team",
            "dat_left_team",
            "flg_administrator",
            "flg_caller_role",
            "flg_allow_response_submit",
            "cod_rec_status",
        ]

class SysPersonalizationTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysPersonalizationTags
        fields = "__all__"

class CmpCampaignScriptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpCampaignScripts
        fields = "__all__"

class CmpCampaignGeoCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model =CmpCampaignGeoCoverage
        fields="__all__"

class CmpSegmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CmpSegment
        fields = "__all__"

class CmpSegmentSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpSegmentSize
        fields = "__all__"

class CmpCampaignXChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpCampaignXChannels
        fields = "__all__"

class MstActiveCampaignTeamRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCampaignTeamRole
        fields=["id",'cod_team_role','txt_role_name']
        read_only_fields = ["id",'cod_team_role','txt_role_name']


from .models import CmpCallerCredentials


class CmpCallerCredentialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CmpCallerCredentials
        fields = "__all__"
class CmpEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpEmail
        fields = "__all__"
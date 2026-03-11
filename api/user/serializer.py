from rest_framework import serializers
from .models import SecUserMaster,SecUserAccessLog
from ..campaign.serializer import MstThirdPartiesSerializer,MstActiveThirdPartiesSerializer
from ..campaign.models import MstThirdParties


class SecUserMasterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    id_parent_company_3rdparty = serializers.PrimaryKeyRelatedField(
        queryset=MstThirdParties.objects.all(),
        required=False,
        allow_null=True
    )

    # ✅ Return full object in response
    # parent_company = MstActiveThirdPartiesSerializer(
    #     source="id_parent_company_3rdparty",
    #     read_only=True
    # )
    class Meta:
        model = SecUserMaster
        fields = [
            "id",
             "password",
             "last_login",
             "txt_login_id",
             "flg_functional_id",
             "flg_force_passwd_chg",
             "dat_last_passwd_chg",
             "txt_user_fname",
             "txt_user_mname",
             "txt_user_lname",
             "enu_user_gender",
             "dat_user_birth",
             "id_parent_company_3rdparty",
             "txt_parent_company_name",
             "flg_parent_company_verified",
             "dat_time_parent_company_verified",
             "txt_parent_company_verified_by",
             "is_superuser",
             "is_staff",
             "is_enduser",
             "is_client",
             "is_verified",
             "is_pass_changed",
             "is_2fa",
             "is_active",
             "is_deleted",
             "txt_employee_id",
             "cod_language",
             "txt_user_email_id",
             "txt_user_mobile_phone",
             "txt_device_assigned",
             "txt_fcm_token",
             "dat_time_fcm_expiry",
             "cod_home_module",
             "cod_home_menu",
             "dat_time_t_and_c_accepted",
             "dat_time_welcome_dismissed",
             "cod_department",
             "cod_user_designation",
             "cod_credit_officer_level",
             "txt_manager_login_id",
             "txt_default_reviewer_id",
             "txt_credit_approver_id",
             "cod_home_branch",
             "flg_disabled",
             "flg_user_logged_in",
             "dat_last_login",
             "num_failed_pwd",
             "dat_profile_created",
             "dat_profile_expiry",
             "cod_time_zone",
             "cod_2fa_question_1" ,
             "txt_2fa_answer_1",
             "cod_2fa_question_2",
             "txt_2fa_answer_2",
             "cod_2fa_question_3",
             "txt_2fa_answer_3",
             "cod_2fa_question_4",
             "txt_2fa_answer_4",
             "cod_2fa_question_5",
             "txt_2fa_answer_5",
             "cod_rec_status",
             "txt_last_maker_id",
             "dat_last_maker",
             "txt_last_checker_id",
             "dat_last_checker",
            #  "groups",
            #  "user_permissions",
             "created_by",
             "updated_by"
             
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.id_parent_company_3rdparty:
            representation["id_parent_company_3rdparty"] = \
                MstActiveThirdPartiesSerializer(
                    instance.id_parent_company_3rdparty
                ).data

        return representation

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = SecUserMaster(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()

        return instance
    
class SecActiveUserMasterSerializer(serializers.ModelSerializer):
    class Meta:
         model = SecUserMaster
         fields=["id","txt_login_id"]
         read_only_fields = ["id",'txt_login_id']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)





# class SecUserMasterSerializer(serializers.ModelSerializer):
#     txt_user_signature = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = SecUserMasters
#         # Include all fields
#         fields = '__all__'

#     def create(self, validated_data):
#         password = validated_data.pop('txt_user_signature', None)
#         user = SecUserMaster(**validated_data)
#         if password:
#             user.set_password(password)
#         user.save()
#         return user

#     def update(self, instance, validated_data):
#         password = validated_data.pop('txt_user_signature', None)
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         if password:
#             instance.set_password(password)
#         instance.save()
#         return instance
    
# serializers.py
from rest_framework import serializers
from .models import SecUserPreferences, SecUserMaster

class SecUserPreferencesSerializer(serializers.ModelSerializer):
    # Optionally, you can show related user's login ID instead of full object
    txt_login_id = serializers.PrimaryKeyRelatedField(
        queryset=SecUserMaster.objects.all()
    )

    class Meta:
        model = SecUserPreferences
        fields = '__all__'

class SecUserAccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecUserAccessLog
        fields = "__all__"
from .models import SecUserPswdHist

class SecUserPswdHistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecUserPswdHist
        exclude = ["txt_user_signature"]  # do NOT expose password hashes
        
class SecUserPswdHistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecUserPswdHist
        fields = "__all__"



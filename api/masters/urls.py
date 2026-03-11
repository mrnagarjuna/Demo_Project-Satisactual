from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Use relative imports since views folder is inside this app
from .views.mstaddrtype_view import MstAddrTypesViewSet
from .views.mstdepartmentsupportteam_view import MstDepartmentSupportTeamViewSet
from .views.mst_disabilitycodes_view import MstDisabilityCodesViewSet
from .views.mstdepartment_view import MstDepartmentsViewSet
from .views.mst_disclosurelang_view import MstDisclosureLangViewSet
from .views.mst_disclosures_view import MstDisclosuresViewSet
from .views.mst_districtcode_view import MstDistrictCodesViewSet
from .views.sys_email_template_view import SysEmailTemplatesViewSet
# from .views.mst_applscoring_view import MstApplScoringViewSet
# from .views.mst_assignment_types_view import MstAssignmentTypesViewSet
from .views.mst_auditchecklist_view import MstAuditChecklistViewSet
from .views.mst_audittypes_view import MstAuditTypesViewSet
# from .views.mst_bankbranches_view import MstBankBranchesViewSet
# from .views.mst_bankcodes_view import MstBankCodesViewSet
# from .views.mst_banktypes_view import MstBankTypesViewSet
# from .views.mst_blockcodes_view import MstBlockCodesViewSet
# from .views.mst_cardlogos_view import MstCardLogosViewSet
# from .views.mst_centertypes_views import MstCenterTypesViewSet
from .views.mst_cityclasses_view import MstCityClassesViewSet
# from .views.mst_clauselibrary_view import MstClauseLibraryViewSet
# from .views.mst_clauselibrarylang_view import MstClauseLibraryLangViewSet
# from .views.mst_collateraltypes_view import MstCollateralTypesViewSet
from .views.mst_countrycodes_view import MstCountryCodesViewSet
# from .views.mst_covanantcodes_view import MstCovenantCodesViewSet
# from .views.mst_covenanttypes_view import MstCovenantTypesViewSet
from .views.mst_credit_officerlevels_view import MstCreditOfficerLevelsViewSet
# from .views.mst_croptypes_view import MstCropTypesViewSet
from .views.mst_currency_view import MstCurrencyViewSet
from .views.mst_secmenu_options_view import SecMenuOptionsViewSet
from .views.mst_language_view import MstLanguagesViewSet
# from .views.mst_legal_disputetypes_view import MstLegalDisputeTypeViewSet
from .views.mst_major_city_view import MstMajorCityViewSet
from .views.mst_userdesignation_view import MstUserDesignationViewSet
from .views.mst_statecodes_view import MstStateCodesViewSet
# from .views.mst_customer_view import CusMasterViewSet
# from .views.mst_cus_phonehist_view import CusPhoneHistViewSet
# from .views.mst_cus_miscdocs_view import CusMiscDocsViewSet
from .views.mst_pincodes_view import MstPinCodesViewSet
from .views.mst_timezone_view import MstTimeZoneViewSet
from .views.sys_css_theme_view import SysCssThemeViewSet
from .views.sys_user_message_view import SysUserMessageViewSet
from .views.sys_install_module_view import SysInstallModuleViewSet
from .views.sub_licences_view import SubLicenceViewSet
from .views.sub_package_roles_view import SubPackageRolesViewSet
from .views.sub_licance_hist_view import SubLicencesHistViewSet
from .views.sys_org_chart_view import SysOrgChartViewSet



router = DefaultRouter()

router.register(r'mst-addrs', MstAddrTypesViewSet, basename='mstaddr')
router.register(r'mst-department-support-team',MstDepartmentSupportTeamViewSet,basename='mstdepartmentsupportteam')
router.register(r'mst-disabilitycodes',MstDisabilityCodesViewSet,basename='mstdisabilitycodes')
router.register(r'mst-department',MstDepartmentsViewSet,basename='mstdepartment')
router.register(r'mst-disclosure-lang',MstDisclosureLangViewSet,basename='mstdisclosurelang')
router.register(r'mst-disclosures',MstDisclosuresViewSet,basename='mstdisclosures')
router.register(r'mst-districtcode',MstDistrictCodesViewSet,basename='mstdistrictcode')
router.register(r'sys-email-template',SysEmailTemplatesViewSet,basename='sys-email-template')
# router.register(r'mst-applscoring',MstApplScoringViewSet,basename='mstapplscoring')
# router.register(r'mst-assignment-types',MstAssignmentTypesViewSet,basename='mstassignmenttypes')
router.register(r'mst-audit-checklist',MstAuditChecklistViewSet,basename='mstauditchecklist')
router.register(r'mst-audit-types', MstAuditTypesViewSet,basename='mstaudittypes')
# router.register(r'mst-bank-branches', MstBankBranchesViewSet,basename='mstbankbranches')
# router.register(r'mst-bank-codes', MstBankCodesViewSet,basename='mstbankcodes')
# router.register(r'mst-bank-types', MstBankTypesViewSet,basename='mstbanktypes')
# router.register(r'block-codes', MstBlockCodesViewSet,basename='mstblockcodes')
# router.register(r'mst-cardlogos',MstCardLogosViewSet,basename='mstcardlogos')
# router.register(r'mst_center_types', MstCenterTypesViewSet,basename='mstcentertypes')
router.register(r'mst-cityclasses',MstCityClassesViewSet,basename='mstcityclasses')
# router.register(r'mst-clause-library', MstClauseLibraryViewSet,basename='mstclauselibrary')
# router.register(r'mst-clause-library-lang', MstClauseLibraryLangViewSet,basename='mstclauselibrarylang')
# router.register(r'mst-collateral-types', MstCollateralTypesViewSet,basename='mstcollateraltypes')
router.register(r'mst-country-codes', MstCountryCodesViewSet,basename='mstcountrycodes')
# router.register(r'mst-covenant-codes', MstCovenantCodesViewSet,basename='mstcovenantcodes')
# router.register(r'mst-covenant-types', MstCovenantTypesViewSet,basename='mstcovenanttypes')
router.register(r'mst-credit-officer-levels', MstCreditOfficerLevelsViewSet,basename='mstcreditofficerlevels')
# router.register(r'mst-crop-types', MstCropTypesViewSet,basename='mstcroptypes',)
router.register(r'mst-currencies', MstCurrencyViewSet,basename='mstcurrencies')
router.register(r'menu-options', SecMenuOptionsViewSet,basename='menuoptions')
router.register(r'mst-language',MstLanguagesViewSet,basename='mstlanguage')
# router.register(r'mst-legal-disputetypes',MstLegalDisputeTypeViewSet,basename='mstlegaldisputetypes')
router.register(r'mst-major-city',MstMajorCityViewSet,basename='mstmajorcity')
router.register(r'mst-user-designation',MstUserDesignationViewSet,basename='mstuserdesignation')
router.register(r'mst-state-codes',MstStateCodesViewSet,basename='mststatecode')
# router.register(r'mst-customer',CusMasterViewSet,basename='mstcustomer')
# router.register(r'mst-customer-phonehist',CusPhoneHistViewSet,basename='mstcusphonehist')
# router.register(r'mst-customer-Miscellaneous-docs',CusMiscDocsViewSet,basename='mst-customermiscellaneous')
router.register(r'mst-pincodes',MstPinCodesViewSet,basename='mstpincodes')
router.register(r'mst-timezone',MstTimeZoneViewSet,basename='mst-timezone')
router.register(r'sys-css-theme',SysCssThemeViewSet,basename='sys-css-theme')
router.register(r'sys-user-message',SysUserMessageViewSet,basename='sys-user-message')
router.register(r'sys-install-module',SysInstallModuleViewSet,basename='sys-install-module')
router.register(r'sub-licence',SubLicenceViewSet,basename='sub-licence')
router.register(r'sub-package-roles',SubPackageRolesViewSet,basename='sub-package-roles')
router.register(r'sub-licence-hist',SubLicencesHistViewSet,basename='sub-licence-hist')
router.register(r'sys-org-chart',SysOrgChartViewSet,basename='sys-org-chart')


urlpatterns = [
    path('', include(router.urls)),
]

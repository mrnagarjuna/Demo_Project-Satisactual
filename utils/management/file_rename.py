import os
from datetime import datetime
from django.utils.text import slugify


def custom_upload_to(instance, filename, field_name):
    """
    Generate a custom file path and name for uploaded files based on model and field.

    Args:
        instance: The model instance.
        filename: The original file name.
        field_name: The field name (e.g., 'profile_pic', 'gallery_image').

    Returns:
        str: The new file path with a renamed file.
    """
    # Extract the file extension
    extension = os.path.splitext(filename)[1]

    # Get the model name dynamically
    model_name = instance.__class__.__name__.lower()

    # Use model-specific logic to create an identifier based on the model's fields
    # if model_name == 'user':  # For the User model
    #     # Use first name and last name
    #     identifier = slugify(f"{instance.fname}_{instance.lname}")
    if model_name == 'cmpcampaigns':  # For the CmpCampaigns model
        # Use the title of the gallery image
        identifier = slugify(instance.txt_campaign_name)
    elif model_name == 'mstthirdparties':  # For the third party model
        # Use banner title (or a fallback)
        identifier = slugify(instance.txt_third_party_name)
    elif model_name == 'SecMenuOptions':  # For the menu model
        # Use country name (or a fallback)
        identifier = slugify(instance.cod_menu_option)
    elif model_name == 'SecUserPreferences':  # For the user profile pic model
        # Use logo name (or a fallback)
        identifier = slugify(instance.txt_login_id)
    # elif model_name == 'kycdetail':
    #     #use kyc name
    #     identifier = slugify(instance.kyc_type)
    # elif model_name == 'emailslog':
    #     #user emails log
    #     identifier = slugify(instance.attachment)
    # elif model_name == 'visatypemaster':
    #     #use visa type name
    #     identifier = slugify(instance.image)
    # elif model_name == 'service':
    #     #use servicename
    #     identifier = slugify(instance.name)
    # elif model_name == 'testimonial':
    #     #use client name
    #     identifier = slugify(instance.client_name)
    # elif model_name == 'notification':
    #     #use notification title
    #     identifier = slugify(instance.notification_title)
    # elif model_name == 'siteprofile':
    #     identifier = slugify(instance.title)
    # elif model_name == 'socialmedia':
    #     identifier = slugify(instance.name)
    # elif model_name == 'integrationmaster':
    #     #use integration name
    #     identifier = slugify(instance.icon)
    # elif model_name == 'globalsitesetting':
    #     identifier = slugify(instance.site_title)
        
    # elif model_name == 'globalsitesetting':
    #     identifier = slugify(instance.site_title)
    
    # elif model_name == 'clientsitesetting':
    #     identifier = slugify(instance.site_title)
        
    # elif model_name == 'feature':
    #     identifier = slugify(instance.name)
    # elif model_name == 'clientmedia':
    #     identifier = slugify(instance.name)
    # elif model_name == 'campaignattachment':
    #     identifier = slugify(instance.campaign)
    # elif model_name == 'campaign':
    #     identifier = slugify(instance.title)

    # elif model_name == 'emailgatewaysetting':
    #     identifier = slugify(instance.provider)
    # elif model_name == 'smsgatewaysetting':
    #     identifier = slugify(instance.provider)
    # elif model_name == 'paymentgatewaysetting':
    #     identifier = slugify(instance.provider)
    # elif model_name == 'frontfeature':
    #     identifier = slugify(instance.title)
    
    else:
        # Default: use the model's pk (primary key) or a default identifier
        identifier = str(instance.pk or 'unknown')

    # Generate a unique file name using the timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    new_filename = f"{identifier}_{timestamp}{extension}"
    
    # Build the directory path dynamically for each model
    directory = f"site/{model_name}/{field_name}/"  # Example: site/user/profile_pic/

    return os.path.join(directory, new_filename)


# Directly using these functions for the respective fields

# def upload_to_profile_pic(instance, filename):
#     return custom_upload_to(instance, filename, 'profile_pic')

# def upload_to_gallery_image(instance, filename):
#     return custom_upload_to(instance, filename, 'gallery_image')

# def upload_to_gallery_video(instance, filename):
#     return custom_upload_to(instance, filename, 'gallery_video')

# def upload_to_banner_image(instance, filename):
#     return custom_upload_to(instance, filename, 'banner_image')

def upload_to_logo_image(instance, filename):
    return custom_upload_to(instance, filename, 'logo_image')

# def upload_to_favicon(instance, filename):
#     return custom_upload_to(instance, filename, 'favicon')

# def upload_to_country(instance, filename):
#     return custom_upload_to(instance, filename, 'country')

# def upload_to_kyc(instance, filename):
#     return custom_upload_to(instance, filename, 'kyc')

# def upload_to_emailslog(instance, filename):
#     return custom_upload_to(instance, filename, 'attachment')

# def upload_to_visatypemaster(instance, filename):
#     return custom_upload_to(instance, filename, 'visatypemaster')

# def upload_to_service(instance, filename):
#     return custom_upload_to(instance, filename, 'service')

# def upload_to_testimonial(instance, filename):
#     return custom_upload_to(instance, filename, 'testimonial')

# def upload_to_notification(instance, filename):
#     return custom_upload_to(instance, filename, 'notification')

# def upload_to_site_profile(instance, filename):
#     return custom_upload_to(instance, filename, 'site_profile')

# def upload_to_social_media(instance, filename):
#     return custom_upload_to(instance, filename, 'social_media')

# def upload_to_integration_icons(instance, filename):
#     return custom_upload_to(instance, filename, 'integration_icons')

# def upload_to_global_site_setting_logo(instance, filename):
#     return custom_upload_to(instance, filename, 'logo')

# def upload_to_global_site_setting_favicon(instance, filename):
#     return custom_upload_to(instance, filename, 'favicon')

# def upload_to_client_site_setting_logo(instance, filename):
#     return custom_upload_to(instance, filename, 'logo')

# def upload_to_feature(instance, filename):
#     return custom_upload_to(instance, filename, 'feature')

# def upload_to_client_photo(instance, filename):
#     return custom_upload_to(instance, filename, 'client_media')

# def upload_to_campaign(instance, filename):
#     return custom_upload_to(instance, filename, 'recipient_file')
def upload_to_third_Party(instance, filename):
    return custom_upload_to(instance, filename, 'third_party_logo')
def upload_to_menuoption(instance, filename):
    return custom_upload_to(instance, filename, 'menu_logo')
def upload_to_third_Party_poa(instance, filename):
    return custom_upload_to(instance, filename, 'poa_logo')
def upload_to_user_profile_pic(instance, filename):
    return custom_upload_to(instance, filename, 'user_profile_pic')
# def upload_to_emailsetting(instance, filename):
#     return custom_upload_to(instance, filename, 'logo')

# def upload_to_smssetting(instance, filename):
#     return custom_upload_to(instance, filename, 'logo')

# def upload_to_paymentsetting(instance, filename):
#     return custom_upload_to(instance, filename, 'logo')

# def upload_to_f_feature(instance, filename):
#     return custom_upload_to(instance, filename, 'image')
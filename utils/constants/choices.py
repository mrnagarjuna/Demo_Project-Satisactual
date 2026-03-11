 # -----------------------------
    # Choice Definitions
    # -----------------------------
YES_NO_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
REC_STATUS_CHOICES = [
        ('A', 'Active'),
        ('N', 'New'),
        ('M', 'Modified'),
        ('R', 'Reviewed'),
        ('C', 'Cancelled'),
        ('X', 'Deleted'),
    ]
AUDIT_PERIODICITY_CHOICES = (
    ('A', 'Annual'),
    ('M', 'Monthly'),
    ('Q', 'Quarterly'),
    ('H', 'Half Yearly'),
    ('X', 'None'),
)

OFFICE_TYPE = (
    ('B', 'Branch'),
    ('O', 'Office'),
    ('N', 'None')
)
FOREX_CATEGORY = (
    ('A', 'Category A'),
    ('B', 'Category B'),
    ('C', 'Category C')
)
AUDIT_FREQ_CHOICES = (
    ('M', 'Monthly'),
    ('Q', 'Quarterly'),
    ('H', 'Half-Yearly'),
    ('A', 'Annual'),
)
BASE_COLL_TYPE_CHOICES = [
    ('M', 'Home Mortgage'),
    ('F', 'Financial Asset'),
    ('V', 'Vehicle'),
    ('D', 'Deposit Account'),
    ('O', 'Other'),
]

DEPR_METHOD_CHOICES = [
    ('L', 'Linear'),
    ('R', 'Reducing'),
    ('S', 'Straight Line'),
]

REVIEW_FREQ_CHOICES = [
    ('M', 'Monthly'),
    ('Q', 'Quarterly'),
    ('H', 'Half-Yearly'),
    ('A', 'Annually'),
    ('O', 'Others'),
]
BASE_CHANNEL_CHOICES = (
    ('EML', 'Email'),
    ('PHN', 'Phone'),
    ('SMS', 'SMS'),
    ('FLD', 'Field'),
    ('WEB', 'Web'),
    ('FBK', 'Facebook'),
    ('MAL', 'Mail'),
    ('STR', 'Store'),
)

MAIL_PROTOCOL_CHOICES = (
    ('S', 'SMTP'),
    ('E', 'Exchange'),
    ('O', 'Other'),
)
FREQ_VERIFICATION_CHOICES = (
    ('M', 'Monthly'),
    ('Q', 'Quarterly'),
    ('A', 'Annual'),
    ('R', 'Renewal'),
)


CROP_CLASS_CHOICES = (
    ('BASIC', 'Basic'),
    ('CASH', 'Cash'),
    ('FRUIT', 'Fruit'),
    ('VEG', 'Vegetable'),
    ('HIVAL', 'Hival'),
)
RESIDENCE_TYPE_CHOICES = (
    ('O', 'Own'),
    ('R', 'Rented')
)
WING_CHOICES = (
    ('AIR', 'Air'), 
    ('NAVY', 'Navy'), 
    ('LAND', 'Land'),
    ('PARA', 'Para'), 
    ('POLICE', 'Police'), 
    ('OTH', 'Other')
)
RESIDENCE_TYPE_CHOICES = (
    ('O', 'Own'), 
    ('R', 'Rented')
)
KYC_RISK_CHOICES = (
    ('H', 'High'), 
    ('M', 'Medium'), 
    ('L', 'Low')
)
CUST_TYPE_CHOICES = (
    ('O', 'Organization'), 
    ('I', 'Individual')
)

OLD_ACCT_PROD_CHOICES = (
    ('CAS', 'CAS'), 
    ('CRD', 'CRD'), 
    ('FD', 'FD'), 
    ('LON', 'LON'),
    ('MTG', 'MTG'), 
    ('INS', 'INS'), 
    ('INV', 'INV'), 
    ('PEN', 'PEN'),
    ('OTH', 'Other')
)
GENDER_CHOICES = (
    ('M', 'Male'), 
    ('F', 'Female'), 
    ('O', 'Other'), 
    ('N/A', 'Not Applicable')
)
PHONE_TYPE_CHOICES = (
    ('H', 'Home'),
    ('M', 'Mobile'),
    ('O', 'Office'),
    ('F', 'Fax'),
    ('P', 'Pager'),
    ('A', 'Assistant'),
)
DOC_PURPOSE_CHOICES = (
    ('I', 'Identity'),
    ('A', 'Address'),
    ('S', 'Signature'),
    ('C', 'Credit'),
    ('T', 'Tax'),
    ('P', 'Photo'),
    ('M', 'Misc'),
    ('U', 'Utility'),
    ('F', 'Financial'),
    ('V', 'Verification'),
    ('G', 'Agreement'),
)

BASE_QUESTION_TYPE_CHOICES = (
    ('H', 'Header'),
    ('I', 'Interval'),
    ('R', 'Rating'),
    ('O', 'Ordinal'),
    ('N', 'Nominal'),
    ('X', 'Match'),
)



REPORT_FORMAT_CHOICES = (
    ('TBL', 'Table'),
    ('BAR', 'Bar'),
    ('PIE', 'Pie'),
    ('CLOUD', 'Cloud'),
    ('TIME', 'Time'),
    ('HEAT', 'Heat'),
    ('GEO', 'Geo'),
)

AV_RECORDING_CHOICES = (
    ('A', 'Audio'),
    ('V', 'Video'),
    ('P', 'Photo'),
    ('N', 'None'),
)
PRODUCT_TYPE_CHOICES = (
        ('CAS', 'Current & Savings'),
        ('CRD', 'Credit Card'),
        ('FD', 'Fixed Deposit'),
        ('LON', 'Loan'),
        ('MTG', 'Mortgage'),
        ('INS', 'Insurance'),
        ('INV', 'Investment'),
        ('PEN', 'Pension'),
        ('OTH', 'Other'),
)
DOC_PURPOSE_CHOICES=(
            ('I', 'Initiation'),
            ('A', 'Account Opening'),
            ('S', 'Submission'),
            ('C', 'Closure'),
            ('T', 'Top-up'),
            ('P', 'Post Disbursement'),
            ('M', 'Modification'),
            ('U', 'Updation'),
            ('F', 'Foreclosure'),
            ('V', 'Verification'),
            ('G', 'General'),
)
CAMPAIGN_STATUS_CHOICES = (
    ('D', 'Design'),
    ('W', 'Waiting Approval'),
    ('A', 'Active'),
    ('R', 'Response Monitoring'),
    ('X', 'Closed'),
)
COL_DISPLAY_TYPE_CHOICES = (
    ('B', 'Boolean'),
    ('A', 'Alphanumeric'),
    ('N', 'Numeric'),
    ('D', 'Date'),
)
DISPLAY_TYPE_CHOICES = (
        ('A', 'Alpha'),
        ('B', 'Boolean'),
        ('C', 'Choice'),
        ('D', 'Date'),
        ('GL', 'Graph Large'),
        ('GM', 'Graph Medium'),
        ('GS', 'Graph Small'),
        ('GX', 'Graph Extra'),
        ('L', 'List'),
        ('M', 'Multi Select'),
        ('N', 'Numeric'),
        ('R', 'Rating'),
        ('RL', 'Rating List'),
        ('S', 'Single Select'),
        ('T', 'Text'),
        ('AV', 'Audio Visual'),
        ('CUSTOM', 'Custom'),
)
# DISPLAY_TYPE_CHOICES = (
#     ('A', 'A'),
#     ('B', 'B'),
#     ('C', 'C'),
#     ('D', 'D'),
#     ('GL', 'Grid List'),
#     ('GM', 'Grid Matrix'),
#     ('GS', 'Grid Scale'),
#     ('GX', 'Grid Custom'),
#     ('L', 'List'),
#     ('M', 'Multiple'),
#     ('N', 'Numeric'),
#     ('R', 'Range'),
#     ('RL', 'Rating List'),
#     ('S', 'Single'),
#     ('T', 'Text'),
#     ('AV', 'Audio/Video'),
#     ('CUSTOM', 'Custom'),
# )
TAG_TYPE_CHOICES = (
    ('M', 'Message'),
    ('A', 'Alert'),
    ('U', 'Universal'),
)
LINK_TYPE_CHOICES = (
    ('SHOW', 'Show'),
    ('HIDE', 'Hide'),
    ('LABL', 'Label Change'),
    ('MISC', 'Misc'),
)
MSG_TYPE_CHOICES = [
        ('S', 'Success'),
        ('I', 'Information'),
        ('E', 'Error'),
        ('W', 'Warning'),
    ]

BILLING_FREQUENCY = [
        ('R', 'Recurring'),
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('F', 'Fortnightly'),
        ('M', 'Monthly'),
        ('Q', 'Quarterly'),
        ('H', 'Half-Yearly'),
        ('A', 'Annual'),
        ('B', 'Biannual'),
        ('X', 'None'),
    ]

STATUS_CHOICES = [
        ('C', 'Composed'),
        ('A', 'Approved'),
        ('T', 'Tested'),
    ]
RESPONSE_STATUS_CHOICES = [
        ('C', 'Completed'),
        ('I', 'Incomplete'),
        ('Q', 'Qualified'),
        ('N', 'Not Qualified'),
        ('P', 'Pending'),
        ('R', 'Rejected'),
    ]

GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N/A', 'Not Applicable'),
        ('', 'Blank'),
    ]

REFERRAL_STATUS = [
        ('B', 'Booked'),
        ('O', 'Open'),
        ('X', 'Closed'),
    ]

RESPONSE_CLASS = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
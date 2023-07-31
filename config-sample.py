siteConfig = {
    'secret-key' : 'aabbbcccddd',
    'menu' : [
        {'label':'Home', 'link':'/','newtab':False},
        {'label':'Crop Budgets', 'link':'https://www.uidaho.edu/cals/idaho-agbiz/crop-budgets','newtab':True},
        {'label':'Crop Markets', 'link':'https://www.uidaho.edu/cals/idaho-agbiz/crop-markets','newtab':True},
        {'label':'Livestock Budgets', 'link':'https://www.uidaho.edu/cals/idaho-agbiz/livestock-budgets','newtab':True},
        {'label':'Livestock Markets', 'link':'https://www.uidaho.edu/cals/idaho-agbiz/livestock-markets','newtab':True},
        {'label':'Crop Insurance Calculator', 'link':'/crop-insurance/calculator-input','newtab':False},
        {'label':'Find an Extension Office', 'link':'https://www.uidaho.edu/extension/directory/counties','newtab':True},

        {'label':'Example', 'link':'https://google.com','newtab':True}

        #{'label':'Example', 'link':'https://google.com','newtab':False}
        #
        # label: This is what users will see in the sidebar
        # link: The link to the resource. For pages on this site, use absolute references (ex. '/home/somepage'). If you are unsure
        # as to the difference between absolute and relative links, give it a Google search before proceeding
        # newtab: If set to True, the link will open in a new tab. Recommended for external links.
    ]
}

dbConfig = {
    'username' : '',
    'password' : '',
    'hostname' : 'xxxxxxxx.mysql.pythonanywhere-services.com',
    'port' : '3306',
    'database' : 'agbiz_dev'
    }

mailgunConfig = {
    'api_key' : '',
    'from' : 'Idaho Ag Biz <agbiz-noreply@mail.tylerhand.com>',
    'url' : 'https://api.mailgun.net/v3/mail.tylerhand.com/messages',
    'report_template' : '',
    'newsletter_template' : ''
    }

##################################################################################################
# Settings for included applications, please label any additions with comments
##################################################################################################

# Crop Insurance
cropInsuranceConfig = {
    'api-domain' : 'api.tylerhand.com', # Don't include the https://
    'auth-username' : '',
    'auth-password' : '',
    'auth' : ''
    }
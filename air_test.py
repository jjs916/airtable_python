from airtable import airtable
#example for onemunich airtable base
# at = airtable.Airtable('BASE_ID', 'personal token/API key')
at = airtable.Airtable('appOwBfTbJVoMqMff', 'patpNANMFnpCl86sW.636f891f6a657e76514456565b1ab797fc20c470e404fb06750baa9091207cd0')
tmp = at.get('All publications') #tab name

for i in range(len(tmp['records'])):
    print(tmp['records'][i]['fields']['Title'])#get 'Title' field of All publication tab.
from airtable import airtable
# at = airtable.Airtable('BASE_ID', 'API_KEY')
at = airtable.Airtable('appOwBfTbJVoMqMff', 'patpNANMFnpCl86sW.636f891f6a657e76514456565b1ab797fc20c470e404fb06750baa9091207cd0')
tmp = at.get('All publications')

for i in range(len(tmp['records'])):
# print(len(tmp['records']))
    print(tmp['records'][i]['fields']['Title'])
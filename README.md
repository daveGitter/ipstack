# ipstack
Get the latitude and longitude of a given ip address by queying http://api.ipstack.com

# Usage
To get the latitude and longitude of a given ip address (ip_address), go to the directory with the get_lati_longi.py, type the command:
```bash
python get_lati_longi.py <ip_address>
```
The tool will print out the latitude and longitude, if the query is successful,
or it will print an error message if something went wrong during the request.

# About the Security
To use api.ipstack.com, one needs to include his access key in the URI. From the security perspective, this request should be transported using https. 
Unfortunately, api.ipstack.com only supports http, not https, for a free plan. See the response from ipstack below:
```JSON
{
    "success": false,
    "error": {
        "code": 105,
        "type": "https_access_restricted",
        "info": "Access Restricted - Your current Subscription Plan does not support HTTPS Encryption."
    }
}
```

As a trial, a free subscription plan is used here, hence http is the only choice, with security risk.
For a serious usage of this service, a paied subscription plan is hightly recommended, so that https can be used to imporve security.

Python Client for Walmart Canada Marketplace API 

Currently works for only Canada Marketplace. 

Before Usage
-------
You have to get your consumer-id, channel-type and private-key information from:
https://seller.walmart.ca/api-key

Installation
------------

    pip install wmapi


Usage
-----

Import the package

    import wmapi

Create an API Class and request as below:

    items_api = wmapi.Items(client_id = '<your client id>', 
                            private_key='<private key>', 
                            channel_type='<channel type>')

    result = items_api.get_all_items()

More
-------
This library is maintained by https://sellerzon.com 
Please contact for further inquiries: help@sellerzon.com

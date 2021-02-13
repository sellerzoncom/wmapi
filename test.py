import wmapi

items_api = wmapi.Items(client_id = '<your client id>', 
                        private_key='<private key>', 
                        channel_type='<channel type>')

result = items_api.get_all_items()

#!/usr/bin/python
# coding: utf-8
import servicenow_api
import warnings


try:
    username = "admin"
    password = "Yogi4091!"
    servicenow_api_url = "https://yshinde.service-now.com/"
    client = servicenow_api.Api(url=servicenow_api_url, username=username, password=password)
except AttributeError:
    pass
except UserWarning as warning:
    print(f'caught a UserWarning: {warning}')


# print(dir(servicenow_api))

# table = client.get_table(table="incident")
# print(f"Table: {table}")
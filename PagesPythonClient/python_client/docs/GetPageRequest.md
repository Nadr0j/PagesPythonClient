# GetPageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**namespace** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from pages_client.models.get_page_request import GetPageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPageRequest from a JSON string
get_page_request_instance = GetPageRequest.from_json(json)
# print the JSON string representation of the object
print(GetPageRequest.to_json())

# convert the object into a dict
get_page_request_dict = get_page_request_instance.to_dict()
# create an instance of GetPageRequest from a dict
get_page_request_from_dict = GetPageRequest.from_dict(get_page_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



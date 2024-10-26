# WritePageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**namespace** | **str** |  | 
**name** | **str** |  | 
**content** | **str** |  | 
**overwrite_existing** | **bool** |  | [optional] 

## Example

```python
from pages_client.models.write_page_request import WritePageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WritePageRequest from a JSON string
write_page_request_instance = WritePageRequest.from_json(json)
# print the JSON string representation of the object
print(WritePageRequest.to_json())

# convert the object into a dict
write_page_request_dict = write_page_request_instance.to_dict()
# create an instance of WritePageRequest from a dict
write_page_request_from_dict = WritePageRequest.from_dict(write_page_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



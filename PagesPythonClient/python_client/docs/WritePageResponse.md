# WritePageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**namespace** | **str** |  | 
**name** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from pages_client.models.write_page_response import WritePageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WritePageResponse from a JSON string
write_page_response_instance = WritePageResponse.from_json(json)
# print the JSON string representation of the object
print(WritePageResponse.to_json())

# convert the object into a dict
write_page_response_dict = write_page_response_instance.to_dict()
# create an instance of WritePageResponse from a dict
write_page_response_from_dict = WritePageResponse.from_dict(write_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



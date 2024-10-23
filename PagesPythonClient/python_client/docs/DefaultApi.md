# pages_client.DefaultApi

All URIs are relative to *http://pages.beta.jws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pages_get_page_post**](DefaultApi.md#pages_get_page_post) | **POST** /pages/getPage | Gets a page.
[**pages_write_page_post**](DefaultApi.md#pages_write_page_post) | **POST** /pages/writePage | Writes a page.


# **pages_get_page_post**
> GetPageResponse pages_get_page_post(get_page_request)

Gets a page.

Returns a previously written page based on user, namespace, and page name.

### Example


```python
import pages_client
from pages_client.models.get_page_request import GetPageRequest
from pages_client.models.get_page_response import GetPageResponse
from pages_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://pages.beta.jws.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pages_client.Configuration(
    host = "http://pages.beta.jws.com"
)


# Enter a context with an instance of the API client
with pages_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pages_client.DefaultApi(api_client)
    get_page_request = pages_client.GetPageRequest() # GetPageRequest | Request body containing user, namespace, and page name.

    try:
        # Gets a page.
        api_response = api_instance.pages_get_page_post(get_page_request)
        print("The response of DefaultApi->pages_get_page_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pages_get_page_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_page_request** | [**GetPageRequest**](GetPageRequest.md)| Request body containing user, namespace, and page name. | 

### Return type

[**GetPageResponse**](GetPageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetches a page. |  -  |
**400** | Invalid input, object invalid. |  -  |
**404** | Page not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pages_write_page_post**
> WritePageResponse pages_write_page_post(write_page_request)

Writes a page.

Writes a new page or updates an existing page based on user, namespace, and page name.

### Example


```python
import pages_client
from pages_client.models.write_page_request import WritePageRequest
from pages_client.models.write_page_response import WritePageResponse
from pages_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://pages.beta.jws.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pages_client.Configuration(
    host = "http://pages.beta.jws.com"
)


# Enter a context with an instance of the API client
with pages_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pages_client.DefaultApi(api_client)
    write_page_request = pages_client.WritePageRequest() # WritePageRequest | Request body containing user, namespace, page name, and content.

    try:
        # Writes a page.
        api_response = api_instance.pages_write_page_post(write_page_request)
        print("The response of DefaultApi->pages_write_page_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pages_write_page_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **write_page_request** | [**WritePageRequest**](WritePageRequest.md)| Request body containing user, namespace, page name, and content. | 

### Return type

[**WritePageResponse**](WritePageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully written or updated a page. |  -  |
**400** | Invalid input, object invalid. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


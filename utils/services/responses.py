# from rest_framework.response import Response

# def success_response(message, data=None, status=200):
#     return Response({
#         "success": True,
#         "message": message,
#         "data": data or {}
#     }, status=status)

# def error_response(errors, message="Validation error",   status=400):
#     return Response({
#         "success": False,
#         "message": message,
#         "errors": errors or {}
#     }, status=status)


# from rest_framework import status

# def success_response(message, data=None, status_code=status.HTTP_200_OK):
#     return {
#         "status": True,
#         "message": message,
#         "data": data or {},
#         "code": status_code
#     }

# def error_response(message, errors=None, status_code=status.HTTP_400_BAD_REQUEST):
#     return {
#         "status": False,
#         "message": message,
#         "errors": errors or {},
#         "code": status_code
#     }

########### updated version ###############
from rest_framework.response import Response
from rest_framework import status

# def success_response(message, data=None, status_code=status.HTTP_200_OK):
#     try:
#         return Response({
#             "status": "success",
#             "message": message,
#             "data": data if data is not None else {},
#             "status_code": status_code
#         }, status=status_code)
#     except Exception as e:
#         # Catch JSON serialization issues
#         return Response({
#             "status": "error",
#             "message": "Failed to get success response data",
#             "errors": str(e),
#             "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
#         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# def error_response(message="Validation error", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
#     try:
#         return Response({
#             "status": "error",
#             "message": message,
#             "errors": errors if errors is not None else {},
#             "status_code": status_code
#         }, status=status_code)
#     except Exception as e:
#         return Response({
#             "status": "error",
#             "message": "Failed to get error response",
#             "errors": str(e),
#             "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
#         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# def success_response(message, data=None, status_code=status.HTTP_200_OK):
#     return Response({
#         "status": "success",
#         "message": message,
#         "data": data or {},
#         "status_code": status_code
#     }, status=status_code)

# def error_response(message="Validation error", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
#     return Response({
#         "status": "error",
#         "message": message,
#         "errors": errors or {},
#         "status_code": status_code
#     }, status=status_code)





# from functools import wraps

# def ensure_response(func):
#     @wraps(func)
#     def wrapped_func(self, request, *args, **kwargs):
#         response = func(self, request, *args, **kwargs)
#         if response is None:
#             return Response({
#                 'status': 'error',
#                 'message': 'No response returned from view'
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         return response
#     return wrapped_func


###################### update 2.0 #######################
def success_response(message="Success", data=None, status_code=status.HTTP_200_OK):
    try:
        response_data = {
            "status": "success",
            "message": message,
            "status_code": status_code
        }

        if data is not None:
            response_data["data"] = data

        return Response(response_data, status=status_code)

    except Exception as e:
        # logger.exception("Failed to build success response: %s", e)
        return Response({
            "status": "error",
            "message": "Failed to build success response",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "errors": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def error_response(message="Validation error", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    try:
        response_data = {
            "status": "error",
            "message": message,
            "status_code": status_code
        }

        if errors is not None:
            response_data["errors"] = errors

        return Response(response_data, status=status_code)

    except Exception as e:
        # logger.exception("Failed to build error response: %s", e)
        return Response({
            "status": "error",
            "message": "Failed to build error response",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "errors": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
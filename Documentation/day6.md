Function-Based Views (FBV)
Definition: Views are written as Python functions.

Usage: Simple, straightforward logic.

Example:

```py
# filepath: views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})
```

When to use: For simple endpoints with minimal logic.

Class-Based Views (CBV)
Definition: Views are written as Python classes, often inheriting from DRF’s generic views.

Usage: More structure, reusable, and extensible.

Example:

```py
# filepath: views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})
```

When to use: For complex logic, multiple HTTP methods, or when you want to reuse code.

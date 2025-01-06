from django.http import HttpResponse

def redoc_view(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Redoc</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.css" />
        </head>
        <body>
            <redoc spec-url="/swagger.json"></redoc>
            <script src="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"></script>
        </body>
    </html>
    ''', content_type="text/html")

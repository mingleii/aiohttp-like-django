from demo import views

urlpatterns = [
    ["GET", "/{name:\w*}", views.IndexView, "index"],
    ["GET", "/hello/{name:\w*}", views.HelloView, "hello"],
    ["GET", "/json/{name:\w*}", views.json_view, "json"],
    ["GET", "/insert/{name:\w*}", views.InsertData, "inster"],
]
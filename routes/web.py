"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup


ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    
    RouteGroup([
        Get("/","RugpullController@index").name("index"),
        Get("/@id","RugpullController@show").name("show"),
        Post("/","RugpullController@create").name("create"),
        Put("/@id","RugpullController@update").name("update"),
        Delete("/@id","RugpullController@destroy").name("destroy")
    ], prefix="/rugpull",name="rugpull")
]
""" A RugpullController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Rugpull import Rugpull


class RugpullController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", RugpullController)
        """

        id = self.request.param("id")
        return Rugpull.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", RugpullController)
        """

        return Rugpull.all()

    def create(self):
        """Show form to create new resource listings
        ex. Get().route("/create", RugpullController)
        """
        confession = self.request.input("confession")
        age = self.request.input("age")
        rugpull = Rugpull.create({"confession": confession, "age": age})
        return rugpull

    # def store(self):
    #     """Create a new resource listing
    #     ex. Post target to create new Model
    #         Post().route("/store", RugpullController)
    #     """

    #     pass

    # def edit(self):
    #     """Show form to edit an existing resource listing
    #     ex. Get().route("/edit", RugpullController)
    #     """

    #     pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", RugpullController)
        """

        confession = self.request.input("confession")
        age = self.request.input("age")
        id = self.request.param("id")
        Rugpull.where("id",id).update({"confession":confession,"age":age})
        return Rugpull.where("id",id).get()

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", RugpullController)
        """

        id = self.request.param("id")
        rugpull = Rugpull.where("id",id).get()
        Rugpull.where("id",id).delete()
        return rugpull
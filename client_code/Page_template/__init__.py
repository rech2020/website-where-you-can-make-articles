from ._anvil_designer import Page_templateTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Homepage import Homepage
class Page_template(Page_templateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def about_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

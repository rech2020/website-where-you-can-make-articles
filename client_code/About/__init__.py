from ._anvil_designer import AboutTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Homepage import Homepage
from ..About import About

class About(AboutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_link_click(self, **event_args):
    homepage = Homepage()
    open_form(homepage)

  def about_link_click(self, **event_args):
    about = About()
    open_form(about)

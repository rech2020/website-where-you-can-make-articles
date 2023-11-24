from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ArticleEdit import ArticleEdit
from ..AddCategory import AddCategory

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    
    # Any code you write here will run before the form opens.
    self.refresh_articles()
    # Set an event handler on the RepeatingPanel (our 'articles_panel')
    self.articles_panel.set_event_handler('x-delete-article', self.delete_article)

  def add_article_button_click(self, **event_args):
    # Initialise an empty dictionary to store the user inputs
    new_article = {}
    # Open an alert displaying the 'ArticleEdit' Form
    save_clicked = alert(
      content=ArticleEdit(item=new_article),
      title="Add Article",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      anvil.server.call('add_article', new_article)
      self.refresh_articles()

  def refresh_articles(self):
    # Load existing articles from the Data Table, 
    # and display them in the RepeatingPanel
    self.articles_panel.items = anvil.server.call('get_articles')

  def delete_article(self, article, **event_args):
    # Delete the article
    anvil.server.call('delete_article', article)
    # Refresh articles to remove the deleted article from the Homepage
    self.refresh_articles()

  def add_category_click(self, **event_args):
    new_category = {}
    save_clicked = alert(
      content=AddCategory(item=new_category),
      title="Add Category",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    if save_clicked:
      anvil.server.call('add_category', new_category)
      

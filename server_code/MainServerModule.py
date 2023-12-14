import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

def verify_user_permission(article):
  current_user = anvil.users.get_user()
  # Check that someone is logged in
  if current_user is not None:
    print('user passed the logged in check')
    # Check if the article to be updated does exist in the Data Table
    # Check that the article belongs to the logged in user
    if app_tables.articles.has_row(article) and article['user'] == current_user:
      print('user passed the article belonging check')
      return True

@anvil.server.callable
def add_article(article_dict):
  # Get the logged in user
  current_user = anvil.users.get_user()

  # Check that someone is logged in
  if current_user is not None:
    app_tables.articles.add_row(
	  created=datetime.now(),
	  # Store the logged in user in the 'user' column
	  user=current_user,
	  **article_dict
	)

@anvil.server.callable
def get_articles():
  # Get the logged in user
  current_user = anvil.users.get_user()

  # Check that someone is logged in
  if current_user is not None:
    # Get a list of articles that belong to the logged-in user,
    # sorted by 'created' column, in descending order
    return app_tables.articles.search(    )

@anvil.server.callable
def update_article(article, article_dict):
  if verify_user_permission(article):
    # Set the 'updated' property to datetime.now()
    article_dict['updated'] = datetime.now()
    article.update(**article_dict)
  else:
    # Raise an exception if the article doesn't exist in the Data Table
    # or the user doesn't own the article being updated
    print('attempted to update an article that does not exist or does not belong to the user')
    raise Exception("Article does not exist or does not belong to this user")

@anvil.server.callable
def delete_article(article):
  if verify_user_permission(article):
    # Delete the article
    article.delete()
  else:
    # Raise an exception if the article doesn't exist in the Data Table
    # or the user doesn't own the article being deleted
    print('attempted to delete an article that does not exist or does not belong to the user')
    raise Exception("Article does not exist or does not belong to this user")

@anvil.server.callable
def add_category(category_dict):
  app_tables.categories.add_row(
    **category_dict
  )
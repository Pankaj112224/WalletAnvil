from ._anvil_designer import show_usersTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class show_users(show_usersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.button_1.visible = False
       

        # Filter users and set items in the repeating panel
    self.refresh_users()

  def refresh_users(self, username_filter=None):
        # If a username filter is provided, filter users based on the username
        if username_filter:
            customer_type_filter = [user for user in app_tables.wallet_users.search()
                                    if user['usertype'] == 'customer' and user['username'].lower().startswith(username_filter.lower())]
        else:
            # If no username filter, show all customers
            customer_type_filter = [user for user in app_tables.wallet_users.search() if user['usertype'] == 'customer']

        # Set items in the repeating panel
        self.repeating_panel_1.items = customer_type_filter
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.visible = not self.repeating_panel_1.visible

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    username_filter = self.text_box_1.text
    self.refresh_users(username_filter)

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.admin_add_user')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.report_analysis')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.account_management', user= self.user)

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.transaction_monitoring')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.admin_add_user')

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.audit_trail', user = self.user)

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    serves_data = app_tables.sevices.search()

    # Open the admin.user_support form and pass the serves_data
    user_support_form = open_form('admin.user_support', serves_data=serves_data)

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    show_users_form = open_form('admin.show_users')

  def link_8_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Login')

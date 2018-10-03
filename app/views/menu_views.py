from flask.views import MethodView
from flask import request
from app.models.menu_model import OrderMenu
from app.views.helper import response, response_auth,token_required
from app import conn

cur = conn.cursor()
class AddMenuItem(MethodView):
    
    def get(self):
        sql = """
                SELECT * FROM menu 
            """
        cur.execute(sql)
        rows = cur.fetchall()
        if rows:
            all_items = []
            for row in rows:
                item = {
                    'item_id':row[0],
                    'item_name':row[1],
                    'price':row[2]
                }
                all_items.append(item)

            return response('success', all_items, 200)
        return response('success', "Menu is empty, Please consult the caterer.", 200)
        
    def post(self):
            """
            Register food items, and add them to the database
            """
            if request.content_type == 'application/json':
                post_data = request.get_json()
                item_name = post_data.get('item_name')
                price = post_data.get('price')
                
                if isinstance(item_name, str) and isinstance(price ,int):
                    if item_name and price > 0:
                        item = OrderMenu.check_item(item_name)
                        if not item:
                            OrderMenu(item_name=item_name, price=price).save()
                            return response('success', 'Successfully registered', 201)
                        else:
                            return response('failed', 'Failed, Item already exists, Please add a different one', 400)
                    return response('failed', 'Failed, Item name cannot be empty or price should be 1 and above.', 400)
                                   
                return response('failed', 'Item name and quantity should be a string and a non negative integer respectively', 400)
                                
            return response('failed', 'Content-type must be json', 400)
        

class GetMenuUrls:
    @staticmethod
    def fetch_urls(app):
        # Register classes as views
        add_menu_item_view = AddMenuItem.as_view('register_item')
        app.add_url_rule('/menu', view_func=add_menu_item_view, methods=['POST','GET'])
        
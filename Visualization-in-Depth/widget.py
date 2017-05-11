from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown

output_file("dropdown.html")


menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]
dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)

def function_to_call(attr, old, new):
    print dropdown.value

dropdown.on_change('value', function_to_call)
dropdown.on_click(function_to_call)
show(widgetbox(dropdown))

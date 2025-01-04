from dash_visualizer import app

#test whether header is present 
def test_header_loads(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)
    assert dash_duo.find_element("#header").text == 'Pink Morsel Sales - Line Graph'

#test whether graph is present
def test_visualiation_loads(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#line-graph", timeout=10)

#test whether picker is present
def test_picker_loads(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio-buttons", timeout=10)

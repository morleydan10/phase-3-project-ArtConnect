from nicegui import ui

@ui.page('/')
def home_page():

    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')
    

# URLs for routing on homepage
    url_request = 'http://localhost:8080/create_request'
    url_profile_artist = 'http://localhost:8080/create_artist_profile'

    ui.button('Create request', on_click = lambda: ui.open(url_request))
    ui.label('New Artist?').style('color: black; font-size: 200%')
    ui.button('Create Profile', on_click = lambda: ui.open(url_profile_artist))

@ui.page('/create_request')
def create_request():

    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = 'http://localhost:8080/'
    ui.button('Home', on_click = lambda: ui.open(url))
    ui.label('Create Request here!')

@ui.page('/create_artist_profile')
def create_profile():

    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = 'http://localhost:8080/'
    ui.button('Home', on_click = lambda: ui.open(url))
    ui.input(label= 'Name', placeholder = 'Name Here')
    ui.input(label= 'City', placeholder= 'City Here')
    ui.input(label = 'Discipline', placeholder= 'i.e. Paint, Photography, Video, etc.')
    ui.button('Submit', on_click = lambda: ui.submit())

@ui.page('/artist_profile/')
def artist_profile():

    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')
    with ui.tabs() as tabs:
        ui.tab('My Profile')
        ui.tab('My Requests')
        ui.tab('My Portfolio')





ui.run()
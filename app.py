from nicegui import ui

# **********************************HOME PAGE**************************************
@ui.page('/')
def home_page():

    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

# Creates side menu
    # with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    #     ui.label('Side menu')
    

# URLs for routing on homepage
    url_request = 'http://localhost:8080/create_request'
    url_create_profile_artist = 'http://localhost:8080/create_artist_profile'
    url_create_profile_business = 'http://localhost:8080/create_business_profile'
    url_profile_artist = 'http://localhost:8080/artist_profile'
    url_profile_business = 'http://localhost:8080/business_profile'


    
    ui.label('New Artist?').style('color: black; font-size: 175%')
    ui.button('Create Profile', on_click = lambda: ui.open(url_create_profile_artist))

    ui.label('New Business?').style('color: black; font-size: 175%')
    ui.button('Create Profile', on_click = lambda: ui.open(url_create_profile_artist))

    ui.label('Already have a profile?').style('color: black; font-size: 150%')

    with ui.row():
        ui.button('My Artist Profile', on_click = lambda: ui.open(url_profile_artist))
        ui.button('My Business Profile', on_click = lambda: ui.open(url_profile_business))

# ******************************CREATE REQUEST************************************
@ui.page('/create_request')
def create_request():

    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = 'http://localhost:8080/'
    ui.button('Home', on_click = lambda: ui.open(url))
    ui.label('Create Request here!').style('font-size: 150%')
    ui.input(label= 'Name', placeholder = 'Name Here')
    ui.input(label= 'City', placeholder= 'City Here')
    ui.textarea(label = 'Description', placeholder= 'Provide a short desrcription of the job... i.e. Mural on side of building').classes()
    ui.input(label= 'Compensation', placeholder = 'i.e. $500 or $40/hr')

# ************************CREATE ARTIST PROFILE*********************************
@ui.page('/create_artist_profile')
def create_profile():

    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = 'http://localhost:8080/'
    ui.button('Home', on_click = lambda: ui.open(url))
    ui.input(label= 'Name', placeholder = 'Name Here')
    ui.input(label= 'City', placeholder= 'City Here')
    ui.input(label = 'Discipline', placeholder= 'i.e. Paint, Photography, Video, etc.')
    ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')
    ui.button('Submit', on_click = lambda: ui.submit())

# ********************************ARTIST PROFILE**********************************
@ui.page('/artist_profile/')
def artist_profile():

    # def load_requests():
    #     from lib.Artist import Artist
    #     request_data = Artist.requests
    #     grid.options['rowData'] = [
    #         {'name': request_data.name, 
    #         'type': request_data.type, 
    #         'date': request_data.date,
    #         'int': request_data.compensation}]
    
    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')
    
    url = 'http://localhost:8080/'
    ui.button('Home', on_click = lambda: ui.open(url))
    
    with ui.tabs() as tabs:
        profile_tab = ui.tab('My Profile')
        request_tab = ui.tab('My Requests')
        # , on_click= load_requests()
        portfolio_tab = ui.tab('My Portfolio')
    

    ui.label('Your Requests:').style('font-size: 150%')
    grid = ui.aggrid({
    'defaultColDef': {'flex': 10},
    'columnDefs': [
        {'headerName': 'Business', 'field': 'name'},
        {'headerName': 'Type', 'field': 'type'},
        {'headerName': 'Date', 'field': 'date'},
        {'headerName': 'Compensation', 'field': 'comp'},
        {'headerName': 'Parent', 'field': 'parent', 'hide': True},
    ],
    'rowData': [
        {'name': 'A', 'type': 'Paint-canvas', 'date': '01/01/2024', 'comp': '$200'},
        {'name': 'B', 'type': 'Paint-spray', 'date': '01/02/2024', 'comp': '$50/hr'},
        {'name': 'C', 'type': 'Photo', 'date': '01/03/2024', 'comp': '$500'},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-600')
        #     grid = ui.aggrid({
        #     'columnDefs': [
        #         {'headerName': 'Business', 'field': 'name'},
        #         {'headerName': 'Type', 'field': 'type'},
        #         {'headerName': 'Date', 'field': 'date'},
        #         {'headerName': 'Compensation', 'field': 'int'},
        #     ],
        #     'rowData': [],
        # }).style(
        #     'font-size: 50%').bind_visibilty(request_tab)

            # '.custom-header': {'font-weight': 'bold', 'font-size': '16px'})
            # .custom-header({
            #     'font-weight': 'bold', 'font-size': '16px', 'color': '#333'
            #     }
            # )
    

# ****************************CREATE BUSINESS PROFILE********************************
@ui.page('/create_artist_profile')
def create_profile():

    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = 'http://localhost:8080/'
    ui.button('Home', on_click = lambda: ui.open(url))
    ui.input(label= 'Name', placeholder = 'Name Here')
    ui.input(label= 'City', placeholder= 'City Here')
    ui.input(label = 'Discipline', placeholder= 'i.e. Paint, Photography, Video, etc.')
    ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')
    ui.button('Submit', on_click = lambda: ui.submit())

# ******************************BUSINESS PROFILE*********************************
@ui.page('/business_profile/')
def business_profile():

    # def load_requests():
    #     from lib.Artist import Artist
    #     request_data = Artist.requests
    #     grid.options['rowData'] = [
    #         {'name': request_data.name, 
    #         'type': request_data.type, 
    #         'date': request_data.date,
    #         'int': request_data.compensation}]
    
    with ui.header().classes(replace='row items-center') as header:
        ui.label('ArtConnect').style('color: white; font-size: 500%')
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')
    
    url = 'http://localhost:8080/'
    ui.button('Home', on_click = lambda: ui.open(url))
    
    with ui.tabs() as tabs:
        profile_tab = ui.tab('Profile')
        request_tab = ui.tab('Requests')
        # , on_click= load_requests()
        
    
    ui.button('Create request', on_click = lambda: ui.open(url_request))

    ui.label('Your Requests:').style('font-size: 150%')
    grid = ui.aggrid({
    'defaultColDef': {'flex': 10},
    'columnDefs': [
        {'headerName': 'Artist', 'field': 'name'},
        {'headerName': 'Type', 'field': 'type'},
        {'headerName': 'Date', 'field': 'date'},
        {'headerName': 'Compensation', 'field': 'comp'},
        {'headerName': 'Parent', 'field': 'parent', 'hide': True},
    ],
    'rowData': [
        {'name': 'Emily A.', 'type': 'Paint-canvas', 'date': '01/01/2024', 'comp': '$200'},
        {'name': 'Brad B.', 'type': 'Paint-spray', 'date': '01/02/2024', 'comp': '$50/hr'},
        {'name': 'Chelsea C.', 'type': 'Photo', 'date': '01/03/2024', 'comp': '$500'},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-600')



# native=True runs app as a new window
ui.run()
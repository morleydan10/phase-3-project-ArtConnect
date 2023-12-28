from nicegui import ui
import json
from lib.Artist import Artist
from lib.Business import Business
from lib.Request import Request

artist_profiles = []
business_profiles = []
business_requests = []

with open("artist_profiles.json", "r") as file:
    artist_profiles_json = json.load(file)
    for a_profile in artist_profiles_json:
        artist = Artist(
            name=a_profile["name"],
            city=a_profile["city"],
            discipline=a_profile["discipline"],
            rating=None,
        )
        artist_profiles.append(artist)

with open("business_profiles.json", "r") as file:
    business_profiles_json = json.load(file)
    for b_profile in business_profiles_json:
        business = Business(
            name=b_profile["name"],
            city=b_profile["city"],
            type=b_profile["type"],
            rating=None,
        )
        business_profiles.append(business)


with open("business_requests.json", "r") as file:
    business_requests_json = json.load(file)
    for b_request in business_requests_json:
        business_request = Request(**b_request)
        business_requests.append(business_request)

        # The double asterisks ** before b_request is the syntax for dictionary unpacking in Python. When used in a function or constructor call, ** allows you to pass the key-value pairs of a dictionary as keyword arguments.
        # The first line is what the dictionary normally looks like, while the second line is the equivalent it gets converted to when you use the **
        # b_request = {"business": "Some Business", "city": "Some City", "description": "Some Description", "compensation": 5000}
        # **b_request = Request(business="Some Business", city="Some City", description="Some Description", compensation=5000)


# **********************************HOME PAGE**************************************
@ui.page("/")
def home_page():
    with ui.header().classes(replace="row items-center") as header:
        ui.label("ArtConnect").style("color: white; font-size: 500%; padding: 15px")
        # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    # Creates side menu
    # with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    #     ui.label('Side menu')

    # URLs for routing on homepage

    url_create_profile_artist = "http://localhost:8080/create_artist_profile"
    url_create_profile_business = "http://localhost:8080/create_business_profile"
    url_profile_artist = "http://localhost:8080/artist_profile"
    url_profile_business = "http://localhost:8080/business_profile"

    ui.label(
        "Welcome to ArtConnect, where local artists and small businesses can collaborate on amazing new projects!"
    ).style("font-size: 40px; text-align: center")

    with ui.column().style("align-items: center"):
        ui.label("New Artist?").style("color: black; font-size: 175%")
        ui.button("Create Profile", on_click=lambda: ui.open(url_create_profile_artist))

    ui.label("New Business?").style("color: black; font-size: 175%")
    ui.button("Create Profile", on_click=lambda: ui.open(url_create_profile_business))

    ui.label("Already have a profile?").style("color: black; font-size: 150%")

    with ui.row():
        ui.button("My Artist Profile", on_click=lambda: ui.open(url_profile_artist))
        ui.button("My Business Profile", on_click=lambda: ui.open(url_profile_business))


# ******************************CREATE REQUEST************************************
@ui.page("/create_request")
def create_request():
    with ui.header().classes(replace="row items-center") as header:
        ui.label("ArtConnect").style("color: white; font-size: 500%; padding: 15px")

    url = "http://localhost:8080/"
    ui.button("Home", on_click=lambda: ui.open(url))
    ui.label("Create Request here!").style("font-size: 150%")
    business_name = ui.input(label="Name", placeholder="Name Here")
    city_name = ui.input(label="City", placeholder="City Here")
    request_description = ui.textarea(
        label="Description",
        placeholder="Provide a short description of the job... i.e. Mural on the side of the building",
    ).classes()
    request_compensation = ui.input(
        label="Compensation", placeholder="i.e. $500 or $40/hr"
    )
    submit_button = ui.button(
        "Submit",
        on_click=lambda: submit_request(
            business_name.value,
            city_name.value,
            request_description.value,
            request_compensation.value,
        ),
    )

    def submit_request(
        business_name, city_name, request_description, request_compensation
    ):
        # json_data_business_requests = {
        #     "business": business_name,
        #     "city": city_name,
        #     "description": request_description,
        #     "compensation": request_compensation,
        # }
        new_request = Request(
            business=business_name,
            city=city_name,
            description=request_description,
            compensation=request_compensation,
        )

        business_requests.append(new_request)
        # print(business_requests)
        save_requests_to_json()

        ui.notify("Request Submitted")

    def save_requests_to_json():
        with open("business_requests.json", "w") as json_file:
            # import pdb; pdb.set_trace()
            business_requests_json = [br.to_dict() for br in business_requests]
            json.dump(business_requests_json, json_file, indent=2,)


# ************************CREATE ARTIST PROFILE*********************************
@ui.page("/create_artist_profile")
def create_profile():
    with ui.header().classes(replace="row items-center") as header:
        ui.label("ArtConnect").style("color: white; font-size: 500%; padding: 15px")
        # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = "http://localhost:8080/"
    ui.button("Home", on_click=lambda: ui.open(url))
    name_input = ui.input(label="Name", placeholder="Name Here")
    city_input = ui.input(label="City", placeholder="City Here")
    discipline_input = ui.input(
        label="Discipline", placeholder="i.e. Paint, Photography, Video, etc."
    )

    profile_image = ui.upload(
        on_upload=lambda e: ui.notify(f"Uploaded {e.name}")
    ).classes("max-w-full")
    submit_button = ui.button(
        "Submit",
        on_click=lambda: submit_profile(
            name_input.value, city_input.value, discipline_input.value, profile_image
        ),
    )

    def submit_profile(name, city, discipline, image):
        _json_data_artist = {
            "name": name,
            "city": city,
            "discipline": discipline,
            "image": str(image),  # Convert the profile_image object to a string
        }

        artist_profiles.append(_json_data_artist)

        save_artist_profiles_to_json()

        ui.notify("Information Submitted")

    def save_artist_profiles_to_json():
        with open("artist_profiles.json", "w") as json_file:
            json.dump(artist_profiles, json_file, indent=2)


# ********************************ARTIST PROFILE**********************************
@ui.page("/artist_profile/")
def artist_profile():
    # def load_requests():
    #     from lib.Artist import Artist
    #     request_data = Artist.requests
    #     grid.options['rowData'] = []

    with ui.header().classes(replace="row items-center") as header:
        ui.label("ArtConnect").style("color: white; font-size: 500%; padding: 15px")
        # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = "http://localhost:8080/"
    ui.button("Home", on_click=lambda: ui.open(url))

    ui.label("Your Profile:").style("font-size: 150%; font-weight: bold")
    with ui.row().style("align-content: flex; gap: 20px; align-items: center"):
        with ui.avatar().style("font-size: 100px"):
            ui.image(f"User Pic")
        ui.label(f"User name").style("font-size: 50px;  padding: 10px")
        ui.label("Rating: ").style("font-size: 30px;")
        ui.icon("star").style("font-size: 40px; color: yellow")

    ui.label(f"User City/Location").style("font-size: 150%")
    ui.label(f"User Discipline").style("font-size: 150%")
    ui.label(f"User Bio").style("font-size: 150%")

    ui.label("Your Requests:").style("font-size: 150%; font-weight: bold")
    grid = ui.aggrid(
        {
            "defaultColDef": {"flex": 10},
            "columnDefs": [
                {"headerName": "Business", "field": "name"},
                {"headerName": "Type", "field": "type"},
                {"headerName": "Date", "field": "date"},
                {"headerName": "Compensation", "field": "comp"},
                {"headerName": "Parent", "field": "parent", "hide": True},
            ],
            "rowData": [
                {
                    "name": "A",
                    "type": "Paint-canvas",
                    "date": "01/01/2024",
                    "comp": "$200",
                },
                {
                    "name": "B",
                    "type": "Paint-spray",
                    "date": "01/02/2024",
                    "comp": "$50/hr",
                },
                {"name": "C", "type": "Photo", "date": "01/03/2024", "comp": "$500"},
            ],
            "rowSelection": "multiple",
        }
    ).classes("max-h-600")

    ui.label("Your Portfolio:").style("font-size: 150%; font-weight: bold")
    ui.image()


# ****************************CREATE BUSINESS PROFILE********************************
@ui.page("/create_business_profile")
def create_profile():
    with ui.header().classes(replace="row items-center") as header:
        ui.label("ArtConnect").style("color: white; font-size: 500%; padding: 15px")
        # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = "http://localhost:8080/"
    ui.button("Home", on_click=lambda: ui.open(url))
    name_input = ui.input(label="Name", placeholder="Name Here")
    city_input = ui.input(label="City", placeholder="City Here")
    type_input = ui.input(
        label="Type", placeholder="i.e. Restaurant, Retail, Commercial office, etc."
    )
    # ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')
    submit_button = ui.button(
        "Submit",
        on_click=lambda: submit_profile(
            name_input.value,
            city_input.value,
            type_input.value,
            # profile_image
        ),
    )

    def submit_profile(name, city, type):
        _json_data_business = {
            "name": name,
            "city": city,
            "type": type,
            # 'image': str(image),  # Convert the profile_image object to a string
        }

        business_profiles.append(_json_data_business)

        save_business_profiles_to_json()

        ui.notify("Information Submitted")

    def save_business_profiles_to_json():
        with open("business_profiles.json", "w") as json_file:
            json.dump(business_profiles, json_file, indent=2)


# ******************************BUSINESS PROFILE*********************************
@ui.page("/business_profile/")
def business_profile():
    def load_requests():
        # Have to convert the objects into python dictionaries so they can be loaded into the grid
        grid.options["rowData"] = [br.to_dict() for br in business_requests]

    with ui.header().classes(replace="row items-center") as header:
        ui.label("ArtConnect").style("color: white; font-size: 500%; padding: 15px")
        # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = "http://localhost:8080/"
    ui.button("Home", on_click=lambda: ui.open(url))

    # with ui.tabs() as tabs:
    #     profile_tab = ui.tab('Profile')
    #     request_tab = ui.tab('Requests')
    # , on_click= load_requests()

    url_request = "http://localhost:8080/create_request"

    ui.label("Your Profile:").style("font-size: 150%")
    with ui.row().style("align-content: flex; gap: 20px; align-items: center"):
        with ui.avatar().style("font-size: 100px"):
            ui.image(f"User Pic")
        business_name = ui.label(f"{business.name}").style(
            "font-size: 50px;  padding: 10px"
        )
        # **RATING**
        with ui.label("Rating: ").style("font-size: 30px;"):
            ui.icon("star").style(
                "font-size: 40px; color: yellow; border-color: black; border-weight: 5px"
            )

    business_location = ui.label(f"{business.city}").style("font-size: 150%")
    business_type = ui.label(f"{business.type}").style("font-size: 150%")

    ui.label("Your Requests:").style("font-size: 150%")
    ui.button("Create request", on_click=lambda: ui.open(url_request))
    grid = ui.aggrid(
        {
            "defaultColDef": {"flex": 10},
            "columnDefs": [
                {"headerName": "Business", "field": "business"},
                {"headerName": "City", "field": "city"},
                {"headerName": "Description", "field": "description"},
                {"headerName": "Compensation", "field": "compensation"},
            ],
            "rowSelection": "multiple",
        }
    ).classes("max-h-600")

    # Call load_requests to load the initial data when the page is loaded
    load_requests()


# native=True runs app as a new window
ui.run()

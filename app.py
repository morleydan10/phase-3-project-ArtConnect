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
        artist = Artist(**a_profile)
            # name=a_profile["name"],
            # city=a_profile["city"],
            # discipline=a_profile["discipline"],
        artist_profiles.append(artist)
        print(artist.to_dict())


with open("business_profiles.json", "r") as file:
    business_profiles_json = json.load(file)
    for b_profile in business_profiles_json:
        business = Business(**b_profile)
            # name=b_profile["name"],
            # city=b_profile["city"],
            # type=b_profile["type"],
            # image=b_profile["image"],
            # rating=None
        
        business_profiles.append(business)
        print(business.to_dict())


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

    with ui.column().style("align-items: center"):
        ui.label(
            "Welcome to ArtConnect, where local artists and small businesses can collaborate on amazing new projects!"
        ).style("font-size: 40px; text-align: center")

        whitespace = ui.label('This is whitespace').style("color: white; font-size: 75px")

        with ui.column().style("align-items: center"):

            with ui.column().style("align-items: center"):
                ui.label("New Artist?").style("color: black; font-size: 40px")
                ui.button("Create Artist Profile", on_click=lambda: ui.open(url_create_profile_artist))

            ui.label("New Business?").style("color: black; font-size: 40px")
            ui.button("Create Business Profile", on_click=lambda: ui.open(url_create_profile_business))

            ui.label("Already have a profile?").style("color: black; font-size: 40px")

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
    ui.label("Create Request").style("font-size: 50px")
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
    ui.label("Create Artist Profile").style("font-size: 50px")
    name_input = ui.input(label="Name", placeholder="Name Here")
    city_input = ui.input(label="City", placeholder="City Here")
    discipline_input = ui.input(
        label="Discipline", placeholder="i.e. Paint, Photography, Video, etc."
    )

    profile_image = ui.input(label="Profile Image", placeholder="url here")
    submit_button = ui.button(
        "Submit",
        on_click=lambda: submit_profile(
            name_input.value, 
            city_input.value, 
            discipline_input.value, 
            profile_image.value
        ),
    )

    def submit_profile(name_input, city_input, discipline_input, profile_image):
        new_artist_profile = Artist(
            name=name_input,
            city=city_input,
            discipline=discipline_input,
            image=profile_image
        )
        # _json_data_artist = {
        #     "name": name,
        #     "city": city,
        #     "discipline": discipline,
        #     "image": str(image),  # Convert the profile_image object to a string
        # }

        artist_profiles.append(new_artist_profile)

        save_artist_profiles_to_json()

        ui.notify("Information Submitted")

    def save_artist_profiles_to_json():
        with open("artist_profiles.json", "w") as json_file:
            artist_profiles_json = [ap.to_dict() for ap in artist_profiles]
            json.dump(artist_profiles_json, json_file, indent=2)


# ********************************ARTIST PROFILE**********************************
@ui.page("/artist_profile/")
def artist_profile():
    def load_requests():
        grid.options["rowData"] = [br.to_dict() for br in business_requests]

    with ui.header().classes(replace="row items-center") as header:
        ui.label("ArtConnect").style("color: white; font-size: 500%; padding: 15px")
        # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = "http://localhost:8080/"
    ui.button("Home", on_click=lambda: ui.open(url))

    ui.label("Your Profile:").style("font-size: 35px; font-weight: bold")
    with ui.row().style("align-content: flex; gap: 20px; align-items: center"):
        with ui.avatar().style("font-size: 200px"):
            ui.image(f"{artist.image}")
        artist_name = ui.label(f"{artist.name}").style("font-size: 50px;  padding: 10px")
        # **RATING**
        with ui.label("Rating: ").style("font-size: 30px;"):
        #     average_rating = artist.average_rating()
        #     for _ in range(average_rating):
                star = ui.icon("star").style("font-size: 40px; color: gold")

    with ui.grid(columns=2):
        ui.label('City: ').style('font-size: 20px')
        artist_city = ui.label(f"{artist.city}").style("font-size: 25px")

        ui.label('Discipline: ').style('font-size: 20px')
        artist_discipline = ui.label(f"{artist.discipline}").style("font-size: 25px")
        
        ui.label("Bio:").style("font-size: 20px")
        artist_bio = ui.label("Hi I'm Jane. I paint well. Hire me.").style("font-size: 18px")


    ui.label("Your Requests:").style("font-size: 35px; font-weight: bold; padding: 10px")
    grid = ui.aggrid(
        {
            "defaultColDef": {"flex": 10},
            "columnDefs": [
                {"headerName": "Business", "field": "business"},
                {"headerName": "City", "field": "city"},
                {"headerName": "Description", "field": "description"},
                {"headerName": "Compensation", "field": "compensation"},
                # {"headerName": "Parent", "field": "parent", "hide": True},
            ],
            "rowSelection": "multiple",
        }
    ).classes("max-h-100")

    load_requests()

    ui.label("Your Portfolio:").style("font-size: 35px; font-weight: bold")
    ui.image()


# ****************************CREATE BUSINESS PROFILE********************************
@ui.page("/create_business_profile")
def create_profile():
    with ui.header().classes(replace="row items-center") as header:
        ui.label("ArtConnect").style("color: white; font-size: 500%; padding: 15px")
        # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').style('position: flex')

    url = "http://localhost:8080/"
    ui.button("Home", on_click=lambda: ui.open(url))
    ui.label("Create Business Profile").style("font-size: 50px")
    name_input = ui.input(label="Name", placeholder="Name Here")
    city_input = ui.input(label="City", placeholder="City Here")
    type_input = ui.input(
        label="Type", placeholder="i.e. Restaurant, Retail, Commercial office, etc."
    )
    profile_image = ui.input(label="Profile Image", placeholder="url here")
    
    submit_button = ui.button(
        "Submit",
        on_click=lambda: submit_profile(
            name_input.value,
            city_input.value,
            type_input.value,
            profile_image.value
        ),
    )

    def submit_profile(name_input, city_input, type_input, profile_image):
        # _json_data_business = {
        #     "name": name,
        #     "city": city,
        #     "type": type,
        #     'image': str(image),  # Convert the profile_image object to a string
        # }
        new_busines_profile = Business(
            name=name_input,
            city=city_input,
            type=type_input,
            image=profile_image
        )

        business_profiles.append(new_busines_profile)

        save_business_profiles_to_json()
        
        ui.notify("Information Submitted")

    def save_business_profiles_to_json():
        with open("business_profiles.json", "w") as json_file:
            business_profiles_json = [bp.to_dict() for bp in business_profiles]
            json.dump(business_profiles_json, json_file, indent=2)


# ******************************BUSINESS PROFILE*********************************
@ui.page("/business_profile/")
def business_profile():
    def load_requests():
        # Have to convert the objects into python dictionaries so they can be loaded into the grid
        # grid.options["rowData"] = [br.to_dict() for br in business_requests]
        
        grid.options["rowData"] = [br.to_dict() for br in business_requests if br.business == business.name]


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
        with ui.avatar().style("font-size: 200px"):
            ui.image(f"{business.image}")
        business_name = ui.label(f"{business.name}").style(
            "font-size: 50px;  padding: 10px"
        )
        # **RATING**
        with ui.label("Rating: ").style("font-size: 30px;"):
            ui.icon("star").style(
                "font-size: 40px; color: gold; border-color: black; border-weight: 5px"
            )
    
    with ui.grid( columns=2):
        ui.label('City: ').style('font-size: 20px')
        business_location = ui.label(f"{business.city}").style("font-size: 25px")

        ui.label('Type: ').style('font-size: 20px')
        business_type = ui.label(f"{business.type}").style("font-size: 25px")

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

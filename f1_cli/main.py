import typer
import requests
from rich.console import Console
from rich.table import Table
from prettytable import PrettyTable

app = typer.Typer()
console = Console()


@app.command()
def constructors(season: int = typer.Argument(..., help="Year of the F1 season")):
    """
    Fetches Formula 1 constructors for a given year and displays them in a table.
    """

    url = f"https://api.jolpi.ca/ergast/f1/{season}/constructors.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        table = PrettyTable()
        table.field_names = ["Team", "Nationality"]
        constructors = data['MRData']['ConstructorTable']['Constructors']

        for team in constructors:
            constructor_name = team['name']
            country = team['nationality']
            table.add_row([constructor_name, country])
        typer.echo(f"F1 Constructors in the  {season} F1 season: \n{table}")
    else:
        typer.echo(f"Failed to fetch data. Status code: {response.status_code}")

@app.command()
def constructor_standings(season: int):
    """
    Fetches Formula 1 constructor standings for a specific season.
    """
    url = f"https://api.jolpi.ca/ergast/f1/{season}/constructorstandings.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        standings_lists = data["MRData"]["StandingsTable"]["StandingsLists"]

        if not standings_lists:
            typer.echo(f"No constructor standings data found for the {season} season.")
            return

        standings = standings_lists[0].get("ConstructorStandings", [])

        if not standings:
            typer.echo(f"No constructor standings data available for {season}.")
            return

        table = PrettyTable()
        table.field_names = ["Position", "Constructor", "Points", "Wins"]

        for team in standings:
            position = team.get("positionText", "N/A")  
            points = team.get("points", "N/A")
            wins = team.get("wins", "N/A")
            constructor_name = team['Constructor']['name']

            table.add_row([position, constructor_name, points, wins])

        typer.echo(f"Constructor Standings for {season}:\n{table}")
    else:
        typer.echo(f"Failed to fetch data. Status code: {response.status_code}")

@app.command()
def driver_standings(season: int):
    """
    Fetches Formula 1 driver standings for a specific season.
    """
    url = f"https://api.jolpi.ca/ergast/f1/{season}/driverstandings.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        standings_lists = data["MRData"]["StandingsTable"]["StandingsLists"]

        if not standings_lists:
            typer.echo(f"No standings data found for the {season} season.")
            return

        standings = standings_lists[0].get("DriverStandings", [])

        if not standings:
            typer.echo(f"No driver standings data available for {season}.")
            return

        table = PrettyTable()
        table.field_names = ["Position", "Driver", "Points", "Wins"]

        for driver in standings:
            position = driver.get("position", "N/A")  
            points = driver.get("points", "N/A")
            wins = driver.get("wins", "N/A")
            driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"

            table.add_row([position, driver_name, points, wins])

        typer.echo(f"Driver Standings for {season}:\n{table}")
    else:
        typer.echo(f"Failed to fetch data. Status code: {response.status_code}")

@app.command()
def races(season: int = typer.Argument(..., help="Year of the F1 season")):
    """
    Fetches Formula 1 races for a given year and displays them in a table.
    """

    url = f"https://api.jolpi.ca/ergast/f1/{season}/races.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        table = PrettyTable()
        table.field_names = ["Round", "Race", "Circuit", "Date", "Time"]
        races = data['MRData']['RaceTable']['Races']

        for race in races:
            round = race['round']
            name = race['raceName']
            circuit = race['Circuit']['circuitName']
            date = race['date']
            time = race['time']
            table.add_row([round, name, circuit, date, time])
        typer.echo(f"Races in the {season} F1 season: \n{table}")
    else:
        typer.echo(f"Failed to fetch data. Status code: {response.status_code}")

@app.command()
def results(
    season: int = typer.Argument(..., help="Year of the F1 season"),
    race: int = typer.Argument(..., help="Round of the F1 race"),
):
    """
    Fetches Formula 1 race results for a specific round and displays them in a table.
    """

    url = f"https://api.jolpi.ca/ergast/f1/{season}/{race}/results.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        races = data["MRData"]["RaceTable"]["Races"]


        if not races:
            typer.echo(f"No race data found for {season} round {race}.")
            return

        race_data = races[0]
        table = PrettyTable()
        table.field_names = ["Position", "Driver", "Constructor"]

        for result in race_data["Results"]:
            position = result["position"]
            driver_name = result['Driver']['givenName'] + " " + result['Driver']['familyName']
            constructor_name = result["Constructor"]["name"]
            table.add_row([position, driver_name, constructor_name])

        typer.echo(f"Results of the {season} {race_data['raceName']}:\n{table}")
    else:
        typer.echo(f"Failed to fetch data. Status code: {response.status_code}")


if __name__ == "__main__":
    app()
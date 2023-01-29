import requests
from odns.models.odns_models import AllPackages

def all_packages(contains: str = None, limit: int = 1000) -> list[tuple]:
    """
    Returns names and id's of all packages available from <opendata.nhs.scot> 
    in a list as tuples along with the package id, with the option to limit 
    results based on a search term
    """
    url = "https://www.opendata.nhs.scot/api/3/action/"

    if contains:
        contains = f"q=title:{contains}&"
    else:
        contains = f""
    
    req = f"{url}package_search?{contains}rows={limit}"

    res = requests.get(req)

    assert res.status_code == 200

    res = res.json()
    
    packages = []

    for result in res['result']['results']:
        pac_det = AllPackages.parse_obj(result)
        packages.append((pac_det.id, pac_det.name))

    return packages


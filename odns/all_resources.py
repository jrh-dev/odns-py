import requests
from odns.models.odns_models import AllResources
from odns.models.odns_models import AllPackages

def all_resources(package_contains: str = None, resource_contains: str = None) -> dict:
    """
    Returns an overview of all resources available from <opendata.nhs.scot>, 
    with the option to limit results based on both package and resource names.
    The returned data.frame can be used to look-up package and resource ids
    and is useful for exploring the available data sets.
    """
    
    url = "https://www.opendata.nhs.scot/api/3/action/"

    req = f"{url}package_search?"

    res = requests.get(req, timeout = 3)   

    res = res.json()

    resources = []

    for result in res['result']['results']:
        pac_det = AllPackages.parse_obj(result)
        if package_contains is None or package_contains.lower() in pac_det.name.lower():
            for resource in result['resources']:
                res_det = AllResources.parse_obj(resource)
                if resource_contains is None or resource_contains.lower() in res_det.name.lower():
                    resources.append({
                        "package_id":pac_det.id,
                        "package_name":pac_det.name,
                        "resource_id":res_det.id,
                        "resource_name":res_det.name
                        })
    
    return resources


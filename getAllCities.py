from uszipcode import SearchEngine

def get_counties():
    # Create a search object
    search = SearchEngine()

    # Search for zipcodes in Texas
    results = search.by_state('Texas', returns=0)
    
    # print(results)

    # Extract the unique city names from the results
    counties = set([result.post_office_city for result in results])

    return counties

    # print(len(counties))

    # Print the list of cities
    # for county in counties:
    #     print(county)
# print(get_counties())
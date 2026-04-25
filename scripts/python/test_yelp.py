import os
import requests

# Read YELP API key from environment
api_key = os.environ.get("YELP_API_KEY", "").replace("\n", "").replace("\r", "").strip()
if not api_key:
    raise ValueError("YELP_API_KEY environment variable is not set.")

# YELP Fusion API endpoint for business search
url = "https://api.yelp.com/v3/businesses/search"

# Request headers - API key goes here as a "Bearer token"
headers = {
    "Authorization" : f"Bearer {api_key}"
}

# Query parameters - what we're searching for
params = {
    "location" : "Irvine, CA",  # Orange County City
    "categories" : "restaurants",  # Only restaurants
    "limit" : 5  # Just 5 for testing
}

# Make the API call
response = requests.get(url, headers=headers, params=params)

# Check if it worked
if response.status_code == 200:
    data = response.json()
    businesses = data.get("businesses", [])
    print(f"Successfully pulled {len(businesses)} restaurants from Yelp.\n")

    for i, biz in enumerate(businesses, 1):
        print(f"{i}. {biz['name']}")
        print(f"  Rating: {biz['rating']} ({biz['review_count']} reviews)")
        print(f"  Categories: {', '.join([c['title'] for c in biz['categories']])}")
        print(f"  Address: {', '.join(biz['location']['display_address'])}")
        print()
else:
    print(f"Error {response.status_code}: {response.text}")
from django.shortcuts import render
from django.views.generic import TemplateView
import requests

# Create your views here.

class LandingPage(TemplateView):
    template_name = 'landingPage.html'
    def get(self, request):
        url = "https://restcountries.com/v3.1/all"

        response = requests.get(url)
        data = response.json()
       
        countries_with_tourist_spots = []
        for country in data:
            countries_with_tourist_spots.append(country["name"]["common"])
            if len(countries_with_tourist_spots) == 5:
                break
        countries_with_tourist_spots.append("Philippines")
        return render(request,'landingPage.html',{'countries':countries_with_tourist_spots})


class DestinationPage(TemplateView):
    template_name = 'destinationPage.html'

    def get(self, request, country, place):
        def fetch_popular_food(country, city):
            api_key = "Q2-GLImBqseGs8AIRNI4Vxayyhxul90CWrZgfEyvLa9o-qv59S-ADQMxgAbHXL9P_1PuQBvVbM9SzdfMzH7EQntdh4_K1kD6FotzNm8T29MHkGKUvvO9DPwAswuyZHYx"
            url = f"https://api.yelp.com/v3/businesses/search"

            headers = {
                "Authorization": f"Bearer {api_key}"
            }

            params = {
                "categories": "restaurants",
                "location": f"{city}, {country}",
                "sort_by": "rating",
                "limit": 5 
            }

            response = requests.get(url, headers=headers, params=params)
            data = response.json()

            if "businesses" in data:
                businesses = data["businesses"]
                popular_food = [business["name"] for business in businesses]
                return popular_food

            return []

        def fetch_articles(country, query):
            query = "Tourism in " + query
            api_key = "a66fd9d712964e8b9e35342520764d7e"
            url = f"https://newsapi.org/v2/top-headlines?country={country}&q={query}&apiKey={api_key}"

            response = requests.get(url)
            data = response.json()
            if data['status'] == 'ok':
                articles = data['articles']
                return articles

            return []
        # Display the fetched articles
        context = {
            'country': country,
            'place':place
        }
        foods = fetch_popular_food(country, place)
        article = fetch_articles(country, place)
        return render(request, 'destinationPage.html', context)
    
class HotelPage(TemplateView):
    template_name = 'placeView.html'

class LandingPage1(TemplateView):
    template_name = 'landingPage1.html'
"""RugpullTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.Rugpull import Rugpull



class RugpullTableSeeder(Seeder):
    def run(self):
        Rugpull.create({"confession": "I am not the father: I followed Reddit’s advice and asked for a DNA paternity test. Turns out you have to wait for the ninth week to be able to do it. It’s expensive as shit by the way. Anyway… Turns out I am not the father", "age": "27"})
        Rugpull.create({"confession": "Whenever I offer someone food, I secretly hope they say no...", "age": "20"})
        Rugpull.create({"confession": "I ate dog food just to see what it tasted like", "age": "18"})
        Rugpull.create({"confession": "I work at a hotel. The blankets only get washed once a year", "age": "32"})
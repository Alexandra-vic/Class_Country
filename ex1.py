class Locality: 
    country = 'Египет'
    capital = 'Каир'
    attraction = 'Прамиды Гизы, Большой сфинкс'

    def result(self):
        return f'Страна - {self.country}, его столица {self.capital} и достопримечательности: {self.attraction}'

place = Locality()
print(place.result())

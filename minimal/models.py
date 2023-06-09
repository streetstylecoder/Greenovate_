from django.db import models


# Create your models here.

location_options=[
    ('USA','USA'),
    ('Canada','Canada'),
    ('UK','Europe'),
    ('Africa','Africa'),
    ('LatinAmerica','LatinAmerica'),
    ('MiddleEast','MiddleEast'),
    ('OtherCountry','OtherCountry')
    
]


class comp_database(models.Model):
    company_name=models.CharField(max_length=100)
    paper_use=models.IntegerField()
    traditional_hydro_use=models.IntegerField()
    traditional_hydro_location=models.CharField(max_length=100,choices=location_options,default='USA')
    solar_energy=models.IntegerField()
    wind_energy=models.IntegerField()
    hydroelectric_energy=models.IntegerField()
    biomass_energy=models.IntegerField()
    geothermal_energy=models.IntegerField()
    other_clean_energy=models.IntegerField()
    Fuel_petrol=models.IntegerField()
    Fuel_Diesel=models.IntegerField()
    Fuel_LPG=models.IntegerField()
    SmallDieselCar=models.IntegerField()
    MediumDieselCar=models.IntegerField()
    LargeDieselCar=models.IntegerField()
    MediumHybridCar=models.IntegerField()
    LargeHybridCar=models.IntegerField()
    MediumLPGCar=models.IntegerField()
    LargeLPGCar=models.IntegerField()
    MediumCNGCar=models.IntegerField()
    LargeCNGCar=models.IntegerField()
    SmallPetrolVan=models.IntegerField()
    LargePetrolVan=models.IntegerField()
    SmallDielselVan=models.IntegerField()
    MediumDielselVan=models.IntegerField()
    LargeDielselVan=models.IntegerField()
    LPGVan=models.IntegerField()
    CNGVan=models.IntegerField()
    SmallPetrolCar=models.IntegerField()
    MediumPetrolCar=models.IntegerField()
    LargePetrolCar=models.IntegerField()
    SmallMotorBike=models.IntegerField()
    MediumMotorBike=models.IntegerField()
    LargeMotorBike=models.IntegerField()
    DomesticFlight=models.IntegerField()
    ShortEconomyClassFlight=models.IntegerField()
    ShortBusinessClassFlight=models.IntegerField()
    LongEconomyClassFlight=models.IntegerField()
    LongPremiumClassFlight=models.IntegerField()
    LongBusinessClassFlight=models.IntegerField()
    LongFirstClassFlight=models.IntegerField()
    Taxi=models.IntegerField()
    ClassicBus=models.IntegerField()
    EcoBus=models.IntegerField()
    Coach=models.IntegerField()
    NationalTrain=models.IntegerField()
    LightRail=models.IntegerField()
    Subway=models.IntegerField()
    purchased_cooling=models.IntegerField(default=0)
    purchased_heating=models.IntegerField(default=0)
   
    
    
class carbon_emmission(models.Model):
    company_name=models.CharField(max_length=100)
    paper_carbon=models.IntegerField()
    hydro_carbon=models.IntegerField()
    clean_energy_carbon=models.IntegerField()
    Fuel_carbon=models.IntegerField()
    vehicle_carbon=models.IntegerField()
    flight_carbon=models.IntegerField()
    motor_bike_carbon=models.IntegerField()
    public_transit_carbon=models.IntegerField()
    purchased_cooling=models.IntegerField(default=0)
    purchased_heating=models.IntegerField(default=0)
    
    
    
    
    

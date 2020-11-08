from dataclasses import dataclass
from decimal import Decimal

#Typ instytucji: Klub dziecięcy
#Nazwa: Klub Malucha Lazurowy Obłoczek
#Lokalizacja instytucji: ŚLĄSKIE > Powiat Katowice > Katowice > Katowice
#ul. Ignacego Mościckiego 6
#Adres WWW żłobka/klubu: Brak danych
#E-mail żłobka/klubu: meg-ewa@wp.pl
#Telefon żłobka/klubu: 692880409
# Liczba miejsc: 22
# Liczba dzieci zapisanych: 22
# Opłata miesięczna - podstawowa opłata ponoszona przez rodziców za pobyt dziecka (bez zniżek i bez wyżywienia): 500.0 zł
# Opłata za wyżywienie - dzienna: 9.0 zł
# Zniżki: Brak danych
# Godziny otwarcia: Poniedziałek, Wtorek, Środa, Czwartek, Piątek 6:30-16:00
# Czy żłobek/klub jest dostosowany do potrzeb dzieci niepełnosprawnych lub wymagających szczególnej opieki?: NIE
# Podmiot prowadzący - nazwa: SZKOŁA RODZENIA TERCET
# Podmiot prowadzący - NIP: 6341583709
# Podmiot prowadzący - REGON: 276610776
# Podmiot prowadzący - numer pozycji rejestru: 9930/P
# Adres WWW podmiotu prowadzącego żłobek/klub: Brak danych
# Czy podmiot prowadzący zawiesił działalność gospodarczą?: NIE


@dataclass
class Nursery:
    institution_type: str = None
    institution_name: str = None
    host_entity_name: str = None
    host_entity_url: str = None
    host_entity_registry_number: str = None
    host_entity_website_url: str = None
    localization: str = None #todo - split it -> wojewodztwo, powiat, adres
    website_url: str = None
    e_mail: str = None
    telephone_number: str = None
    capacity: int = None
    children_assigned: int = None
    month_payment: Decimal = None
    food_payment: Decimal = None
    discounts: str = None #todo type
    when_open: str = None #todo type
    is_ready_for_disabled: bool = False
    nip: str = None
    regon: str = None
    register_number: str = None    
    is_activity_suspended: str = None #TODO bool type
    map_url: str = None

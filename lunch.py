import time

from Functions import envoie_discord

DELAI = 2.75
NB_ARTICLES = 1
URL_FREE_BOT = "https://www.vinted.fr/vetements?brand_id[]=53&brand_id[]=12&brand_id[]=7&brand_id[]=15&brand_id[]=197478&brand_id[]=6005&brand_id[]=20&brand_id[]=255&brand_id[]=11493&brand_id[]=161&catalog[]=2050&price_from=1&currency=EUR&price_to=50&order=newest_first "
URL_TSHIRT_NIKE = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&brand_id[]=53&price_from=1&currency=EUR&price_to=10&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first"
URL_TSHIRT_LACOSTE = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=304&brand_id[]=677891&brand_id[]=268734&price_to=15"
URL_TSHIRT_RALPH = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&price_to=15&brand_id[]=88&brand_id[]=4273"
URL_TSHIRT_TNF = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&price_to=10&brand_id[]=2319"
URL_TSHIRT_TOMMY = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&price_to=10&brand_id[]=94&brand_id[]=352755"
URL_SWEAT_NIKE = "https://www.vinted.fr/vetements?brand_id[]=53&size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1811&catalog[]=267&catalog[]=1813&catalog[]=1814&catalog[]=1815&catalog[]=1825&price_from=1&currency=EUR&price_to=20&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first"
URL_SWEAT_LACOSTE = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=79&brand_id[]=304&brand_id[]=677891&brand_id[]=268734&price_from=1&currency=EUR&price_to=25&status[]=3&status[]=2&status[]=6&status[]=1&order=newest_first"
URL_SWEAT_RALPH = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1811&catalog[]=267&catalog[]=1813&catalog[]=1814&catalog[]=1815&catalog[]=1825&catalog[]=1812&price_from=1&currency=EUR&price_to=25.00&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=88&brand_id[]=4273"
URL_SWEAT_TNF = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1811&catalog[]=267&catalog[]=1813&catalog[]=1814&catalog[]=1815&catalog[]=1825&catalog[]=1812&price_from=1&currency=EUR&price_to=20.00&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=2319"
URL_SWEAT_TOMMY = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1811&catalog[]=267&catalog[]=1813&catalog[]=1814&catalog[]=1815&catalog[]=1825&catalog[]=1812&price_from=1&currency=EUR&price_to=20.00&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=94&brand_id[]=352755"
URL_SWEAT_NIKE_TECH = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1812&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=53&price_to=30"

WEBHOOK_URL_FREE_BOT = "https://discord.com/api/webhooks/1018306492945932358/fwE3Tl7Pi4JRRZggbZZmLWCE_2GmfEk8ydMAsiOn-VI56aIty5o6t4dYb9atyENxspwa"
WEBHOOK_URL_TSHIRT_NIKE = "https://discord.com/api/webhooks/1018270137813573673/hhJ3hyeB1rgSiDttwCc5JJfuA_kjhWq78rvn82gop3vNcjqDWogrDXViccUwCjpTBFc6"
WEBHOOK_URL_TSHIRT_LACOSTE = "https://discord.com/api/webhooks/1018270289538326558/9P02JKVuot6mJfQazwreqEyJGmx08bM-MQabQaS6sjaTIW-v2je95I-wAfbxShigfcPW "
WEBHOOK_URL_TSHIRT_RALPH = "https://discord.com/api/webhooks/1018270428239765635/oy-c4axgeQ4WsPmIH0lTI82uD_VTdXpo5U0m3Abiyz_kmkq3vto27WSqNWcoiUiza_e9 "
WEBHOOK_URL_TSHIRT_TNF = "https://discord.com/api/webhooks/1018297089274417263/m8kEN7TkYyNDYuwnwo547qtHgCRUT8xVlzUfok-fmR16ApqoDiZoF8z3pPrk9R_oM5UQ"
WEBHOOK_URL_TSHIRT_TOMMY = "https://discord.com/api/webhooks/1018297308204498994/rb5IT80uPy0QkeFnSUzXzmSQ8gLGG5LRVgJtrOI7LhViQfX3PYzxySfHjTIT43dEpBSt "
WEBHOOK_URL_SWEAT_NIKE = "https://discord.com/api/webhooks/1018191923258867762/_MOMwTTDfIp7W8HXa41nTB30Qju31Fgs5DKnG4PNNa7Z9-f9LA05gLvUlJb02Jn6I9y7 "
WEBHOOK_URL_SWEAT_LACOSTE = "https://discord.com/api/webhooks/1018192348154433617/eMvu99lOH0PIG-n6tHNuN-h_rJ0eCuBYSxPf6PlLjy4lmKIbZHGb4YwGbl0pHO6xj02i "
WEBHOOK_URL_SWEAT_RALPH = "https://discord.com/api/webhooks/1017532663231430727/2ZwyDA3C0nWmZ82J0UxvMHYPI37DzoFlAc5OMjWNmZTz8rU4kE-F8JFsZLSe5SSCUET0 "
WEBHOOK_URL_SWEAT_TNF = "https://discord.com/api/webhooks/1018297759352238141/O9gA4x2el3pY5kKkJxtMo_CA_UieuMJzfMYDzVK0sLtIeL_nZzSLhMc9G1W0TM0VMtp- "
WEBHOOK_URL_SWEAT_TOMMY = "https://discord.com/api/webhooks/1018297971223306321/x3CAb-qLS6dKZbwx27fhfSGkdvvHTmvlHykUaieAsyyrGDtTpMrXVZyZE0qDovxdwGah "
WEBHOOK_URL_SWEAT_NIKE_TECH = "https://discord.com/api/webhooks/1018597731977154630/B2qQgRTkkJztB8tJ0HJUDv8CBEe_JLjD8R_BetV59GADTqShFNrvgHxCYLVFAlGJBB52"

while True:
    try:
        print("FREE BOT dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_FREE_BOT, WEBHOOK_URL_FREE_BOT)
        print("TSHIRT NIKE dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_TSHIRT_NIKE, WEBHOOK_URL_TSHIRT_NIKE)
        print("TSHIRT LACOSTE dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_TSHIRT_LACOSTE, WEBHOOK_URL_TSHIRT_LACOSTE)
        print("TSHIRT RALPH dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_TSHIRT_RALPH, WEBHOOK_URL_TSHIRT_RALPH)
        print("TSHIRT TNF dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_TSHIRT_TNF, WEBHOOK_URL_TSHIRT_TNF)
        print("TSHIRT TOMMY dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_TSHIRT_TOMMY, WEBHOOK_URL_TSHIRT_TOMMY)
        print("SWEAT NIKE dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_SWEAT_NIKE, WEBHOOK_URL_SWEAT_NIKE)
        print("SWEAT LACOSTE dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_SWEAT_LACOSTE, WEBHOOK_URL_SWEAT_LACOSTE)
        print("SWEAT RALPH dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_SWEAT_RALPH, WEBHOOK_URL_SWEAT_RALPH)
        print("SWEAT TNF dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_SWEAT_TNF, WEBHOOK_URL_SWEAT_TNF)
        print("SWEAT TOMMY dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_SWEAT_TOMMY, WEBHOOK_URL_SWEAT_TOMMY)
        print("SWEAT NIKE TECH " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_SWEAT_NIKE_TECH, WEBHOOK_URL_SWEAT_NIKE_TECH)
    except Exception:
        pass

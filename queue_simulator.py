from queue import Queue
import time
import random

queue = Queue()

def generate_request(request_id):
    print(f"Generating request with ID: {request_id}")
    queue.put(request_id)

def process_request():
    if not queue.empty():
        request_id = queue.get()
        print(f"Processing request with ID: {request_id}")
        time.sleep(1)
    else:
        print("The queue is empty. No requests to process.")

def main():
    print("Request processing system started. Press Ctrl+C to exit.")
    request_id = 1
    try:
        while True:
            for _ in range(random.randint(1, 3)):
                generate_request(request_id)
                request_id += 1
            
            for _ in range(random.randint(1, 3)):
                process_request()

            time.sleep(2)
    except KeyboardInterrupt:
        print("\nRequest processing system stopped.")

if __name__ == "__main__":
    main()

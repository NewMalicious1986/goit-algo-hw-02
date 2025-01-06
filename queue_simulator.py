from queue import Queue
import time
import random

# Create a queue
queue = Queue()

# Function to generate new requests
def generate_request(request_id):
    print(f"Generating request with ID: {request_id}")
    queue.put(request_id)

# Function to process requests
def process_request():
    if not queue.empty():
        request_id = queue.get()
        print(f"Processing request with ID: {request_id}")
        # Simulate request processing
        time.sleep(1)
    else:
        print("The queue is empty. No requests to process.")

# Main loop of the program
def main():
    print("Request processing system started. Press Ctrl+C to exit.")
    request_id = 1  # Unique request identifier
    try:
        while True:
            # Generate a random number of requests
            for _ in range(random.randint(1, 3)):
                generate_request(request_id)
                request_id += 1
            
            # Process a random number of requests
            for _ in range(random.randint(1, 3)):
                process_request()

            # Pause between iterations
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nRequest processing system stopped.")

if __name__ == "__main__":
    main()

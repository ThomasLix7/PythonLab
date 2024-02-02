import multiprocessing
import time


def wait_for_signal(conn):
    print("P2: Waiting for the 'START' signal...")
    while True:
        msg = conn.recv()
        if msg == 'START':
            print("P2: Received 'START' signal. Beginning task...")
            print('P2: I am continuing further with my code')
        # Perform the task here
            print("P2: Executing until received 'STOP' signal...")
        elif msg == 'STOP':
            print("P2: Received 'STOP' signal. Stopping task...")
            break
        else:
            print(f"Unexpected message: {msg}")


def send_start_signal(conn):
    print("P1: Sleeping for 5 seconds before sending the 'START' signal...")
    time.sleep(5)
    conn.send('START')
    print("P1: 'START' signal sent.")

    time.sleep(5)
    conn.send('STOP')
    print("P1: 'STOP' signal sent.")


if __name__ == "__main__":

    parent_conn, child_conn = multiprocessing.Pipe()
    # Create the processes
    p1 = multiprocessing.Process(target=send_start_signal, args=(parent_conn,))
    p2 = multiprocessing.Process(target=wait_for_signal, args=(child_conn,))
    # Start the processes
    p1.start()
    p2.start()

from threading import Event, Thread
from urllib.request import urlopen

file_name = None
def download_file(event,url):
    global file_name
    print(f"File downloading from the {url}")
    file_name=  url.split("/")[-1]
    data = None
    with urlopen(url) as response:
        data = response.read()

    if not data:
        raise Exception(f"Error:could not download the file")
    
    with open("./dist/sales/" + file_name, 'wb') as file:
        file.write(data)
    print(f"{file_name} was downloaded...")
    event.set()

def count_words(event):
    print(f"Waiting for the file to be downloaded....")
    event.wait()

    print(f"Received signal to count the words in the file")

    word_count =0
    with open("./dist/sales/"+file_name, 'r') as file:
        
        for line in file:
            words = line.split()
            word_count += len(words)
    
    print(f"The file {file_name} has {word_count} words")
        
def main():
    event = Event()

    download_thread = Thread(target=download_file, args=(event,"https://www.ietf.org/rfc/rfc793.txt"))
    word_count_thread = Thread(target=count_words, args=(event,))

    download_thread.start()
    word_count_thread.start()

    download_thread.join()
    word_count_thread.join()

    print("All threads have finished execution.")

if __name__=="__main__":
    main()
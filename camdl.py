import requests, time, datetime

target_count = input("How many times would you like to download each video? ")
target_count = int(target_count)
print("Tfl jamcams refresh around every three minutes.")

interval = input("Interval between downloads (in mins): ")
interval = int(interval) * 60

def download_video_series(video_links):
    stamp = datetime.datetime.now()
    for name, url in video_links.items():

        file_name = url.split('/')[-1].split('.')[-2]
        file_name = name + " (" + str(stamp.strftime("%d %b, %Y - %H.%M")) + ").mp4"

        # create response object
        r = requests.get(url, stream = True)

        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)

        print("Downloaded", file_name)

    return

# links = ["https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/00001.07450.mp4"]
links = {
"Picadilly Circus":"https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/00001.07450.mp4",
"Loampit Vale":"https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/00001.03706.mp4",
"Westminster Bridge":"https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/00001.04502.mp4",
"London Bridge":"https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/00001.02002.mp4",
}

count = 1

while count <= target_count:
    print("Running iteration: " + str(count) + ".\n")
    download_video_series(links)
    time.sleep(interval)
    count += 1

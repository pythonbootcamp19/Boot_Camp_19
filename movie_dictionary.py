input_data = """
Video
(HD - Movies)
Alita.Battle.Angel.2019.1080p.WEBRip.x264-MP4
Magnet linkThis torrent has 5 comments.Trusted Uploaded 06-29 08:46, Size 1.96 GiB, ULed by MrStark	7226	853
Video
(HD - Movies)
Hellboy.2019.1080p.WEBRip.x264-MP4
Magnet linkThis torrent has 1 comments.Trusted Uploaded 07-09 19:17, Size 1.95 GiB, ULed by MrStark	6439	996
Video
(HD - Movies)
Long.Shot.2019.720p.WEBRip.x264-MP4
Magnet linkTrusted Uploaded 07-16 17:27, Size 1.03 GiB, ULed by MrStark	3905	1003
Video
(HD - Movies)
Dumbo (2019) [BluRay] [1080p]
Magnet linkThis torrent has 2 comments.VIP Uploaded 06-14 23:19, Size 1.79 GiB, ULed by surferbroadband	4188	509
Video
(HD - Movies)
Alita.Battle.Angel.2019.720p.WEBRip.x264-MP4
Magnet linkThis torrent has 1 comments.Trusted Uploaded 06-29 08:45, Size 1.02 GiB, ULed by MrStark	3712	596
Video
(HD - Movies)
Long.Shot.2019.1080p.WEBRip.x264-MP4
Magnet linkTrusted Uploaded 07-16 17:28, Size 1.99 GiB, ULed by MrStark	2850	1175
"""
splitted_data = input_data.split("\n")
clean_splitted_data = splitted_data[1:-1]
#print(clean_splitted_data)
#range(start,end,skip)
for i in range(0,len(clean_splitted_data),4):
    torrent_type = clean_splitted_data[i]
    section = clean_splitted_data[i+1]
    name = clean_splitted_data[i+2]
    details = clean_splitted_data[i+3]

    section = section.strip("()")
    #print(f"{torrent_type}\n{section}\n{name}\n{details}\n")

def detail_parser(details):
    important_details = details.split("Uploaded")[1].strip()

    upload_time = important_details.split(",")[0]

    size = important_details.split(",")[0]

    everything_else = important_details.split(",")[2]

    parsed_detail = {"upload_time": upload_time,
                    "size": size,
                    "everything_else": everything_else}
    everything_else_sliced = everything_else.split(' ')

    print(everything_else_sliced)


    return parsed_detail

print(detail_parser(details))


##----
# print(len(everything_else_sliced))
# print(everything_else_sliced)

#print(detail_parser(details))

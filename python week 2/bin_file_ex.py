#function copy_file(source, dest) that takes the paths of source file and destination
#file and copies the binary data from the source file to the destination file

# def copy_file(source, dest):
#     with open(source, "rb") as f:
#         data = f.read()
#     with open(dest, "wb") as f2:
#         f2.write(data)

# copy_file("source.jpg", "dest.jpg")

#correction, another way

def copy_file(source, dest, chunk_size=2048, log_messages=True):
    with open(source, "rb") as source_file, open(dest, "wb") as dest_file:
        buffer = source_file.read(chunk_size)
        while buffer:
            n_bytes_written = dest_file.write(buffer)
            if log_messages:
                print(f"{n_bytes_written} bytes were copied successfully")
            buffer = source_file.read(chunk_size)

# copy_file("source.jpg", "dest.jpg")

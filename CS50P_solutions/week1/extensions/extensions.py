def Main():
    file = input("File name:")
    if not "." in file:
        print("application/octet-stream")
        return
    else:
        file = file.strip().lower().rsplit(".", maxsplit=1)[1]
        #print(file)
        match file:
            case("gif"):
                print("image/gif")
            case("jpg"):
                print("image/jpeg")
            case("jpeg"):
                print("image/jpeg")
            case("png"):
                print("image/png")
            case("pdf"):
                print("application/pdf")
            case("txt"):
                print("text/plain")
            case("zip"):
                print("application/zip")
            case _:
                print("application/octet-stream")
Main()

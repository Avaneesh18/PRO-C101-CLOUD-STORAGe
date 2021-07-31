import dropbox 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'CL1U7haZYgAAAAAAAAAAAY5IxNESjYP-gQrKvGR--c4tRGiAPzhLfev1JOK6yw0p'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to enter: ")
    file_to = input("Enter the full path to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("file is in dropbox as you wished: ")

main()
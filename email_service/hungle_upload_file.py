def handle_uploaded_file(f, title):

    with open('./media/{}.csv'.format(title), 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)
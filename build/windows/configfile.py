import os
appdata= os.getenv('APPDATA')
if not os.path.exists(f'{appdata}/supernote'):
    os.makedirs(f'{appdata}/supernote')
bdd_path=f'{appdata}/supernote/supernote.db'
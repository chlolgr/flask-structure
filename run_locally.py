from app import app
from flask import url_for

@app.context_processor
def override_url_for():
	return dict(url_for=dated_url_for)

import os
def dated_url_for(endpoint, **values):
	if endpoint == 'static':
		filename = values.get('filename', None)
		if filename:
			file_path = os.path.join(app.root_path,
								 endpoint, filename)
			values['q'] = int(os.stat(file_path).st_mtime)
	return url_for(endpoint, **values)

app.config['DEBUG'] = True
app.run(port=5002)

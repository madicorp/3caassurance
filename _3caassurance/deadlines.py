import os
import tempfile


def _copy_in_tmp_file(uploaded_deadline_file):
    _, file_extension = os.path.splitext(uploaded_deadline_file.name)
    deadline_tempfile = tempfile.TemporaryFile(suffix=file_extension)
    # Copy uploaded file in temp file
    for chunk in uploaded_deadline_file.chunks():
        deadline_tempfile.write(chunk)
    # Return to the beginning so that the tmp file can be read
    deadline_tempfile.seek(0)
    return deadline_tempfile


def send_deadlines(uploaded_deadline_file):
    deadline_tmp_file = _copy_in_tmp_file(uploaded_deadline_file)
    # Close will delete after read
    deadline_tmp_file.close()

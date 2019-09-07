import re
import time


def file_upload_to(instance, folder, filename):
    """
    Helper function to specify where the file should be uploaded
    Append current timestamp so that re-uploading file with same name does replace old file.
    Replace special characters from the file name with underscore
    """
    timestamp = int(time.time())
    format_name = u'{}_{}'.format(timestamp, filename)
    return u'uploads/{}/{}'.format(folder, re.sub('([^a-zA-Z0-9\.\_\-]+)', '_', format_name))

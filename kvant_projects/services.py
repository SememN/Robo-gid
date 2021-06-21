from . import models


def get_projects():
    '''returns all kvantoriums projects'''
    return models.Project.objects.all()

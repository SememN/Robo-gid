from .models import ItCourse, AutoCourse, AeroCourse, PromDesCourse, PromRoboCourse, HiTechCourse,\
    ItDescription, AutoDescription, AeroDescription, PromDesDescription,\
    PromRoboDescription, HiTechDescription


def get_creds(kvant_name: str):
    '''function to get creds to load page about kvantum and it's courses'''
    courses_bd = {
        'it': [ItDescription.objects.get(id=4), ItCourse.objects.all()],
        'auto': [AutoDescription.objects.get(id=2), AutoCourse.objects.all()],
        'aero': [AeroDescription.objects.get(id=1), AeroCourse.objects.all()],
        'design': [PromDesDescription.objects.get(id=5), PromDesCourse.objects.all()],
        'robo': [PromRoboDescription.objects.get(id=6), PromRoboCourse.objects.all()],
        'hi-tech': [HiTechDescription.objects.get(id=3), HiTechCourse.objects.all()]
    }

    if kvant_name == 'it':
        return courses_bd['it']
    if kvant_name == 'auto':
        return courses_bd['auto']
    if kvant_name == 'aero':
        return courses_bd['aero']
    if kvant_name == 'design':
        return courses_bd['design']
    if kvant_name == 'robo':
        return courses_bd['robo']
    if kvant_name == 'hi-tech':
        return courses_bd['hi-tech']

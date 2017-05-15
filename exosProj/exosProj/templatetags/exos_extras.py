from django import template
from datetime import timedelta, datetime

register = template.Library()

@register.simple_tag
def is_eligible(b):
    '''
    return 'allowed' if user is 13 years old or older

    return 'blocked' if user is under 13 or does not have a birth date listed
    '''
    if b is None:
        return 'blocked'
    
    birthday = datetime.combine(b, datetime.min.time())
    if datetime.now().year - birthday.year - ((datetime.now().month, datetime.now().day) < (birthday.month, birthday.day)) >= 13:
        return 'allowed'

    return 'blocked'

@register.simple_tag
def bizz_fuzz(num):
    '''
    return 'Bizz' if num % 3 == 0

    return 'Fuzz' if num % 5 == 0

    return 'BizzFuzz' if num % 3 == 0 and num % 5 == 0
    '''
    ret = ''

    if num % 3 == 0:
        ret = 'Bizz'

    if num % 5 == 0:
        ret = ret + 'Fuzz'

    if ret == '':
        ret = num

    return ret

    

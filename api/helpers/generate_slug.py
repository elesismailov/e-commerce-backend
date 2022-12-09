

from slugify import slugify

def generate_slug(*args):
    
    try:
        slug = slugify(' '.join([str(i) for i in args]))

    except Exception:

        print('error')
        return None

    return slug
